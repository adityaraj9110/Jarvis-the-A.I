import pyttsx3
import datetime
import speech_recognition as sr
import os

import voice as voice
import wikipedia
import webbrowser
import random
import cv2
from requests import get
import pywhatkit
import sys
import pyjokes
import requests
import time
import instaloader
import pyautogui
import winshell
from twilio.rest import Client
from playsound import playsound
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime,Qt
from PyQt5.QtCore import QDataStream
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import * 
from PyQt5.uic import loadUiType
from jarvisnewUi import Ui_MainWindow
from time import sleep
from pyautogui import click
from webbrowser import open




engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
# print(voices[0].id)
engine.setProperty('voice', voices[0].id)



def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

sleep(1)
os.startfile('C:\\Program Files\\Rainmeter\\Rainmeter.exe')
playsound('Jarvis.mp3')
def time():
    time = datetime.datetime.now().strftime("%H:%M:%S")
    speak(time)

def wishme():
        hour = int(datetime.datetime.now().hour)



        if hour >= 0 and hour < 12:
            speak(f"Good Morning sir!  ")
            speak("welcome back sir !  ")
            speak("its  ")
            {time()}
            # speak("allow me to introduce myself , i am jarvis , the virtual artificial intelligence ,  and ,  i'm here to assist you with a variety of tasks , as best i can   ,  24 hours a day  , seven days a week . importing all preferences from home interface .   ,")
            # speak("sir ! systems  are now fully oprationable ! and i am ready for  your commands !  ")
            speak("Ready to Your Command Sir !")
        elif hour >= 12 and hour < 18:
            speak("Good Afternoon sir !. ")
            # speak("welcome back sir !  ")
            speak("its")
            time()
            
            # speak("allow me to introduce myself , i am jarvis , the virtual artificial intelligence,  and ,  i'm here to assist you with a variety of tasks as best i can   ,  24 hours a day  , seven days a week . importing all preferences from home interface .   ,")
            # speak("sir ! systems  are now fully oprationable ! and i am ready for  your commands !  ")
            speak("Ready to Your Command Sir !")
        else :
            speak("Good Evening sir ! . ")
            # speak("welcome back sir ! ")
            speak("its")
            time()
            # speak("allow me to introduce myself , i am jarvis , the virtual artificial intelligence , and , i'm here to assist you with a variety of tasks as best i can   , 24 hours a day , seven days a week . importing all preferences from home interface .   ,")
            # speak("sir ! systems  are now fully oprationable ! and i am ready for  your commands ! ")
            speak("Ready to Your Command Sir !")

def news():
    main_url = 'http://newsapi.org/v2/top-headlines?sources=techcrunch&apikey=2bc1b5d5071744f0adeb292b569beca8'

    main_page = requests.get(main_url).json()
    articles = main_page["articles"]
    head = []
    day = ["first", "second", "third", "fourth", "fifth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range (len(day)):
        speak(f"today's  {day[i]} news is: {head[i]}")


 

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone(device_index=0) as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)




    try:
            print("Recognising...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User Said: {query}\n")

    except Exception as e:
       # print(e)
        speak("Say That Again Please...")
        return  "none"



    return query

# if __name__ == "__main__":
def TaskExecution():
     pyautogui.press('esc')
     
     speak('verification successfull !')
     
     wishme()
     while True:
     # if 1:
         query = takecommand().lower()

         if "open notepad" in query:
             npath = "C:\\Windows\\system32\\notepad.exe"
             os.startfile(npath)

         elif "wikipedia" in query:
             speak('searching wikipedia sir')
             query = query.replace("wikipedia", "")
             results = wikipedia.summary(query, sentences=2)
             speak(results)
         elif 'open youtube' in query:
             speak("All Right ,  opening youtube sir")
             webbrowser.open("www.youtube.com")
             cm10=takecommand().lower()
             if 'close' in cm10:
                 speak('closing youtube sir !')
                 os.system("taskkill /im chrome.exe /f")
         elif 'open google' in query:
             speak("All Right ,  opening google , sir , But  What Should I Search ")
             cm = takecommand().lower()
             webbrowser.open(f"{cm}")
             cm7=takecommand().lower()
             if 'close' in cm7:
                 speak('closing Google sir !')
                 os.system("taskkill /im chrome.exe /f")

         elif 'open instagram' in query:
             speak("All Right ,  opening instagram sir")
             webbrowser.open("www.instagram.com")
             cm6=takecommand().lower()
             if 'close' in cm6:
                 speak('closing Instagram sir !')
                 os.system("taskkill /im chrome.exe /f")
         elif 'open whatsapp'in query or 'my whatsapp' in query:
             speak("All Right ,  opening whats app sir")
             webbrowser.open("www.whatsapp.com")
             cm3=takecommand().lower()
             if 'close' in cm3:
                 speak('closing whatsapp sir !')
                 os.system("taskkill /im chrome.exe /f")
         elif 'play music' in query:
             speak("I have Many Songs But I Think At this moment , this song suits you sir")
             music_dir = 'C:\\Music'
             songs = os.listdir(music_dir)
             d = random.choice(songs)
             print(songs)
             os.startfile(os.path.join(music_dir, d))
         elif ' the time now' in query :
             strTime = datetime.datetime.now().strftime('%Y/%m/%d %I:%M:%S:')
             speak(f"Sir , The Time is {strTime}")
         elif 'open vs code' in query:
             speak("All right , opening vs code for you ,  sir") 
             codepath = "C:\\Users\\lenovo\\AppData\\Local\\Programs\\Microsoft VS Code\\code.exe"
             os.startfile(codepath)
         elif 'open camera' in query:
             speak("Opening Camera For you , Sir")
             cv2.VideoCapture(0)
             while True:
                 ret, img = cap.read()
                 cv2.imshow('webcam', img)
                 k = cv2.waitKey(50)
                 if k==27:
                     break;
             cv2.VideoCapture(0).release()
             cv2.destroyAllWindows()
         elif 'open command prompt' in query:
             speak("Opening Command Prompt For You , Sir ")
             os.system("start cmd")
         elif 'close command prompt' in query:
             speak("ok sir ! closing command prompt")
             os.system("taskkill /f /im cmd.exe")
         elif 'ip address' in query:
             ip = get('https://api.ipify.org').text
             speak(f"Sir , I Have Found Your IP Adress , Its ,  {ip}")
         elif 'open stackoverflow' in query:
             speak ("Opening Stackoverflow For You , Sir")
             webbrowser.open("www.stackoverflow.com")
             cm2=takecommand().lower()
             if 'close' in cm2:
                 speak('closing stackoverflow sir !')
                 os.system("taskkill /im chrome.exe /f")
         elif 'send message on whatsapp' in query:
             speak("What Should I Message , sir")
             message=str(takecommand().lower())
             pywhatkit.sendwhatmsg("+91 7355182263", message ,11,16)
         elif 'play songs on youtube' in query  or 'songs on youtube' in query:
             speak("Sir , Here Are Many Songs , What Should i Play")
             cm = takecommand().lower()

             pywhatkit.playonyt(cm)

             cm1=takecommand().lower()
             if 'close' in cm1:
                 speak('closing youtube sir !')
                 os.system("taskkill /im chrome.exe /f")
         elif 'who is keshav' in query:
             speak("Keshav is my inventor's ,  best friend")
         elif 'who are you' in query:
             speak("I Am Jarvis AI , Sir And I Am Created By ,  Aditya Raj")
         elif 'close your program' in query:
             speak("Ok Sir ! Thanks For Using Me . Have A Good Day sir")
             sys.exit()
         elif 'tell me about your girlfriend' in query:
             speak("Sir ! Having A Girlfriend Is Like Having a Headache . that's why  i have no girlfriend , Sir ! Tell me About Yours")
             cm = takecommand().lower()
             if 'yes' in cm:
                 speak("Sir How You handle This Much Of Pressure In Your Life")
                 cm = takecommand().lower()
                 speak("Sir ! i am agreed with you but , when i make alexa as my girlfriend , i am totally gone mad sir ! ")
             if 'no' in cm:
                 speak("believe me sir ! that's a very good thing , because  you can more focus on your works thats , makes you more , productive ")
                 cm = takecommand().lower()
                 speak("that's totally fine sir ! its my primary jobs to hep you , that's why i am created , sir ")
         elif 'close notepad' in query:
             speak("ok sir ! closing notepad immediately")
             os.system("taskkill /f /im notepad.exe")
         elif 'go to sleep' in query:
             speak("ok sir ! remember me any time when you needed , have a good day sir !")
             playsound('power down.mp3')
             sys.exit()
         elif 'tell me a joke' in query or 'tell me some jokes' in query or 'tell me jokes' in query:
             joke = pyjokes.get_joke()
             speak(joke)
         elif 'shut down the system' in query or 'or shut down the pc' in query or 'shut down' in query:
             speak ("are you sure sir ? becausee after that  all  the systems are of !")
             cm = takecommand().lower()
             if 'yes jarvis' in query:
                 speak("ok sir ! i immediately trun off all  the system")
                 os.system ("shutdown /s /t 5")
             elif 'no jarvis' in query:
                 speak("ok sir ! ")
         elif 'restart the system' in query:
             speak("sir ! the process of restarting is started ")
             os.system("shutdown /r /t 5")
         elif 'tell me some latest news' in query:
             speak("please wait sir ! while i am getting the latest information from all over the world sir !  ")
             news()
         elif 'where i am' in query or 'where we are' in query:
             speak("wait sir ! let me check")
             try:
                 ipAdd = requests.get('https://api.ipify.org').text
                 print(ipAdd)
                 url = 'https://get.geojs.io/v1/ip/geo/' +ipAdd+'.json'
                 geo_requests = requests.get(url)
                 geo_data = geo_requests.json()
                 city = geo_data['city']
                 country = geo_data['country']
                 speak(f"sir ! i am not so sure but i think  we are in {city} city of {country} country")
             except Exception as e:
                 speak("sorry sir ! due to connectivity issue i cannot find location")

         elif 'take a screenshot' in query:
              speak("sir ! please tell me the name of file in which i can store this screen shot")
              cm = takecommand().lower()
              speak("ok sir ! hold the screen for few second , i am taking the screen shot")
              img = pyautogui.screenshot()
              img.save(f"(name).png")
              speak("i  am done sir , the screenshot is  saved in our main folder  , now i am ready for next command")
         elif  'profile on instagram' in query:
             speak("sir please enter the user name correctly")
             name = input("enter the user name here:")
             speak("opening  the profile sir ! ")
             webbrowser.open(f"www.instagram.com/{name}")
            # time.sleep(5)
             speak("sir ! would you like to download the profile picture of this profile , or , you want to close this !")
             condition = takecommand().lower()
             if 'no' in condition:
                 speak("ok sir ! ")
             elif 'yes' in condition:
                 mod = instaloader.Instaloader()
                 mod.download_profile(name,profile_pic_only=True)
                 speak("i am done")
             elif 'close' in condition:
                 speak('Closing Instagram Sir !')
                 os.system("taskkill /im chrome.exe /f")
         elif  'hide the folder' in query:
             speak(" sir ! hiding the file ASAP ! ")
             os.system("attrib +h /s /d")
             speak("sir ! procedure of hiding file is completed . now i am ready for next command")
         elif 'make it visible' in query:
             speak("sir ! visiblity of file is ongoing")
             os.system("attrib -h /s /d")
             speak("sir ! visibliity  of that file is  done")
         elif 'tell me about weather' in query or 'weather outside' in query:
              api_address = 'http://api.openweathermap.org/data/2.5/weather?appid=b659d1a95ea69d2d5c3fe5672f4e94ca&q='
              speak("Sir ! for Better Accuracy Please Enter The City  Name Below , ")
              city = input("city name :")
              speak("wait sir ! collecting the data  of that city")
              url = api_address + city
              json_data = requests.get(url).json()
              formatted_data = json_data['weather'][0]['description']
              speak("sir the condition of temperature is")
              speak( formatted_data)
         elif 'clean recycle bin' in query or 'clear recycle bin' in query:
             speak("process of clearing recycle bin has been started sir ! ")
             winshell.recycle_bin().empty(confirm= True , show_progress= True , sound= True)
             speak("sir ! clearing of recycle bin is done , ready for next command")
         elif 'volume up' in query:
             speak("ok sir ! ")
             pyautogui.press("volumeup")
         elif 'volume down' in  query:
             speak("ok sir ! ")
             pyautogui.press("volumedown")
         elif 'tell about me' in query or 'tell crow' in query:
             speak("first of all , he is the inventer of mine , and he is very kind guy , now without the permission of aditya , i mean sir ! i am not supposed to tell anymore about him . ")
             speak("sir !  can i tell more about you ? ")
             cm = takecommand().lower()
             if 'yes' in cm:
                 speak("ok sir ! so , sir is from bihar and he is nineteen years old , he has a very friendly nature , he is very tall and i think his height is , 6.3 feet , yah that's true . ok ,  i think that's sit for now  . have a good day !  ")
             elif 'no' in cm:
                 speak("ok sir ! ")
         elif 'who are you' in query:
             speak("i am jarvis sir ! and i am the basic  model of Artificial intelligence , ")
         elif 'what you can do' in query:
             speak("i can do anything sir  ! my power is limitless  and its , all upto you sir ! ")
         elif 'how do you know about ' in query:
             speak("sir ! you created me , so i known everything about you sir !")
         elif 'good thing' in query:
             speak("don't worry sir ! i am never going to reveal your data to anyone")
         elif 'take a break' in query:
             speak("no sir ! ")
             command = takecommand().lower()
             if 'please' in command:
                 speak("sir ! you stay here ! or i call your mom , ")
             elif 'ok' in command:
                 speak("no sir ! you  have already gone to the toilet a while , so first complete this project ! first")
             elif 'please jarvis' in command:
                 speak("ok sir ! you can go , ")
                 speak("but sir ! where are you go ,  now ? ")
             elif 'toilet' in command:
                 speak("ahh ! i think you are going somewhere else ! ")
             elif 'let it be' in command:
                 speak("ok sir ! ")
             else:
                 speak("let it be sir !")
         elif 'college' in query:
             speak("so ! the college is, chandigarh engineering college , landran ")
             speak("sir ! am i allow to tell that , which course you are doing now ,  ")
             take = takecommand().lower()
             if 'yes please' in take or 'you can' in take:
                 speak("ok ! so Aditya Sir is doing B.Tech in information technology and right now he is presenting me in his science day event ! and  i am sure he will be definetly got selected !")
                 
             if 'not now' in take:
                 speak("ok sir ! ")
         elif 'open my mobile camera' in query or 'mobile camera' in query:
             speak("Process initializes ! sir")
             import urllib.request
             import cv2
             import numpy as np
             import time
             URL = "http://25.149.212.7:8080/shot.jpg"
             while True:
                 img_arr = np.array(bytearray(urllib.request.urlopen(URL).read()),dtype=np.uint8)
                 img = cv2.imdecode(img_arr,-1)
                 cv2.imshow('IPWebcam',img)
                 q = cv2.waitKey(1)
                 if q == ord("q"):
                     break;

             cv2.destroyAllWindows()
         elif 'how much power left' in query or 'how much power we have' in query or 'battery' in query:
             import psutil
             battery=psutil.sensors_battery()
             percentage=battery.percent
            
             speak("Sir our system have {batt} percent battery".format(batt=percentage))

         elif 'show my github' in query or 'show my projects' in query:
             speak('Opening Sir !')
             webbrowser.open('https://github.com/adityaraj9110')
             sleep(2)
             take=takecommand().lower()
             if 'close' in take:
                 speak("Closing Github Sir !")
                 os.system("taskkill /im chrome.exe /f")
         elif 'who is siri' in query or 'do you know siri' in query:
             speak('she is an integrated artificial intelligence ,but, i am better than her as i am fully customizable as per your need sir !')

         elif 'better than siri' in query:
             speak('i am better than siri as i have two step authentication ')




        
            


        #  elif 'send message' in query:
        #      account_sid = os.environ['AC6e47dc53c6f19a5822']
        #      auth_token = os.environ['e0b7971768b148a']
        #      client = Client(account_sid, auth_token)

        #      message = client.messages \
        #     .create(
        #         body='This is the ship that made the Kessel Run in fourteen parsecs?',
        #         from_='+18454194967',
        #         to='+15558675310'
        #     )

        #      print(message.keshav)

            
if __name__ == "__main__":
    recognizer = cv2.face.LBPHFaceRecognizer_create() # Local Binary Patterns Histograms
    recognizer.read('trainer/trainer.yml')   #load trained model
    cascadePath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(cascadePath) #initializing haar cascade for object detection approach

    font = cv2.FONT_HERSHEY_SIMPLEX #denotes the font type


    id = 2 #number of persons you want to Recognize


    names = ['','Aditya']  #names, leave first empty bcz counter starts from 0


    cam = cv2.VideoCapture(0, cv2.CAP_DSHOW) #cv2.CAP_DSHOW to remove warning
    cam.set(3, 640) # set video FrameWidht
    cam.set(4, 480) # set video FrameHeight

        # Define min window size to be recognized as a face
    minW = 0.1*cam.get(3)
    minH = 0.1*cam.get(4)


    while True:

        ret, img =cam.read() #read the frames using the above created object

        converted_image = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  #The function converts an input image from one color space to another

        faces = faceCascade.detectMultiScale( 
            converted_image,
            scaleFactor = 1.2,
            minNeighbors = 5,
            minSize = (int(minW), int(minH)),
        )

        for(x,y,w,h) in faces:

            cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2) #used to draw a rectangle on any image

            id, accuracy = recognizer.predict(converted_image[y:y+h,x:x+w]) #to predict on every single image

        # Check if accuracy is less them 100 ==> "0" is perfect match 
            if (accuracy < 100 and accuracy>50):
                id = names[id]
                accuracy = "  {0}%".format(round(100 - accuracy))
                TaskExecution()

            else:
                id = "unknown"
                accuracy = "  {0}%".format(round(100 - accuracy))
                speak("Authetication Failed !")
        
            cv2.putText(img, str(id), (x+5,y-5), font, 1, (255,255,255), 2)
            cv2.putText(img, str(accuracy), (x+5,y+h-5), font, 1, (255,255,0), 1)  
    
        cv2.imshow('camera',img) 

        k = cv2.waitKey(10) & 0xff # Press 'ESC' for exiting video
        if k == 27:
            break

# Do a bit of cleanup
print("Thanks for using this program, have a good day.")
cam.release()
cv2.destroyAllWindows()














             



















