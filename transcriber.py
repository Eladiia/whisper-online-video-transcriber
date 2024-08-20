import os
import subprocess
import time
import pyperclip
from faster_whisper import WhisperModel
import re

os.environ['KMP_DUPLICATE_LIB_OK'] = 'TRUE'

# Function to download audio from YouTube
def dl_yt(youtube_id, output_dir):
    audio_file_name = os.path.join(output_dir, f"{youtube_id}.mp3")
    subprocess.run(f"yt-dlp -x --audio-format mp3 -o {audio_file_name} https://youtu.be/{youtube_id}", shell=True)
    return audio_file_name

# Function to format seconds to time format
def seconds_to_time_format(s):
    hours = s // 3600
    s %= 3600
    minutes = s // 60
    s %= 60
    seconds = s // 1
    milliseconds = round((s % 1) * 1000)
    return f"{int(hours):02d}:{int(minutes):02d}:{int(seconds):02d},{int(milliseconds):03d}"

# Function to transcribe video
def transcribe_video(audio_source, output_dir, model_size="medium", vad_duration=900, language="ja"):
    try:
        # Create output directory if it doesn't exist
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        # Load the Whisper model
        model = WhisperModel(model_size, device="cuda", compute_type="float32")

        # Transcribe the audio
        segments, info = model.transcribe(
            audio_source,
            beam_size=5,
            language=language,
            initial_prompt=None,
            word_timestamps=False,
            vad_filter=True,
            vad_parameters=dict(min_silence_duration_ms=vad_duration)
        )

        # Output transcription results
        print(f"Detected language '{info.language}' with probability {info.language_probability}\n")

        # Save the transcription to a file
        transcript_file_name = os.path.join(output_dir, f"{os.path.splitext(os.path.basename(audio_source))[0]}.srt")
        sentence_idx = 1
        with open(transcript_file_name, 'w', encoding='utf-8') as f:
            for segment in segments:
                ts_start = seconds_to_time_format(segment.start)
                ts_end = seconds_to_time_format(segment.end)
                print(f"[{ts_start} --> {ts_end}] {segment.text.strip()}")
                f.write(f"{sentence_idx}\n")
                f.write(f"{ts_start} --> {ts_end}\n")
                f.write(f"{segment.text.strip()}\n\n")
                sentence_idx += 1

        print(f"Transcript file created: {transcript_file_name}")

    except Exception as e:
        print(f"An error occurred: {e}")

# Main function to monitor clipboard and process URLs
def main():
    previous_text = ""
    default_output_dir = os.path.expanduser("~/Transcriptions")

    while True:
        try:
            # Check clipboard content
            clipboard_text = pyperclip.paste().strip()
            if clipboard_text != previous_text:
                previous_text = clipboard_text

                # Check if the clipboard content is a URL
                if clipboard_text.startswith("http://") or clipboard_text.startswith("https://"):
                    # Ask for output directory, model size, language, and VAD filter
                    output_dir = input(f"Enter output directory (default: {default_output_dir}): ").strip() or default_output_dir
                    model_size = input("Enter the Whisper model size (tiny, base, small, medium, large): ").strip()
                    vad_duration = int(input("Enter the VAD filter minimum silence duration in ms (e.g., 900): ").strip())
                    language = input("Enter the language code (e.g., 'ja' for Japanese, 'en' for English): ").strip()

                    # Detect YouTube URL
                    if "youtube.com/watch?v=" in clipboard_text or "youtu.be/" in clipboard_text:
                        print(f"Detected YouTube URL: {clipboard_text}")

                        # Extract video ID
                        if "youtube.com/watch?v=" in clipboard_text:
                            video_id = clipboard_text.split("youtube.com/watch?v=")[-1].split("&")[0]
                        elif "youtu.be/" in clipboard_text:
                            video_id = clipboard_text.split("youtu.be/")[-1].split("?")[0]

                        print(f"Extracted video ID: {video_id}")

                        # Start transcription process
                        transcribe_video(dl_yt(video_id, output_dir), output_dir, model_size=model_size, vad_duration=vad_duration, language=language)

                    else:
                        # Non-YouTube URL
                        print(f"Detected non-YouTube URL: {clipboard_text}")

                        # Start transcription process using the provided URL as audio source
                        transcribe_video(clipboard_text, output_dir, model_size=model_size, vad_duration=vad_duration, language=language)

            time.sleep(5)  # Check clipboard every 5 seconds

        except Exception as e:
            print(f"An error occurred: {e}")
            time.sleep(5)  # Wait before retrying

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        input("Press Enter to exit...")
