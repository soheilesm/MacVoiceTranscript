# MacVoiceTranscript
Generate the transcript of your own speeches using your own Mac and open applications

---
### Installation:
On your Mac try installing `portaudio` using `homebrew` through the below commands in the terminal:
```
brew install portaudio
```

We also install some python libraries such as [SpeechRecognition](https://pypi.org/project/SpeechRecognition/) which is a library for performing speech recognition and converting speech to text and [pyaudio](https://pypi.org/project/PyAudio/) which is a cross-platform audio input/output stream library that is required for accessing to the Mac's microphone. The aforementioned libraries can be installed using the `pip` package as:
```
pip install SpeechRecognition
pip install pyaudio
```

--> You can install all packages by running the bash file `install_packages.sh`.
