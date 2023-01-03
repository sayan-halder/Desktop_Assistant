import os,sys,datetime,random,smtplib,webbrowser,pyttsx3,wikipedia,wolframalpha,pyaudio
import speech_recognition as sr


engine = pyttsx3.init('sapi5')
client = wolframalpha.Client('L84H3U-P9RW2X4GX9')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    print('\n Bosco: ',audio)
    engine.say(audio)
    engine.runAndWait()


def myCommand():
    r = sr.Recognizer()                                                                                   
    with sr.Microphone() as source:                                                                       
        print("\n Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 5000
        audio = r.listen(source)
    try:
        print("\n Recognizing.....")
        query = r.recognize_google(audio, language='en-in')
        print('\n User: ' + query)
    except:
        speak('Sorry Boss! I didn\'t get that! Try typing the command!')
        query = str(input('\n Command: '))
        print('\n User: ' + query)
    return query


def greetMe():
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        speak('Good Morning Boss!')
    elif currentH >= 12 and currentH < 16:
        speak('Good Afternoon Boss!')
    elif currentH >= 16 and currentH != 0:
        speak('Good Evening Boss!')        
    speak('Hello Boss, I am your digital assistant Bosco')
    speak('How may I help you?')
greetMe()

    
if __name__ == '__main__':
    while True:
        query = myCommand().lower()

        if 'hello' in query:
            speak('Hello Boss!')
            
        elif "what\'s up" in query or 'how are you' in query:
            stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy!']
            speak(random.choice(stMsgs))

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Boss! the time is {strTime}")
            
        elif 'open google' in query:
            speak('Okay Boss!')
            webbrowser.open('www.google.co.in')
        
        elif 'open youtube' in query:
            speak('Okay Boss!')
            webbrowser.open('www.youtube.com')
            
        elif 'news headlines' in query:
            speak('Okay Boss!')
            webbrowser.open('www.news.google.com')

        elif 'open gmail' in query:
            speak('okay boss!')
            webbrowser.open('www.gmail.com')

        elif 'send email' in query:
            speak('Okay Boss!')
            try:
                speak('Who is the recipient?')
                #to = myCommand().lower().replace(' ','')
                to = str(input('\n Recipient: '))
                print('\n The Recipient is: ',to)
                speak("What should I say?")
                #content = myCommand()
                content = str(input('\n Text: '))
                print('\n The Text is: ',content)
                
                speak('sending')
                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.ehlo()
                server.starttls()
                server.login('shda42019@gmail.com', '10ab29cd38ef47gh56ij')
                server.sendmail('shda42019@gmail.com', to, content)
                server.close()
                speak("Email has been sent!")
            except Exception as e:
                speak('Sorry Boss! I am unable to send your message at this moment!')

        elif 'open facebook' in query:
            speak('okay boss!')
            webbrowser.open('www.facebook.com')

        elif 'open instagram' in query or 'open insta' in query:
            speak('Okay Boss!')
            webbrowser.open('www.instagram.com')

        elif 'open twitter' in query :
            speak('Okay Boss!')
            webbrowser.open('www.twitter.com') 

        elif 'play music' in query:
            speak('Okay Boss!')
            webbrowser.open('www.gaana.com')
            speak('Here is your music list! Enjoy!')

        elif 'open access' in query :
            speak('Okay Boss!')
            subprocess.call(r'C:\Program Files\Microsoft Office\root\Office16\MSACCESS.EXE')
            speak('Let\'s get the work done!')

        elif 'bye' in query or 'exit' in query or 'quit' in query or 'stop' in query:
            currentH = int(datetime.datetime.now().hour)
            if currentH == 0 or currentH >= 22 or currentH <= 3:
                speak('Goodnight Boss!, Have a sweet dreams.')
            else:
                speak('Bye Boss!, Have a good day.')
            sys.exit()

        elif 'shutdown' in query:
            speak('Okay Boss!')
            os.system('shutdown -s')
            sys.exit()

        elif 'in chrome' in query or 'in browser' in query:
            query=query.replace('open','')
            query=query.replace('.com','')
            query=query.replace('in chrome','')
            query=query.replace('in browser','')
            qry=(query+'.com'.replace(' ',''))
            webbrowser.open(qry)

        elif 'in youtube' in query:
            query=query.replace('play','')
            query=query.replace('song','')
            query=query.replace('in youtube','')
            qry=(query+'.com'.replace(' ',''))
            webbrowser.open(qry)
            
        else:
            try:
                try:
                    speak('searching')
                    res = client.query(query)
                    results = next(res.results).text
                    speak(results)
                except:
                    results = wikipedia.summary(query, sentences=10)
                    speak(results)
            except:
                speak('I don\'t know Sir! Google is smarter than me!')
                webbrowser.open('www.google.com')
        
        speak('Next Command Boss!')
    a=input()
