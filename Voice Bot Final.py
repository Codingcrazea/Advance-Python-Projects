import datetime
import speech_recognition
import pyttsx3 as p

#Source Declaration
a = speech_recognition.Recognizer()
recordtime = 5
s = 0
engine= p.init()
rate = engine.getProperty("rate")  # get current property
volume = engine.getProperty("volume")
engine.setProperty("volume",50.0)
voice =engine.getProperty("voices")
engine.setProperty("voice",voice[1].id)
engine.setProperty("rate",170)

answer = {
    # For single answers
    "" : "Please give any command",
    "hello":"Hii",
    "who are you" : "I am a Voice Bot developed by Sanskar Jaiswal",
    "hu r u" : "I am a Voice Bot developed by Sanskar Jaiswal",
    "tell me your colledge name":"Oriental University",
    "tell me current time": datetime.datetime.now(),
    

}


def say():
    print ("listening....")
    bol ("I am listening")
    with speech_recognition.Microphone() as s:
             audio = a.record(s,recordtime)
             source = a.recognize_google (audio)
             voic = str(source)
             sound = voic.lower()
             print(sound)
    return sound
        
def bol(v):
    sd = str(v)
    engine.say(sd)
    engine.runAndWait()
    
def algo(voice:str):
     global s
     s = 0
     try :
         if  voice=="top program" or voice=="stop program":
             s = 1
         elif voice in answer.keys() :
             bol(answer[str(voice)])
         else :
             bol("Not Matched with any command")
             bol("Can you please say again")
             if s== 0:
                 algo(say())

     except Exception as e :
         print(e)
         bol("Some Error Occured")
     finally :
         if s==0 : 
            algo(say())
         if s ==1 :
             print("Program Stopped")        

if s == 0:
    algo(say())