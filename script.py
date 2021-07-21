import speech_recognition as speech
recognizer = speech.Recognizer()
mic = speech.Microphone()

with mic as source:
    recognizer.adjust_for_ambient_noise(source)
    audio = recognizer.listen(source)
    transcript = recognizer.recognize_google(audio)
    print(transcript)