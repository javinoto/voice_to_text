# Proyecto de Conversión y Transcripción de Audio

Este proyecto permite convertir archivos de audio de formato MP3 a WAV y luego transcribirlos utilizando la API de Google Speech-to-Text.

## Descripción

El script `convert.py` se encarga de convertir archivos de audio en formato MP3 a WAV, haciendo uso de la biblioteca `pydub`. Posteriormente, el script `main.py` utiliza la biblioteca `speech_recognition` para transcribir el contenido de los archivos WAV a texto. Este proceso es útil para obtener transcripciones automáticas de grabaciones de audio.

## Requisitos Previos

Antes de ejecutar este proyecto, asegúrate de tener instalado Python en tu sistema. Además, necesitarás instalar las siguientes bibliotecas:

- pydub
- speech_recognition

Puedes instalarlas utilizando pip:

```bash
pip install pydub speechrecognition
```

También necesitarás tener instalado FFmpeg para la conversión de archivos de audio.

```bash
sudo apt-get install ffmpeg
```

## Uso

Para utilizar este proyecto, sigue estos pasos:

1. Coloca el archivo MP3 que deseas transcribir en el directorio del proyecto.
2. Ejecuta el script convert.py para convertir el archivo MP3 a WAV.
3. Ejecuta el script main.py para transcribir el archivo WAV a texto.
