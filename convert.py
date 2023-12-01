from pydub import AudioSegment

def convertir_mp3_a_wav(archivo_mp3, archivo_wav):
    """
    Convierte un archivo de audio MP3 a formato WAV.

    :param archivo_mp3: Ruta del archivo MP3 original.
    :param archivo_wav: Ruta del archivo WAV convertido.
    """
    # Convertir MP3 a WAV
    sound = AudioSegment.from_mp3(archivo_mp3)
    sound.export(archivo_wav, format="wav")

# Ruta del archivo MP3 original
archivo_mp3 = "halloween.mp3"

# Ruta del archivo WAV convertido
archivo_wav = "halloween.wav"

# Llamada a la función para realizar la conversión
convertir_mp3_a_wav(archivo_mp3, archivo_wav)