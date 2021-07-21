import speech_recognition as speech
recognizer = speech.Recognizer()
mic = speech.Microphone()

with mic as source:
    print("Hey There! Please say something, and we will generate the script of what you talk about :)")
    recognizer.adjust_for_ambient_noise(source)
    audio = recognizer.listen(source)
    transcript = recognizer.recognize_google(audio)
    print("The transcript of what you just sid is: ", transcript)