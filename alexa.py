import pyttsx3 # pip install pyttsx3
import datetime
import speech_recognition as sr # pip install SpeechRecognition
import wikipedia # pip install wikipedia
import smtplib
import webbrowser as wb
import os
import pyautogui # pip install pyautogui
import psutil # pip install psutil
import pyjokes
import pywhatkit
import pyowm
import openweather
import operator
from email.message import EmailMessage

engine = pyttsx3.init()
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def talk(text):
    engine.say(text)
    engine.runAndWait()
def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("the current time is")
    speak(Time)

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("the current date is")
    speak(date)
    speak(month)
    speak(year)
def get_operator(self, op):
        return {
            '+': operator.add,
            '-': operator.sub,
            'x': operator.mul,
            'divided': operator.__truediv__,
            'Mod': operator.mod,
            'mod': operator.mod,
            '^': operator.xor,
        }[op]
def do_math(self, li):
        # passes the second item in our list to get the built-in function operand
        op = self.get_operator(li[1])
        # changes the strings in the list to integers
        int1, int2 = int(li[0]), int(li[2])
        # this uses the operand from the get_operator function against the two intengers
        result = op(int1, int2)
        speak(str(int1) + " " + li[1] + " " + str(int2) + " equals " + str(result))
        
def wishme():
    speak("Welcome back sir!")
    time()
    date()
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour<12:
        speak("Good morning sir!")
    elif hour >=12 and hour<18:
        speak("Good afternoon sir")
    elif hour >= 18 and hour<24:
        speak("Good Evening sir")
    else:
        speak("Good night sir")

    speak("Alexa at your service. Please tell me how can i help you?")
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recongnizning...")
        query = r.recognize_google(audio, language='en-in')
        print(query)

    except Exception as e:
        print(e)
        speak("Say that again please...")
        return "None"
    return query

def send_email(receiver, subject, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    # Make sure to give app access in your Google account
    server.login('adithyansalee2003@gmail.com', 'papasgift')
    email = EmailMessage()
    email['From'] = 'adithyansalee2003@gmail.com'
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(message)
    server.send_message(email)


email_list = {
    'Amma': 'jestisalee@gmail.com',
    'Papa': 'saleemanimangalam@gmail.com',
    'Milutty': 'aahanamilu0@gmail.com'
}


def screenshot():
    img = pyautogui.screenshot()
    img.save("C:\\Users\\arbaz\\Desktop\\Open-cv\\jarvis\\ss.png")
def cpu():
    usage = str(psutil.cpu_percent())
    speak('CPU is at'+ usage)
    battery = psutil.sensors_battery()
    speak("Battery is at")
    speak(battery.percent )
def open_things(self, command):
        # Will need to expand on "open" commands
        if command == "open youtube":
            speak("Opening YouTube.")
            wb.open("https://www.youtube.com")
            pass

        elif "open facebook" in query:
            speak("Opening Facebook.")
            wb.open("https://www.facebook.com")
            pass

        elif command == "open my documents":
            speak("Opening My Documents.")
            os.startfile("C:/Users/Notebook/Documents")
            pass

        elif command == "open my downloads folder":
            speak("Opening your downloads folder.")
            os.startfile("C:/Users/Notebook/Downloads")
            pass

        else:
            speak("I don't know how to open that yet.")
            pass

def get_weather(self, command):
        home = 'Kerala, Thiruvananthapuram'
        owm = pyowm.OWM(openweather)
        mgr = owm.weather_manager()

        if "now" in command:
            observation = mgr.weather_at_place(home)
            w = observation.weather
            temp = w.temperature('fahrenheit')
            status = w.detailed_status
            speak("It is currently " + str(int(temp['temp'])) + " degrees and " + status)

        else:
            print("I haven't programmed that yet.")
def jokes():
    speak(pyjokes.get_joke())

if __name__ == "__main__":
	wishme()
while True:
		query = takeCommand().lower()
		if 'time' in query:
			time()
		elif 'date' in query:
			date()
		elif 'play' in query:
                            song = query.replace("play", "")
                            speak('playing ' + song)
                            pywhatkit.playonyt(song)
		elif 'who is' in query:
			speak("Searching...")
			query = query.replace("who is","")
			result = wikipedia.summary(query, sentences=2)
			print(result)
			speak(result)
		elif 'send email' in query:
                    speak('To Whom you want to send email')
                    name = takeCommand()
                    receiver = email_list[name]
                    print(receiver)
                    speak('What is the subject of your email?')
                    subject = takeCommand()
                    speak('Tell me the text in your email')
                    message = takeCommand()
                    send_email(receiver, subject, message)
                    speak('Sir Your email is sent')
                    speak('Do you want to send more email?')
                
		elif 'logout' in query:
			os.system("shutdown -l")

		elif 'shutdown' in query:
			os.system("shutdown /s /t 1")

		elif 'restart' in query:
			os.system("shutdown /r /t 1")
		
		elif 'play songs' in query:
			songs_dir = 'D:\\Music'
			songs = os.listdir(songs_dir)
			os.startfile(os.path.join(songs_dir, songs[0]))

		elif 'remember that' in query:
			speak("What should I remember?")
			data = takeCommand()
			speak("you said me to remember that"+data)
			remember = open('data.txt','w')
			remember.write(data)
			remember.close()
        
		elif 'do you know anything' in query:
			remember =open('data.txt', 'r')
			speak("you said me to remember that" +remember.read())

		elif 'screenshot' in query:
			screenshot()
			speak("Done!")

		elif 'open youtube'in query:
                    speak("Opening Youtube")
                    wb.open("https://www.youtube.com")
		elif 'introduce yourself' in query:
                    speak("I am ALEXA. Your personal assistant.")
		elif 'bye alexa' in query:
			quit()
            
     
        

        