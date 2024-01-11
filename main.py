from youtube_transcript_api import YouTubeTranscriptApi
import os
from openai import OpenAI
# assigning srt variable with the list
# of dictionaries obtained by the get_transcript() function
import re

def youtube_id_extract(url):
    # Patrón de expresión regular para extraer el ID de un enlace de YouTube
    patron = re.compile(r'(?:youtube\.com\/(?:[^\/\n\s]+\/\S+\/|(?:v|e(?:mbed)?)\/|\S*?[?&]v=)|youtu\.be\/)([a-zA-Z0-9_-]{11})')

    # Buscar el ID en la URL
    coincidencias = patron.search(url)

    # Verificar si se encontraron coincidencias
    if coincidencias:
        return coincidencias.group(1)
    else:
        return None


def read_youtube_captions(youtube_address):
    youtube_id = youtube_id_extract(youtube_address)
    srt = YouTubeTranscriptApi.get_transcript(youtube_id)
    return srt
srt = YouTubeTranscriptApi.get_transcript("hocIsO66UPU")

caption_text = ' '.join(item['text'] for item in srt)



def read_api_key_from_file(nombre_archivo='api_key.txt'):
    try:
        with open(nombre_archivo, 'r') as archivo:
            api_key = archivo.read().strip()
            return api_key
    except FileNotFoundError:
        print(f"El archivo {nombre_archivo} no se encuentra.")
        return None



if __name__ == "__main__":
    url = "https://www.youtube.com/watch?v=hocIsO66UPU"
    print(youtube_id_extract(url))
    
    captions = read_youtube_captions(url)
    
    
    # Obtiene la clave de API desde el archivo
    clave_de_api = read_api_key_from_file()

    if clave_de_api:
        print(f"Clave de API obtenida: {clave_de_api}")
        # Aquí puedes continuar con el resto de tu código utilizando la clave de API
    else:
        print("No se pudo obtener la clave de API.")
    client = OpenAI(
        # This is the default and can be omitted
        api_key = clave_de_api
    ,
    )

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content":f"Read this text taken from the YouTube captions, and ask me 10 questions to see if I understood it. At the end, add a solutions place with the correct answers. Add 10 break lines in blank between questions and answers:\n\n{caption_text}"

            }
        ],
        model="gpt-3.5-turbo",
    )
    print(chat_completion.choices[0].message.content)
