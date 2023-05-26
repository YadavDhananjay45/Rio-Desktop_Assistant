#important library
import pyautogui
import pyttsx3
import speech_recognition as sr
import datetime
import time
import os
import sys
import winsound
import wikipedia
import webbrowser

import pyjokes
import requests
from bs4 import BeautifulSoup
from tkinter import *
from PIL import ImageTk, Image
from twilio.rest import Client


#main window code
root =Tk()
root.geometry("750x800+1+1")

root.maxsize(750,800)
root.minsize(750,800)
icon_img=PhotoImage(file="voice-recorder.png")
root.iconphoto(False,icon_img)
root.title("Rio-Desktop Assistant")
b_image = PhotoImage(file="BG.png")
my_label=Label(root,image=b_image)
my_label.place(x=0,y=0)

launch=PhotoImage(file="images/LAUNCH.png")
end_me=PhotoImage(file="images/end_me.png")
help_btn=PhotoImage(file="images/HELP.png")
voice_btn=PhotoImage(file="images/Voice_btn.png")
search_btn=PhotoImage(file="images/search.png")



#this function is for chatbot replys
def reply():
    import speech_recognition as sr
    import pyttsx3
    import openai
    openai.api_key = "Enter your API-key here:"
    speak("hello sir,tell me what can I do for you")
    from gptbot import my_bot
    my_bot()

#used to call main fucntion
def work():
    wish()
    taskexecution()

#chatbot required material
def chatbot_material():
    #wish()
    reply()  
    # bot.after(3000, bot.destroy)
    

#introduction window code
def help():
    help_window = Toplevel(root)
    help_window.title("Intro window")
    #help_window.geometry("750x800")

    #help_window.maxsize(750, 800)
    #help_window.minsize(750, 800)
    help_window['background'] = "#b0c4de"
    label1=Label(help_window,text="!!!!!Here is complete Intro of our project!!!!!",bg = "#b6d4e7", fg = "black", font=('calibre',10, 'bold'),bd=5)
    label1.pack(fill=BOTH,expand=True,padx=25 , pady=20)
    label2 = Label(help_window, text="Rio is the Application which is made to make some of the \n simple. this Application contains one 'smart me' button \n which is used to start start the application.\n you can find list of command in left side of i button\n the after you will one 'go to google' button \n which takes you to google and shows you results\n and then you will have chatbot button which is made\nfor voice based chatting purpose and its fitness \nrelated chatbot so you can get fitness related answer.\n and the final and most importent button is \n 'end me'. by this you can switch off your application.", bg="#b6d4e7", fg="black",font=('calibre',10, 'normal'),bd=95)
    label2.pack(fill=BOTH, expand=True, padx=25, pady=20)

#all code introduse in this fucntion
def info():
    info_window = Toplevel(root)
    info_window.title("Information About Commands")
    #help_window.geometry("750x800")

    #help_window.maxsize(750, 800)
    #help_window.minsize(750, 800)
    info_window['background'] = "#b0c4de"
    label1=Label(info_window,text="!!!!!Here is complete command list present!!!!!",bg = "#b6d4e7", fg = "black", font=('calibre',10, 'bold'),bd=5)
    label1.pack(fill=BOTH,expand=True,padx=25 , pady=20)
    label2 = Label(info_window, text="open notepad or start notepad: use to open notepad\nclose notepad or turnoff notepad: used to close notepad\nopen chrome or start chrome: used to close chrome\nopen movies for me  or show me some movies : to show movies\nopen youtube or go to youtube: to go google\ntell me about weather or what is weather today: it will fatch you current weather\nopne command prompt or open cmd : used to open cmd\nwhere are we or search location : it will fatch you current location\ntake screenshot or screenshot : used to take screenshot\ntell me a joke : it  will tell you joke\nset alarm : used to set alarm\nopen calculator or do some calculation for me : used to do \nsome calculation eg.456+654,55-876 etc.\nopen bmi or bmi : it will open bmi calculator\ndivide bill or bill split : its used to do bill split\nwikipedia : to use this you have to say your topic\n followed by wikipedia to get voice result.\nshutdown the syetem : it will lead to shotdown\nrestart the system : it will leads to restart the system\ngoodbye : it will end the application", bg="#b6d4e7", fg="black",font=('calibre',10, 'normal'),bd=95,justify="left")
    label2.pack(fill=BOTH, expand=True, padx=25, pady=20)

#all buttons
btn1 =Button(root, image=launch,command = lambda:work(),background="#050541",bd=0,activebackground="#050541")
btn1.place(x=290,y=520)

start_info = PhotoImage(file="images/HELP2.png")
img = Button(root,image=start_info,borderwidth=0 ,command=lambda :info(),activebackground="#050541",background="#050541",bd=0)
img.place(x=650,y=90)

btn2 = Button(root,image=end_me, command = lambda :sys.exit(),background="#050541",activebackground="#050541",bd=0)
btn2.place(x=520,y=665)

btn3 = Button(root, image=help_btn, command = lambda :help(),background="#050541",bd=0,activebackground="#050541")
btn3.place(x=285,y=660)

btn4 = Button(root,image=search_btn, command = lambda :Search(),background="#050541",bd=0,activebackground="#050541")
btn4.place(x=285,y=580)

btn10 = Button(root,image=voice_btn, command = lambda:chatbot_material(),background="#050541",bd=0,activebackground="#050541")
btn10.place(x=50,y=660)

output = Text(root, height=1,width=14,bg="light cyan")
output.place(x=321,y=588)

#setting up voice
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice', voices[0].id)

#use to speak out sentance
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

#use to take command
def  takecommand():
    try:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("listening...")
            r.energy_threshold=10000
            r.pause_threshold = 1
            audio = r.listen(source,timeout=5,phrase_time_limit=8)
    except KeyboardInterrupt:
        taskexecution()
    except sr.WaitTimeoutError as k:
        print("time out")

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")

    except Exception as e:
        speak("sorry for the glitch,please try again")
        return "none"
    except sr.WaitTimeoutError as k:
        print("time out")
    query=query.lower()
    return query

def prin():
    output.insert(END, "Showing Result...")

#used to search command on google
def Search():
    output.delete("1.0", "end")
    prin()
    speak("Tell me what should i search on google")
    search = takecommand()
    webbrowser.open(f"{search}")


#this fuction is used to calculate bmi
def calculate_bmi():
    try:
        speak("can you please tell me your weight in kilograms.")
        weight = takecommand()
        kg = int(weight)
        speak("can you please tell me you height in meters")
        meter = takecommand()
        m = int(meter) / 100
        bmi = kg / (m * m)
        bmi = round(bmi, 1)
        bmi_index(bmi)
    except TimeoutError:
        calculate_bmi()

#this fucntion is for to show output of bmi
def bmi_index(bmi):
    if bmi < 18.5:
        speak(f"{bmi} is Underweight")
    elif (bmi > 18.5) and (bmi < 24.9):
        speak(f"{bmi} is Normal")
    elif (bmi > 24.9) and (bmi < 29.9):
        speak(f"{bmi} is Overweight")
    elif (bmi > 29.9):
        speak(f"{bmi} is Obesity")

#this fucntion is for do bills splits
def bill_split():
    try:
        speak("Tell me how many number of people you are ")
        people = takecommand()
        p1 = int(people)
        speak("tell me the amount of bill")
    except Exception as e:
        print(e)
        speak("sorry sir, i didn't get it , can you repeat again")
        bill_split()
    try:
        amount = takecommand()
        amt = int(amount)
    except Exception as e:
        print(e)
        speak("sorry sir, i didn't get it , can you repeat again")
        bill_split()
    value = amt / p1
    value_1 = round(value,2)
    speak(f"so for each person you have to pay {value_1}")
    if people=="godbye" or "bye" or "close":
        sys.exit()

#this is for to convert calsius to fahrenheit
def caltofah():
    speak("tell me your celsius value")
    cel1 = takecommand()
    fah1 = (cel1 * 1.8) + 32
    result1 = round(fah1,2)
    speak(f"your answer in fahrenheit is {result1}")
    return result1

#this is for to convert fahrenheit to calsius
def fahtocal():
    speak("tell me your Fahrenheit value")
    fah1 = takecommand()
    cal1 = (fah1 - 32) / 1.8
    result1 = round(cal1,2)
    speak(f"your answer in calsius is {result1}")

#this is for with fucntion
def wish():
    hour = int(datetime.datetime.now().hour)
    tt = time.strftime("%I:%M %p")

    if hour >= 0 and hour < 12:
        speak(f"good morning, its {tt}")
    elif hour >= 12 and hour < 16:
        speak(f"good afternoon, its {tt}")
    else:
        speak(f"good evening, its {tt}")
    speak("Please tell me, How can i help you")

#this is for setting up alarm
def alarm(Timing):
    try:
        altime = str(datetime.datetime.now().strptime(Timing,"%H:%M %p"))

        altime = altime[11:-3]
        print(altime)
        horeal = altime[:2]
        horeal = int(horeal)
        mireal = altime[3:5]
        mireal = int(mireal)
        print(f"done, alarm is set for {Timing}")

        while True:
            if horeal==datetime.datetime.now().hour:
                if mireal==datetime.datetime.now().minute:
                    print("alarm is running")
                    winsound.PlaySound("abc",winsound.SND_LOOP)
                    #Winsound.Beep(1, 10)

                elif mireal<datetime.datetime.now().minute:
                    break

    except Exception as e:
        speak("Try again")


#this will fatch weather
def weather():
    search = "temparature in mumbai"
    url = f"https://www.google.com/search?q={search}"
    r = requests.get(url)
    data = BeautifulSoup(r.text, "html.parser")
    temp = data.find("div", class_="BNeawe").text
    speak(f"current {search} is {temp}")


def terminate(ProcessName):
    os.system('taskkill /IM "' + ProcessName + '" /F')

#this is main fucntion which contain most of the features
def taskexecution():
    #wish()

    query = takecommand()
    if "open notepad" in query or "start notepad" in query:
        npath = "C:\\Windows\\system32\\notepad.exe"
        os.startfile(npath)

    elif "close notepad" in query or "trun off notepad" in query:
        speak("okay sir, closing notepad")
        os.system("taskkill /f /im notepad.exe")

    elif "open word" in query or "start word" in query:
        npath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\word"
        os.startfile(npath)

    elif "open chrome" in query or "start chrome" in query:
        npath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\google chrome"
        os.startfile(npath)


    elif "open movies for me" in query or "show me some movies" in query:
        npath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Popcorn Time\\popcorn time"
        os.startfile(npath)

    elif "open command prompt" in query or "open cmd" in query or "go to cmd" in query or "go to command prompt" in query or "command" in query:
        os.system("start cmd")

    elif "open youtube" in query or "youtube" in query or "start youtube" in query:
        webbrowser.open("www.youtube.com")
    
    elif "play" in query or "start the video" in query:
        pyautogui.press("k")

    elif "pause" in query or "pause the video" in query:
        pyautogui.press("k")

    elif "mute" in query:
        pyautogui.press("m")

    elif "volume up" in query or "increase the volume" in query:
        from keyboard import volumeUp
        volumeUp()

    elif "volume down" in query or "decrease the volume" in query:
        from keyboard import volumeDown
        volumeDown()

    elif "open whatsapp" in query or "whatsapp" in query or "start whatsapp" in query:
        webbrowser.open("https://web.whatsapp.com/")

    elif "tell me about weather" in query or "what's  weather" in query or "what is weather today" in query:
        weather()

    elif "show me chart" in query or "chart" in query:
        import yfinance as yf
        import matplotlib.pyplot as plt
        from stock import stockChart
        stockChart()

    elif "open google" in query or "go to google" in query or "start google" in query:
        speak("sir, what do you want me to search on google")
        search = takecommand().lower()
        webbrowser.open(f"{search}")

    elif "wikipedia" in query:
        speak("searching on wikipedia....")
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        speak("according to wikipedia")
        speak(results)
        print(results)

    elif "where are we" in query or "where we are" in query or "search location" in query:
        speak("wait sir , let me check")
        try:
            r = requests.get('https://get.geojs.io/')

            ip_requests = requests.get('https://get.geojs.io/v1/ip.json')
            ipAdd = ip_requests.json()['ip']
            print(ipAdd)

            url = 'https://get.geojs.io/v1/ip/geo/' + ipAdd + '.json'
            geo_request = requests.get(url)
            geo_data = geo_request.json()

            # print(geo_data['city'])
            # print(geo_data['region'])
            # print(geo_data['country'])

            city = geo_data['city']
            state = geo_data['region']
            country = geo_data['country']
            speak(f"sir we are in mumbai city of maharashtra which is in {country} country")
        except Exception as e:
            speak("sorry sir ,not able to find the location")
            pass
        except KeyboardInterrupt as e:
            pass


    elif "take screenshot" in query or "screenshot" in query:
        speak("sir,please tell me the name for screenshot file")
        name = takecommand().lower()
        speak('please hold the screen for few seconds, i am taking screenshot')
        time.sleep(3)
        img = pyautogui.screenshot()
        img.save(f'{name}.png')
        speak('i am done with the screenshot,you ready for the next commands')


    elif "open calculator" in query or "do calculation for me" in query:
        from calc import buildCalc
        buildCalc()
      
    elif "bmi" in query or "open bmi calculator" in query or "open bmi" in query:
        calculate_bmi()

    elif "convert Celsius to Fahrenheit" in query:
        caltofah()


    elif "split the bill" in query:
        bill_split()

    elif "joke" in query :
        joke = pyjokes.get_joke(language="en", category="neutral")
        speak(joke)

    elif "set alarm" in query:
        try:
            speak("sir, please tell me time to set alarm")
            tt = takecommand()
            # tt = tt.replace("set alarm to","")
            tt = tt.replace(".", "")
            tt = tt.upper()
            alarm(tt)
        except KeyboardInterrupt:
            pass

    elif "open" in query:
        query=query.replace("open","")
        query=query.replace("rio","")
        pyautogui.press("super")
        pyautogui.typewrite(query)
        pyautogui.sleep(2)
        pyautogui.press("enter")

    elif "send messgae" in query or "send a message" in query:
        account_sid="Enter your twilio account_sid here"
        auth_token="Enter your twilio Token here:"
        client=Client(account_sid,auth_token)

        speak("what should i send")
        msz=takecommand()
        message=client.messages.create(
            body=msz,
            from_="Enter you Twilio number",
            to="Enter receivers contact number"
            # contact number should be verified on twilio's website
        )

        print(message.sid)
        speak("message sent successfully")



    elif "shutdown the system" in query:
        os.system("shutdown /s /t 5")

    elif "restart the system" in query:
        os.system("shutdown /r /t 5")

    elif "activate sleep mode" in query:
        os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")


    elif "goodbye" in query or "bye" in query:
        speak("thanks for using me, have a good day ahead")
        sys.exit()
    
root.after(3000,root.destroy)

root.mainloop()

if __name__ == '__main__':
    while True:
       taskexecution()