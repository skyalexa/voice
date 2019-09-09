import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser
import os
import random
import smtplib
import sys
import wikipedia
import wolframalpha
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
import pyowm
from selenium import webdriver
from selenium.webdriver.common.keys import Keys



engine = pyttsx3.init('sapi5')

rate = engine.getProperty('rate')

voices = engine.getProperty('voices')


engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0')
engine.setProperty('rate', 160)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

gr1=['I am Star....I am your Personal Assistant......what can I do for you','I am Star....I am your Personal Assistant......How may i help you']
def greet():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning")
        speak(random.choice(gr1))

    elif hour >= 12 and hour < 18:
        speak("good afetrnoon sir")
        speak(random.choice(gr1))


    else:
        speak("Good Evening")
        speak(random.choice(gr1))

greet()

rep1 =['Sure','opening youtube','The website you have requested has been opened for you']
rep2 =['Sure','opening google','The website you have requested has been opened for you','I got these results for you']
rep3 =['Sure','opening hackerrank','The website you have requested has been opened for you']
rep4 =['Sure','opening devcode','The website you have requested has been opened for you']
rep5 =['Sure','opening flipkart','The website you have requested has been opened for you']
rep6 =['Sure','opening amazon','The website you have requested has been opened for you']
rep7 =['Sure','opening geeksforgeeks','The website you have requested has been opened for you']
rep8 =['Sure','opening myntra','The website you have requested has been opened for you']
rep9 =['Sure','opening tutorialspoint','The website you have requested has been opened for you']
rep10 =['Sure','opening hackerearth','The website you have requested has been opened for you']
rep11 =['Sure','opening gmail','The website you have requested has been opened for you']
rep12 =['Sure','opening hotmail','The website you have requested has been opened for you']
rep13 =['Sure','opening facebook','The website you have requested has been opened for you']
rep14 =['Sure','opening instagram','The website you have requested has been opened for you']



def takeCommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        pass
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing.....")
        query = r.recognize_google(audio, language='en-in')
        print("user said", query)


    except Exception as e:
        rep_e=['I did not recognize you','say that again please']
        speak(random.choice(rep_e))

        return "None"
    return query



# Function for sending mail

def sendEmail(to, content):
	server = smtplib.SMTP('smtp.gmail.com',587)
	server.ehlo()
	server.starttls()
	server.login('akash30.155@gmail.com', 'r1543210')
	server.sendmail('akash30.155@gmail.com',to,content)
	server.close()




# Main Function to take commands
 
if __name__ == "__main__":


    welcome = ["Hello!...Sir...I am Star...I am your Personal Assistant....How can I help you!","Hi.....I am your personal assistant.....How may i help you","Hey!....i hope you are doing well....how may i help you"]
    speak(random.choice(welcome))
    
    while True:
        query = takeCommand().lower()


        if 'hey star' in query or 'hi star' in query or 'hello star' in query:

            stReply1 = ['hello sir', 'hey I am here', 'Hi whats going on','hey ! what can i do for you','Hi! i was just thinking...it\'s a great time to make cookies...i can help by setting timers if you\'d like']
            speak(random.choice(stReply1))
        elif 'search' in query:

            app_id="52VE7W-E23KYG2LPL"
            client=wolframalpha.Client(app_id)
            query=query.replace("Queestion:"," ")
            res = client.query(query)
            answer = next(res.results)
            speak(answer)
		
        elif 'what are you doing' in query or 'what are you doing now' in query:
            setReply2 = ["I will probably play some music.......if you want to play just say.....Play music ",
                         "there so much to do today....i spend some of the time reading poetry", "nothing",
                         "i am pretty much learning new things...want to hear an interesting fact",
                         "I plan on waiting here quietly until someone asks me a question"]
            speak(random.choice(setReply2))

        elif 'who are you' in query or 'who is star assistant' in query:
            setReply3 = ["I am your Personal assistant.....Searching is special to me....even i can find Don also....This  is also possible for me",
                         "I am your star assistant...I can help with alarms, reminders and timers....or i can help you search for something online",
                         "I am your Star Assistant","Here are somethings you can do when you are online......like send mail....search new things....play msusic"]
            speak(random.choice(setReply3))

        elif 'who created you' in query or 'creator of star assistant' in query or 'who\'s your father' in query:
            setReply4 = ["I was made by Sky","Mr. akash is like my friend...he mean a lot to me",
                          "At first i was just an idea at his mind but he did so much work hard.....And now I am here",
                          "I am the inspiration by someonene else.....which comes into reality"]
            speak(random.choice(setReply4))


        elif 'thankyou' in query:
            setReply6 = ["you\'re Welcome", "i\'m here to help", "happy to help", "don\'t worry about it"]
            speak(random.choice(setReply6)				                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                # For fun
            

        elif 'do you like ice cream' in query:
            setReply15 = ['i\'ve heard ice cream is delicious...but i wouldn\'t know personally....because i\'m lack taste intolerant','ice cream is pretty cool']
            speak(random.choice(setReply15))

        elif 'do you like me' in query or 'do you love me' in query:
            setReply16 = ['Yes! a thousand times Yes', 'of course..you\'re one of my kind', 'there\'s only one name on my list of favourite people...and guess what?...Its Yours', 'of course...you are one in a billion']
            speak(random.choice(setReply16))


        elif 'do you want to marry me' in query:
            speak('I\'m not sure..marriage is the right step for our relationship...but i\'d love to be your assistant forever')


        elif 'tell me a joke' in query or 'please tell me a joke' in query:
            setReply17 = ['what\'s the computer favourite beat....guess what?...An Algo rhytm','what do you get when you put a vest on an alligator?....its an alligator']
            speak(random.choice(setReply17))
            speak("but if you want some...just open google")







#Opening Websites

        elif 'wikipedia' in query:
            speak('Searching.....')
            query = query.replace('wikipedia', "")
            results = wikipedia.summary(query, sentences=4)
            speak('According to Wikipedia')
            speak(results)

        elif 'open youtube' in query:
            speak(random.choice(rep1))
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak("what do you want to search...")
            search = input("Please type:")
            speak("I got the results for you")
            webbrowser.open_new('www.google.com/search?q=' + search)
            speak(random.choice(rep2))
            webbrowser.open("google.com")

        elif 'open hackerrank' in query:
            speak(random.choice(rep3))
            webbrowser.open("hackerrank.com")

        elif 'open devcode' in query:
            speak(random.choice(rep4))
            webbrowser.open("devkode.in")

        elif 'open flipkart' in query:
            speak(random.choice(rep5))
            webbrowser.open("flipkart.com")
         
        elif 'open amazon' in query:
            speak(random.choice(rep6))
            webbrowser.open("amazon.in")

        elif 'open geeksforgeeks' in query:
            speak(random.choice(rep7))
            webbrowser.open("geeksforgeeks.org")

        elif 'open myntra' in query:
            speak(random.choice(rep8))
            webbrowser.open("myntra.com")

        elif 'open tutorialspoint' in query:
            speak(random.choice(rep9))
            webbrowser.open("tutorialspoint.com")

        elif 'open hackerearth' in query:
            speak(random.choice(rep10))
            webbrowser.open("hackerearth.com")

        elif 'open gmail' in query:
            speak(random.choice(rep11))
            webbrowser.open("gmail.com")

        elif 'open hotmail' in query:
            speak(random.choice(rep12))
            webbrowser.open("hotmail.com")

        elif 'open facebook' in query:
            speak(random.choice(rep13))
            webbrowser.open("facebook.com")

        elif 'open instagram' in query:
            speak(random.choice(rep14))
            webbrowser.open("instagram.com")

#For Playing Music

        elif 'play music' in query:
            songs_directory = 'F:\\Songs'
            songs = os.listdir(songs_directory)
            print(songs)
            reply = ['Sure Sir', 'here we go', 'lets rock the floor', 'ofcourse which type of song do you want']
            speak(random.choice(reply))
            os.startfile(os.path.join(songs_directory, random.choice(songs)))

# For time


        elif 'what is the time' in query or 'tell me the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak("the time is " + strTime)


#Open Application

        elif 'visual studio code' in query:
            path_vc = "C:\\Users\\lenovo\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            speak("opening visual studio code")
            os.startfile(path_vc)


        elif 'pycharm' in query:
            path_pc = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2019.1.3\\bin\pycharm64.exe"
            speak("opening pycharm")
            os.startfile(path_pc)
	

        elif 'command prompt' in query:
            path_cp = "%windir%\\system32\\cmd.exe"
            speak("opening command prompt")
            os.startfile(path_cp)


        elif 'google chrome' in query:
            path_gc = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            speak("opening chrome")
            os.startfile(path_gc)


        elif 'notepad' in query:
            path_np = "%windir%\\system32\\notepad.exe"
            speak("notepad")
            os.startfile(path_np)


        elif 'mozilla firefox' in query:
            path_mf = "C:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe"
            os.startfile(path_mf)


        elif 'paint' in query:
            path_p = "%windir%\\system32\\mspaint.exe"
            os.startfile(path_p)


        elif 'internet explorer' in query:
            path_ie = "C:\Program Files\internet explorer\iexplore.exe"
            os.startfile(path_ie)



# Sending mail


        elif 'send mail' in query or 'send email' in query:         
            try:
                speak("what should i say")
                content = takeCommand()
                speak("who is the recipient?.....please enter the mail id")
                to = input()
                sendEmail(to,content)
                speak("email has been sent successfully.")
            except Exception as e:
                print(e)
                speak("Sorry.....I am not able to send this mail")



# For news

        elif 'news for today' in query:
            try:
                news_url="https://news.google.com/news/rss"
                Client=urlopen(news_url)
                xml_page=Client.read()
                Client.close()
                soup_page=soup(xml_page,"xml")
                news_list=soup_page.findAll("item")
                for news in news_list[:16]:
                        speak(news.title.text.encode('utf-8'))
            except Exception as e:
                print(e)

        
        elif 'tell me the weather' in query or 'what about the weather' in  query:
           owm = pyowm.OWM('20e5b9d27a21f98943ba2cc7fcee3b2e')
           observation = owm.weather_at_place('Kanpur, IN')
           observation_list = owm.weather_around_coords(12.972442, 77.580643)
           w = observation.get_weather()
           w.get_wind()
           w.get_humidity()
           w.get_temperature('celsius')
           print(w)
           print(w.get_wind())
           print(w.get_humidity())
           print(w.get_temperature('celsius'))
           speak(w.get_wind())
           speak('humidity')
           speak(w.get_humidity())
           speak('temperature')
           speak(w.get_temperature('celsius'))
          

#for playing online music
        elif 'online songs' in query:
            speak("which type of songs do you want")
            search = input("Please type:")
            speak("I got the results for you")
            webbrowser.open_new('www.soundcloud.com/search?q=' + search)
            



        elif 'shutdown' in query or 'shut up' in query or 'go away star' in query or 'chup raho' in query:
           rep_exit = ['Bye ! have a good  day', 'saayo naara', 'Ok..as you wish', 'dont say it....i dont want to go']
           speak(random.choice(rep_exit))
           sys.exit()
        