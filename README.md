# English Listening and Speaking Practice Project with YouTube Video Questions

This project aims to provide a tool for practicing listening and speaking skills in English. It utilizes the YouTubeTranscriptApi service to obtain transcriptions from YouTube videos and then generates questions based on those transcriptions using the OpenAI API (GPT-3.5-turbo).

## Project Setup

### Prerequisites
- Ensure you have Python installed on your system.
- Install the required libraries using the following command:
```
pip install youtube_transcript_api openai

```

### Obtain an OpenAI API Key
1. Get an API key from OpenAI at [OpenAI Platform](https://beta.openai.com/signup/).
2. Save your API key in a file named `api_key.txt` in the same directory as your script.

## Using the Project

1. Define the URL of the YouTube video you want to use in the `url` variable.
2. Run the script to extract the YouTube ID and obtain the subtitle transcriptions.
3. The transcription will be processed, and a series of questions based on the video content will be generated.
4. Answer the questions out loud to improve your listening and speaking skills.

## Project Structure

- `youtube_id_extract`: Function to extract the YouTube video ID from a link.
- `read_youtube_captions`: Function to obtain subtitle transcriptions from a YouTube video.
- `read_api_key_from_file`: Function to read the OpenAI API key from a file.
- `if __name__ == "__main__":` Main script block that utilizes the above functions to generate questions based on video transcriptions.

