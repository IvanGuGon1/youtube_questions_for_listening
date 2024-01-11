from youtube_transcript_api import YouTubeTranscriptApi
import re
from openai import OpenAI


def extract_youtube_id(url):
    """
    Extracts the YouTube video ID from a given URL.
    """
    pattern = re.compile(r'(?:youtube\.com\/(?:[^\/\n\s]+\/\S+\/|(?:v|e(?:mbed)?)\/|\S*?[?&]v=)|youtu\.be\/)([a-zA-Z0-9_-]{11})')
    match = pattern.search(url)
    if match:
        return match.group(1)
    else:
        return None


def get_captions_from_youtube(url):
    """
    Retrieves the captions of a YouTube video using its URL.
    """
    youtube_id = extract_youtube_id(url)
    captions = YouTubeTranscriptApi.get_transcript(youtube_id)
    return captions


def read_api_key_from_file(file_name='api_key.txt'):
    """
    Reads the API key from a file.
    """
    try:
        with open(file_name, 'r') as file:
            api_key = file.read().strip()
            return api_key
    except FileNotFoundError:
        print(f"The file {file_name} does not exist.")
        return None


if __name__ == "__main__":
    
    youtube_url = "https://www.youtube.com/watch?v=hocIsO66UPU"

    captions = get_captions_from_youtube(youtube_url)
    caption_text = ' '.join(item['text'] for item in captions)

    api_key = read_api_key_from_file()

    if api_key:
        print(f"API key obtained:")
    else:
        print("Failed to obtain the API key.")

    client = OpenAI(api_key=api_key)

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": f"Read this text taken from the YouTube captions, and ask me 10 questions to see if I understood it. At the end, add a solutions place with the correct answers. Add 10 break lines in blank between questions and answers:\n\n{caption_text}"
            }
        ],
        model="gpt-3.5-turbo",
    )
    print(chat_completion.choices[0].message.content)