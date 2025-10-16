# Azure Speech-to-Text from File

This small script transcribes a local audio file using Azure Cognitive Services Speech SDK for Python.

Requirements
- Python 3.7+
- Install dependencies: `pip install -r requirements.txt`

Usage

Set environment variables or pass subscription and region on the command line:

```
export AZURE_SPEECH_KEY=your_subscription_key
export AZURE_SPEECH_REGION=your_region
python main_from_file.py path/to/audio.wav
```

Notes
- Prefer WAV files encoded as 16-bit PCM. For other formats, convert before running.
- Default recognition language is `ar-AE`. Pass `--language` to change.
