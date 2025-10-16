import os
import sys
import argparse

import azure.cognitiveservices.speech as speechsdk

#  load environment variables from a .env file if present
try:
    from dotenv import load_dotenv
    load_dotenv()
except Exception:
    # If python-dotenv isn't installed, continue; env vars can still be provided
    pass
def transcribe_from_file(audio_path: str, subscription: str, region: str, language: str = "ar-AE") -> str:
    """Transcribe a single short audio file using Azure Speech SDK.

    Inputs:
    - audio_path: path to a WAV (16-bit PCM) file
    - subscription: Azure Speech subscription key or use env var
    - region: Azure service region
    - language: speech recognition language (default: Arabic - United Arab Emirates)

    Returns:
    - The recognized text on success, or raises an exception on failure.
    """
    if not os.path.exists(audio_path):
        raise FileNotFoundError(f"Audio file not found: {audio_path}")

    speech_config = speechsdk.SpeechConfig(subscription=subscription, region=region, speech_recognition_language=language)
    audio_input = speechsdk.AudioConfig(filename=audio_path)
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_input)

    print(f"Transcribing file: {audio_path}")
    result = speech_recognizer.recognize_once_async().get()

    if result.reason == speechsdk.ResultReason.RecognizedSpeech:
        return result.text
    elif result.reason == speechsdk.ResultReason.NoMatch:
        raise RuntimeError("No speech could be recognized from the audio file.")
    else:
        raise RuntimeError(f"Speech recognition failed: {result.reason}")


def main():
 

    # Preference order: CLI args > environment variables (including .env loaded vars)
    subscription = os.getenv("AZURE_SPEECH_KEY")
    region = os.getenv("AZURE_SPEECH_REGION")
    language = os.getenv("AZURE_SPEECH_LANGUAGE","ar-AE")

    if not subscription or not region:
        print("Error: subscription key and region are required. Provide via CLI or set AZURE_SPEECH_KEY and AZURE_SPEECH_REGION env vars.")
        sys.exit(2)

    try:
        audio_file = input("Enter path to audio file (wav recommended): ")
        text = transcribe_from_file(audio_file, subscription, region, language)
        print("--- Transcription result ---")
        print(text)
    except Exception as e:
        print(f"Error during transcription: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
