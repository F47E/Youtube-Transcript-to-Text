import requests 
from bs4 import BeautifulSoup  
from youtube_transcript_api import YouTubeTranscriptApi  
import os

# Function to get the title of a YouTube video
def get_video_title(url):
    # Make an HTTP request to the provided URL
    response = requests.get(url)
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')
    # Find the <title> tag and extract its text, removing the suffix " - YouTube"
    title = soup.find('title').text.replace(' - YouTube', '')
    return title

# Function to download and save the transcript of a YouTube video
def download_transcript(video_id):
    # Fetch the transcript for the given video ID
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    # Construct the filename for the transcript file
    filename = f"{video_id}_transcript.txt"
    # Get the absolute path where the file will be saved
    filepath = os.path.join(os.getcwd(), filename)
    # Open the file for writing
    with open(filepath, "w", encoding="utf-8") as file:
        # Write each segment of the transcript to the file
        for entry in transcript:
            file.write(f"{entry['text']}\n")
    # Inform the user that the transcript has been saved
    print(f"Transcript saved as {filename}")
    # Print the absolute path of the saved file
    print(f"File location: {filepath}")

# Function to prompt the user with a yes/no question
def yes_or_no(question):
    while "the answer is invalid":
        # Prompt the user and get their response
        reply = str(input(question+' (Y/N): ')).lower().strip()
        # Return True for "yes" responses
        if reply[:1] == 'y':
            return True
        # Return False for "no" responses
        if reply[:1] == 'n':
            return False

# Main execution block
if __name__ == "__main__":
    # Prompt the user to provide a YouTube video URL
    video_url = input("Please provide the YouTube video URL: ")
    # Extract the video ID from the URL
    video_id = video_url.split('v=')[1]
    # Retrieve and print the video title
    title = get_video_title(video_url)
    print(f"Video title: {title}")
    # Ask the user to confirm if the fetched title corresponds to the correct video
    if yes_or_no("Is this the correct video?"):
        # If confirmed, download and save the transcript
        download_transcript(video_id)
    else:
        # If not confirmed, exit the script
        print("Exiting...")
