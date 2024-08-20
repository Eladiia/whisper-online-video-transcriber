# Whisper Online Video Transcriber

Whisper Online Video Transcriber is a Python-based script designed to download and transcribe audio from both YouTube and third-party video URLs using the Faster Whisper model. The script allows users to specify the language, Whisper model size, and VAD (Voice Activity Detection) filter settings for accurate transcription.

## Features

- **Support for YouTube and Non-YouTube Videos**: Automatically detects YouTube URLs and downloads the audio for transcription. For non-YouTube URLs, it directly downloads the video using `yt-dlp`.
- **Customizable Settings**: Users can choose the Whisper model size, transcription language, and VAD filter settings.
- **Flexible Output Directory**: Users can specify their preferred output directory for storing transcriptions.

## Requirements

- Python 3.x
- `yt-dlp` for downloading videos
- `faster-whisper` for transcription
- CUDA (optional, but recommended for faster performance)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/whisper-online-video-transcriber.git
   cd whisper-online-video-transcriber
   pip install -r requirements.txt

# Usage
1. Run the script:
`python transcriber.py`
2. Copy a YouTube or non-YouTube video URL to your clipboard.

3. The script will prompt you to select the Whisper model size, language, and VAD filter settings.

4. The transcription will be saved in the specified output directory.
