import speech_recognition as speech
from datetime import datetime
import subprocess
import os
import pyttsx3


def sample_speech_transcription_function():
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


def open_application(app_name):
    # get a list of application installed on your Mac

    d = '/Applications'
    apps = list(map(lambda x: x.split('.app')[0].lower(), os.listdir(d)))
    print(apps)
    # open the first app in the list
    app = app_name
    os.system('open ' +d+'/%s.app' %app.replace(' ','\ '))


def Mac_say(text):
    # your Mac talks to you

    engine = pyttsx3.init()
    # set the voice speed
    engine.setProperty("rate", 200)
    # set the voice agent - e.g., samantha
    engine.setProperty('voice', 'com.apple.speech.synthesis.voice.samantha')
    # read out the input 'text'
    engine.say(text)
    engine.runAndWait()
    

def search_engine():
    # TODO
    # build a search env for voice vs. system commands
    d = '/Applications'
    records = []
    apps = os.listdir(d)
    for app in apps:
        search = {}
        search['voice_command'] = 'open ' + app.split('.app')[0]
        search['sys_command'] = 'open ' + d +'/%s' %app.replace(' ','\ ')
        records.append(search)


def mac_voice_activattion(phrase='Hey there'):
    try:
        recognizer = speech.Recognizer()
        mic = speech.Microphone()
        with mic as source:
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)
            transcript = recognizer.recognize_google(audio)
            print(transcript.lower())
            if transcript.lower() == phrase.lower():
                return True
            else:
                return False
    except:
        pass



recognizer = speech.Recognizer()
mic = speech.Microphone()

while True:
    print("say the activation word <Hey there> to start ...")
    say("say the activation word <Hey there> to start ...")
    if mac_voice_activattion():
        try:
            Mac_say("Hey Soheil, what application do you want me to open for you?")
            with mic as source:
                print("Say Something!")
                # activate the microphone
                recognizer.adjust_for_ambient_noise(source)
                # record the audio
                audio = recognizer.listen(source)
                # get the transcription
                transcript = recognizer.recognize_google(audio)
                print(transcript)
                open_application(transcript)
                # sys_command = search(transcript)
                # os.system(sys_command)
                Mac_say("I opened the {} application for you".format(transcript))

        except:
            pass
    else:
        print("you didn't say the activation word ... Good bye!")
        Mac_say("you didn't say the activation word ... Good bye!")
        break