import os
import sys
import azure.cognitiveservices.speech as speechsdk

# Load .env if python-dotenv is available (optional)
try:
    from dotenv import load_dotenv
    load_dotenv()
except Exception:
    pass


def from_mic():
    subscription = os.getenv("AZURE_SPEECH_KEY")
    region = os.getenv("AZURE_SPEECH_REGION")

    if not subscription or not region:
        print("Error: AZURE_SPEECH_KEY and AZURE_SPEECH_REGION must be set in environment or .env file.")
        sys.exit(2)

    speech_config = speechsdk.SpeechConfig(subscription=subscription, region=region, speech_recognition_language="ar-AE")
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)

    print("Speak into your microphone.")
    speech_recognition_result = speech_recognizer.recognize_once_async().get()
    print(speech_recognition_result.text)


if __name__ == "__main__":
    from_mic()