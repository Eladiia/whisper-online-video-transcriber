# Whisper Online Video Transcriber

Python script designed to download and transcribe audio from both YouTube and third-party video URLs using the Faster Whisper model. The script allows to specify the language, Whisper model size, and VAD (Voice Activity Detection) filter settings for accurate transcription. **This is meant for personal use to use as an alternative for Google Colab (If you ran out of GPU time there), sharing this in case it helps someone. :)**

**Works better with ASBPlayer(https://github.com/killergerbah/asbplayer) for subtitle drop, and any video dl extension (such as FetchV on Chrome Store) to get the video URL of any site.**

https://github.com/user-attachments/assets/82496d7e-a9eb-400e-b7d6-79126b758fc0



## Features

- **Support for YouTube and Non-YouTube Videos**: Automatically detects YouTube URLs and downloads the audio for transcription. For non-YouTube URLs, it directly downloads the video using `yt-dlp`.
- **Customizable Settings**: Users can choose the Whisper model size, transcription language, and VAD filter settings.
- **Flexible Output Directory**: Users can specify their preferred output directory for storing transcriptions.

## Requirements

- Python 3.x
- `yt-dlp` for downloading videos
- `faster-whisper` for transcription
- `pyperclip` for clipboard monitoring
- `subprocess` for running external commands
- CUDA (optional, but recommended for faster performance)
- Ensure you have a CUDA-compatible GPU and the appropriate drivers installed if using GPU acceleration.
  
## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/eladiia/whisper-online-video-transcriber.git
   cd whisper-online-video-transcriber
   pip install yt-dlp faster-whisper pyperclip

# Usage
1. Run the script:
`python transcriber.py`
2. Copy a YouTube or non-YouTube video URL to your clipboard.

3. The script will prompt you to select the Whisper model size, language, and VAD filter settings.

4. The transcription will be saved in the specified output directory.
