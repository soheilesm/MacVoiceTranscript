import speech_recognition as speech
from datetime import datetime
import subprocess
import os
import pyttsx3


def buffer():
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


def buffer2():
    # get a list of application installed on your Mac
    d = '/Applications'
    apps = list(map(lambda x: x.split('.app')[0], os.listdir(d)))
    print(apps)
    # open the first app in the list
    app = apps[0]
    os.system('open ' +d+'/%s.app' %app.replace(' ','\ '))


def buffer3():
    # your Mac talks to you
    def say(text):
        engine = pyttsx3.init()
        # set the voice speed
        engine.setProperty("rate", 200)
        # set the voice agent - e.g., samantha
        engine.setProperty('voice', 'com.apple.speech.synthesis.voice.samantha')
        # read out the input 'text'
        engine.say(text)
        engine.runAndWait()
        
    say("Hey! What can I do for you?")



def buffer4():
    # build a search env for voice vs. system commands
    d = '/Applications'
    records = []
    apps = os.listdir(d)
    for app in apps:
        search = {}
        search['voice_command'] = 'open ' + app.split('.app')[0]
        search['sys_command'] = 'open ' + d +'/%s' %app.replace(' ','\ ')
        records.append(search)


def mac_voice_activattion(phrase='Hey Mac!'):
    recognizer = speech.Recognizer()
    mic = speech.Microphone()
    with mic as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        transcript = recognizer.recognize_google(audio)
        if transcript.lower() == phrase:
            return True
        else:
            return False
