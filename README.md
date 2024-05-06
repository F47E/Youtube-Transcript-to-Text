# Youtube-Transcript-to-Text

## Description

<p>Youtube-Transcript-to-Text is a Python script designed to extract transcripts from YouTube videos and save them as text files. This tool is particularly useful for users looking to convert the spoken content of YouTube videos into a readable format for various purposes such as content analysis, accessibility, or simply for reference. The script fetches the video title for confirmation and, upon user approval, downloads the video's transcript.</p>

## Prerequisites

Before running the script, ensure you have the following libraries installed:

- `requests`
- `beautifulsoup4`
- `youtube_transcript_api`

These libraries can be installed using pip. Additionally, the script is compatible with Python versions 3.6 and above.

## Installation

To install the required libraries, run the following command in your terminal or command prompt:

```bash
pip install requests beautifulsoup4 youtube_transcript_api
```

## Running the Script

### Windows

1. Open Command Prompt.
2. Navigate to the directory where the script is saved using `cd path\to\your\script`.
3. Run the script with:

```bash
python youtube_trans_to_text.py
```

### Mac and Linux

1. Open Terminal.
2. Change the directory to where the script is located with `cd path/to/your/script`.
3. Execute the script by running:

```bash
python youtube_trans_to_txt.py
```

## How to Use

After running the script, you will be prompted to enter the YouTube video URL. Once entered, the script will fetch and display the video title for confirmation. Respond with 'Y' (yes) if the title matches the video you intend to download the transcript for. The script will then proceed to download the transcript and save it as a text file named `{video_id}_transcript.txt` in the same directory as the script. If the video title does not match, respond with 'N' (no) to exit the script.

## Features

- Fetches and displays the YouTube video title for user confirmation.
- Downloads the video transcript and saves it as a text file.
- Supports multiple operating systems including Windows, Mac, and Linux.

## Note

This script relies on the availability of transcripts for the YouTube videos. Some videos may not have transcripts available due to various reasons such as the video owner's settings or the lack of generated captions for the video.
