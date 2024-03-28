import tkinter as tk
from tkinter import PhotoImage
import speech_recognition as sr
import pyttsx3
import webbrowser
import os
root = tk.Tk()
root.title("Speech Recognition Virtual Assistant")

x = 1024  # canvas width
y = 768   # canvas height

r = sr.Recognizer()

def get_speech():
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        print("Processing...")
        try:
            speech = r.recognize_google(audio)
            print("You said:", speech)
            return speech
        except sr.UnknownValueError:
            print("Sorry, could not understand audio.")
            return None
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
            return None

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def process_query(query):
    if query is None:
        speak("Sorry, I couldn't understand you.")
        return

    if "hello" in query:
        speak("Hello!")
    elif "calculator" in query:
        speak("Opening calculator now")
        webbrowser.open('calculator:')
    elif "open Google" in query:
        speak("Opening Google Chrome now")
        webbrowser.open("https://www.google.com")
    elif "open YouTube" in query or "open youtube" in query:
        speak("Opening YouTube now")
        webbrowser.open("https://www.youtube.com")
    elif 'play' in query:
        speak(("now playing "+query.partition("play")[2]))
        webbrowser.open("https://www.youtube.com/results?search_query="+query.partition("play")[2])
    elif 'open gmail' in query:
        speak("Opening Gmail now")
        webbrowser.open("https://mail.google.com")
    elif 'open camera' in query:
        speak("Opening camera now")
    elif 'blender' in query:
        speak("Opening blender now")
        os.system("blender")
        webbrowser.open("microsoft.windows.camera:")
    elif 'thank' in query:
        speak("No Problem , thanks for using me")
        close()
    elif 'how are you' in query:
        speak("I am fine, Thank you for asking. I hope you are doing well too!")
    else:
        speak("Sorry, I cannot fulfill this request.")


def main():
    button1.config(state=tk.DISABLED)
    speak("How can I help you?")
    query = get_speech()
    process_query(query)
    button1.config(state=tk.NORMAL)

def close():
    root.destroy()
    

canvas1 = tk.Canvas(root, width=x, height=y, bg="black")
canvas1.pack()

title_img = PhotoImage(file="title.png")
canvas1.create_image(x/2, y/10, anchor=tk.CENTER, image=title_img)

ai1_img = PhotoImage(file="ai1.png")
canvas1.create_image(x/2, y/25, anchor=tk.CENTER, image=ai1_img)

ai2_img = PhotoImage(file="ai2.png")
canvas1.create_image(x/3, y/2, anchor=tk.CENTER, image=ai2_img)

ai3_img = PhotoImage(file="ai3.png")
canvas1.create_image(x/5, y/5, anchor=tk.CENTER, image=ai3_img)

speak_img = PhotoImage(file="speak.png")
button1 = tk.Button(root, text="Speak", image=speak_img, height=70, width=250, command=main, bg="#0000ff", bd=5, highlightcolor="#00004d", activebackground="#0000ff")
canvas1.create_window(x/2, y/2.1, window=button1)

button2 = tk.Button(root, text="Close", command=close, bg="red")
canvas1.create_window(x/15, y/1.05, window=button2)

root.mainloop()
