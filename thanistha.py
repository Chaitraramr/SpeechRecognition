# To runt the project first wait first alxa to open microphone an


#import speech-- is package used for recongizing of speech
import speech_recognition as sr
#used for text conversion
import pyttsx3
#to play the order
import pywhatkit
import datetime
import wikipedia

listener = sr.Recognizer()

#text conversion
engine = pyttsx3.init()

'''To convert voice to female this is code but already in so not required
voices = engine.getProperty('voices')
engine.setproperty('voice',voices[1].id)'''

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print("I'm gonna catch u..........")
            print("Listening..........")
            voice =listener.listen(source)
            command=listener.recognize_google(voice)
            command=command.lower()
            if 'alexa' in command:
                command=command.replace('alexa','')
                print(command)
            
                
    except:
        pass
    return command

def run_alexa():
    command = take_command()
    if 'play' in command:
        song = command.replace('play','')
        talk('playing buddy'+song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M:%p')
        print(time)
        talk('current time is '+ time)
    elif 'get info on' in command:
        person = command.replace('get info on','')
        info = wikipedia.summary(person,1)
        print(info)
        talk(info)
    elif 'can you say something about thanvik' in command:
        talk('sorry, yar he is very naughty i cant say much ')
    else:
        talk('can you repeat it again')

while True:
    run_alexa()





