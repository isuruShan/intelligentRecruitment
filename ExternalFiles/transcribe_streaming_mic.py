import argparse
import io
import os

from google.cloud import speech_v1p1beta1 as speech

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="/home/isuru/PycharmProjects/gSpeechTest/MyFirstProject-28a3d7098e7b.json"

def transcribe_file_with_auto_punctuation(path):
    """Transcribe the given audio file with auto punctuation enabled."""
    client = speech.SpeechClient()

    with io.open(path, 'rb') as audio_file:
        content = audio_file.read()
    audio = speech.types.RecognitionAudio(content=content)
    config = speech.types.RecognitionConfig(
        enable_automatic_punctuation=True,
        enable_word_time_offsets=True,
        encoding= speech.enums.RecognitionConfig.AudioEncoding.LINEAR16,
        language_code= 'en-US',
        model= 'default')

    response = client.recognize(config, audio)

    for i, result in enumerate(response.results):
        alternative = result.alternatives[0]
        print('-' * 20)
        print('First alternative of result {}'.format(i))
        print('Transcript: {}'.format(alternative.transcript))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('command')
    parser.add_argument(
        'path', help='File for audio file to be recognized')

    args = parser.parse_args()

    if args.command == 'punctuation':
        transcribe_file_with_auto_punctuation(args.path)