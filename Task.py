#Function
import datetime
from urllib import request
from Speak import Say
import wikipedia
import pywhatkit
import requests
import os
import webbrowser as web
import speedtest
from playsound import playsound


import pyfirmata
board = pyfirmata.Arduino('COM5')
board.digital[12].mode = pyfirmata.OUTPUT

#2 Types

#1 - Non Input
#eg: Time , Date , Speedtest


def Time():
    time = datetime.datetime.now().strftime("%H:%M")
    Say(time)

def Date():
    date = datetime.date.today()
    Say(date)

def Day():
    day = datetime.datetime.now().strftime("%A")
    Say(day)

def Location():

    op = "https://www.google.com/maps/place/U.+V.+Patel+College+of+Engineering+(Main+Building)/@23.5305128,72.448513,4625m/data=!3m1!1e3!4m13!1m7!3m6!1s0x390cfd5b347eb62d:0x37205b715389640!2sDelhi!3b1!8m2!3d28.7040592!4d77.1024902!3m4!1s0x395c476dcc7fad61:0x1cf6e21d7ca9091d!8m2!3d23.5284915!4d72.4585896"

    Say("Checking....")

    web.open(op)
    r = requests.get('https://get.geojs.io/')
    ip_req = requests.get('https://get.geojs.io/v1/ip.json')


    ip_add = ip_req.json()['ip']
    print(ip_add)

    url = 'https://get.geojs.io/v1/ip/geo/' + ip_add + '.json'

    geo_q = requests.get(url)

    geo_d = geo_q.json()

    state = geo_d['city']

    country = geo_d['country']

    Say(f"Sir , You Are Now In {state , country} .")

def SpeedTest():
    Say("Checking Network Speed..")

    speed = speedtest.Speedtest()

    upload = speed.upload()

    correct_Up = int(int(upload)/800000)

    download = speed.download()

    correct_down = int(int(download)/800000)

    Say(f"Downloading Speed Is {correct_down} M B Per Second .")
    Say(f"Uploading Speed Is {correct_Up} M B Per Second .")


def NonInputExecution(query):

    # query = str(query)

    if "time" in query:
        Time()

    elif "date" in query:
        Date()

    elif "day" in query:
        Day()

    elif "networktest" in query:
        SpeedTest()

    elif "location" in query:
        Location()

    elif "onlight" in query:
        board.digital[12].write(1)
        Say("Light is on")

    elif "offlight" in query:
        board.digital[12].write(0)
        Say("Light is off")

#2 - Input
#eg - google search , wikipedia

def InputExecution(tag,query):

    # query = str(query)

    if "wikipedia" in tag:
        name = str(query).replace("who is","").replace("about","").replace("what is","").replace("wikipedia","")
        result = wikipedia.summary(name,sentences=5)
        Say(result)

    elif "google" in tag:
        query = str(query).replace("google","")
        query = query.replace("search","")
        pywhatkit.search(query)

    elif "youtube" in tag:
        query =  str(query).replace("play video on","").replace("youtube search","").replace("show me video","").replace("youtube","")
        result = "https://www.youtube.com/results?search_query=" +query 
        web.open(result)
        Say("This Is What I Found For Your Search .")
        pywhatkit.playonyt(query)
        Say("This May Also Help You Sir .")



