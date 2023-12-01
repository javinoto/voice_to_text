import speech_recognition as sr
import convert

# Asegúrate de que el archivo convert.py haya completado la conversión antes de continuar
# Ruta del archivo WAV convertido
audio_path = convert.archivo_wav

# Inicializar el reconocedor
r = sr.Recognizer()

# Trabajar con el archivo de audio
with sr.AudioFile(audio_path) as source:
    audio = r.record(source)  # Leer el archivo completo

# Intentar realizar la transcripción utilizando el reconocedor de Google
try:
    text = r.recognize_google(audio, language="es-ES")  # Asume que el audio está en español
    print("Transcripción del audio:\n", text)
except sr.UnknownValueError:
    print("Google Speech Recognition no pudo entender el audio")
except sr.RequestError as e:
    print(f"No se pudo solicitar resultados de Google Speech Recognition; {e}")
