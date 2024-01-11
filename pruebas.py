import re

def extraer_id_youtube(url):
    # Patrón de expresión regular para extraer el ID de un enlace de YouTube
    patron = re.compile(r'(?:youtube\.com\/(?:[^\/\n\s]+\/\S+\/|(?:v|e(?:mbed)?)\/|\S*?[?&]v=)|youtu\.be\/)([a-zA-Z0-9_-]{11})')

    # Buscar el ID en la URL
    coincidencias = patron.search(url)

    # Verificar si se encontraron coincidencias
    if coincidencias:
        return coincidencias.group(1)
    else:
        return None

# Ejemplo de uso con la URL proporcionada
url_youtube = "https://www.youtube.com/watch?v=hocIsO66UPU"
id_youtube = extraer_id_youtube(url_youtube)

if id_youtube:
    print(f"ID de YouTube extraído: {id_youtube}")
else:
    print("No se pudo extraer el ID de YouTube.")
