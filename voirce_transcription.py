import speech_recognition as speech
from datetime import datetime
import os

recognizer = speech.Recognizer()
mic = speech.Microphone()

with mic as source:
    # activate the microphone
    print("Please say something, and the script of what you talk about will get generated ...")
    recognizer.adjust_for_ambient_noise(source)

    # record the audio
    audio = recognizer.listen(source)

    # get the transcription
    transcript = recognizer.recognize_google(audio)
    print("The transcript of what you just sid is: ", transcript)

    # save the audio file
    audio_files_dir = './audio_files/'
    audio_filename = datetime.now().strftime("%Y%m%d-%H%M%S")
    if not os.path.exists(audio_files_dir): 
        os.makedirs(audio_files_dir)
    with open(audio_files_dir + "audio_" + audio_filename + ".wav", "wb") as file:
        file.write(audio.get_wav_data())