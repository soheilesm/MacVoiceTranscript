# MacVoiceTranscript
Generate the transcript of your own speeches using your own Mac

---
### Installation:
On your Mac try installing `portaudio` and `elasticsearch` using `homebrew` through the below commands in the terminal:
```
brew install portaudio
brew install elasticsearch
```

We also install some python libraries such as [SpeechRecognition](https://pypi.org/project/SpeechRecognition/) which is a library for performing speech recognition and converting speech to text, [elasticsearch](https://pypi.org/project/elasticsearch/) which provides common ground for all elasticsearch related codes in Python, and [pyaudio](https://pypi.org/project/PyAudio/) which is a cross-platform audio input/output stream library that is required for accessing to the Mac's microphone. The aforementioned libraries can be installed using the `pip` package as:
```
pip install SpeechRecognition
pip install elasticsearch
pip install pyaudio
```
