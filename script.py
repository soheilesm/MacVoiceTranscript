import speech_recognition as speech
from datetime import datetime

recognizer = speech.Recognizer()
mic = speech.Microphone()

with mic as source:
    print("Please say something, and the script of what you talk about will get generated ...")
    recognizer.adjust_for_ambient_noise(source)
    audio = recognizer.listen(source)
    transcript = recognizer.recognize_google(audio)
    print("The transcript of what you just sid is: ", transcript)
    audio_filename = datetime.now().strftime("%Y%m%d-%H%M%S")
    with open("./audio_" + audio_filename + ".wav", "wb") as file:
        file.write(audio.get_wav_data())