import smtplib
import speech_recognition as speech
import webbrowser as web
import pyttsx3
import cv2
import random
import os
import datetime

speaker = pyttsx3.init()
r = speech.Recognizer()
a = 1
"' idea==>delete name or goo morning wish from my statements" \
" idea==>use csv file" \
"idea==> to add a reminder who reminds me about upcoming exams , and we can combine the first idea with it" \
"ask to quit if running for too long'"
"idea==>add timer which set on clock app"


def speak(a):
    speaker.say(a)
    speaker.runAndWait()


def time_table():
    now = datetime.datetime.now()
    hour = int(now.strftime("%H"))
    day = now.strftime("%a")
    if day == "Sun":
        speak("sir today is sunday you have no fix routine")
    else:
        if hour == 8:
            speak("sir,its school time do and get ready for school")
        elif hour <= 3:
            speak("sir its too late to work you must sleep,good night sir")
        elif hour <= 4:
            speak("sir you must sleep now or you become a nice boy who is waking up early in morning")
        elif hour <= 7:
            speak("such a good boy u can go for exercise or you can study")
        elif hour <= 9:
            speak("oh sir,is today is you holiday ,nice you can study,")
        elif hour == 22:
            speak("you can go for dinner")
        else:
            speak("sir no particular but routine u can add so..")


def sendmail(to, content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login("025.sahil@gmail.com", "sahil12345")
    server.sendmail("025.sahil@gmail.com", to, content)
    server.close()


def clear():
    os.system('cls')


k = cv2.waitKey(1) & 0xFF

while a == 1:
    curent = datetime.datetime.now()
    hou = int(curent.strftime("%H"))
    if hou <= 12:
        speak("good morning sir")
    elif hou <= 18:
        speak("good afternoon sir")
    else:
        speak("good evening sir")
    speak("what you like to do")
    a = 2
    break
print("Speak Anything :")
while True:
    with speech.Microphone() as source:
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            print(text)
            teli = text.split()
            if text == "hello Rahul" or text == "hello":
                speaker.setProperty('voice','HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_enIN_HeeraM')
                speaker.setProperty('rate', 150)
                speak("or bhai kesa hai")
                speak("tell your password")
                passwa = r.listen(source)
                passward = r.recognize_google(passwa)
                if passward == "I am alive":
                    speak("your secret file is unlocked")  # no file is unlock just for fun soon add something
            elif text == "open YouTube":
                speak("what you want to search")
                print('tell now:')
                while True:
                    try:
                        ayou = r.listen(source)
                        tyou = r.recognize_google(ayou)
                        break
                    except:
                        speak("sorry sir cant understand what u said please say again")
                        print("say again:")
                print(tyou)
                if tyou != "nothing":
                    speak("searching")
                    web.open("https://www.youtube.com/results?search_query=" + tyou, new=1)
                else:
                    web.open_new_tab("https://www.youtube.com")
            elif text == "open Google" or text == "open Chrome" or text == "Google" or text == "Chrome":
                speak("what you want to search")
                print('tell now:')
                while True:
                    try:
                        agoo = r.listen(source)
                        tgoo = r.recognize_google(agoo)
                        break
                    except:
                        speak("sorry sir cant understand what u said please say again")
                        print("say again:")
                print(tgoo)
                if tgoo != "nothing":
                    speak("searching")
                    web.open(
                        "https://www.google.com/search?rlz=1C1CHBF_enIN920IN920&sxsrf=ALeKk02W4tn0-6kjWr1AWBryMXCay3HD4A%3A1614775973032&ei=pYY_YJ65AdDyrAHE5Y-4BA&q=" + tgoo,
                        new=2)
                else:
                    web.open_new_tab("https://www.googl4e.com")
            elif text == "open Notepad" or text == "Notepad":
                speak("opening Notepad")
                os.startfile("C:\\WINDOWS\\system32\\notepad.exe")
            elif text == "open command prompt":
                speak("opening command prompt")
                os.system("start cmd")
            elif text == "open camera":
                cap = cv2.VideoCapture(0)
                while True:
                    ret, frame = cap.read()  # returns ret and the frame
                    cv2.imshow('frame', frame)
                    k = cv2.waitKey(1)
                    if k == 27:
                        break
                cap.release()
                cv2.destroyWindow()
            elif text == "send email":
                speak("who u like to  send this email")
                atomail = r.listen(source)
                ttomail = r.recognize_google(atomail)
                print(ttomail)
                if ttomail == "mummy" or "anita singh":
                    to = "asingh999777@gmail.com"
                speak("what should i say")
                amail = r.listen(source)
                tmail = r.recognize_google(amail)
                print(tmail)
                sendmail(to, tmail)
                speak("email send")
            elif text == "open spotify":
                speak("which song you want to listen sir")
                aspo = r.listen(source)
                tspo = r.recognize_google(aspo)
                print(tspo)
                if tspo != "nothing" and tspo != "anything" and text != "random":
                    web.open_new_tab("https://open.spotify.com/search/" + tspo)
                else:
                    web.open_new_tab("https://open.spotify.com")
            elif text == "play song" or text == "play music":
                songs = os.listdir('D:\\dino')
                x = random.choice(songs)
                os.startfile(os.path.join("D:\\dino", x))
            elif text == "are you dumb":
                speaker.say("sorry for inconvenience sir but every computer is dumb,you don't know, dumb!")
                speaker.runAndWait()
            elif text == "tell my routine" or text == "any routine plan":
                time_table()
            elif text == "open spotify app":
                os.startfile("C:\\WINDOWS\\system32\\notepad.exe")
            elif text == "trash talk mod" or text == "trash talk mode":
                speak("i am trash talking")  # aded some trash talk
            elif text == "change name" or text == "change your name":
                speak("what name you want to give me")
                while True:
                    try:
                        anam = r.listen(source)
                        tnam = r.recognize_google(anam)
                        break
                    except:
                        pass
                print(tnam)
                with open("C:\\Users\\025sa\\PycharmProjects\\funfriend\\fun friend name.txt", 'w') as f:
                    f.write(tnam)
                speak("my name changes to" + tnam)
            elif text == "what is your name" or text == "what's your name":
                with open('C:\\Users\\025sa\\PycharmProjects\\funfriend\\fun friend name.txt', 'r') as readname:
                    speak("my name is" + readname.read())
            elif text in ["exit", "end", "execute", "stop", "quit", "good night"]:
                speak("Thank you for using me sir")
                cur = datetime.datetime.now()
                hou = int(cur.strftime("%H"))
                if text != "good night" and hou >= 20 or hou <= 2:
                    speak("good night")
                break
        except:
            speak("pl")
            pass
