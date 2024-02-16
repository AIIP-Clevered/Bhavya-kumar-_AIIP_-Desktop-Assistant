from tkinter import *
import tkinter as tk
import speech_recognition as sr
import pyttsx3
import pyaudio
import os
import webbrowser



# tkinter GUI
root= tk.Tk()

r = sr.Recognizer()


def getSpeech():
    with sr.Microphone() as source:
        print("Listening...")
        #Adjust for ambient noise
        r.adjust_for_ambient_noise(source)
        #Listen
        audio = r.listen(source)
        #Process audio with google speech recogition AI
        print("Processing...")
        
        speech = r.recognize_google(audio)
        return speech
        myspeech(speech)

    
def myspeech(text):
    code=pyttsx3.init()
    code.say(text)
    code.runAndWait()
    
    



def va():
     stop = False
     query = getSpeech()
     myspeech(query)
     print(query)
     if "hello" in query:
      myspeech("hello")
     elif "calculator" in query:
      myspeech('Opening calculator now')
      webbrowser.open('calculator:')
     elif "open Google" in query:
      myspeech("Google Chrome")
      webbrowser.open("google.com")
     elif "open YouTube" in query:
      print("Opening Youtube now")
      webbrowser.open("youtube.com")
     elif "open youtube" in query:
      myspeech("Opening youtube now")
      webbrowser.open("youtube.com")
     elif 'open gmail' in query:
      myspeech("Opening gmail now")
      webbrowser.open("mail.google.com")
     elif 'open camera' in query:
      myspeech("Opening camera now")
      webbrowser.open("microsoft.windows.camera:")
     elif 'how are you' in query:
      myspeech("I am fine, Thank you for asking. I hope you are doing well too!")
     elif 'stop' in query:
      myspeech('Stopping the program')
      stop = True
     else:
      myspeech("Unable to hear you properly")
     if stop:
         end()
     else:
         va()     

def main():
    
    va()

def end():
    root.destroy()
    

canvas1 = tk.Canvas(root, width = 500, height = 300,bg = "black")
canvas1.pack()


button1 = tk.Button (root, text="Let's have a conversation",command = main)
canvas1.create_window(250, 190, window=button1)

button2 = tk.Button (root, text="Close",command = end)
canvas1.create_window(250, 250, window=button2)


label1 = tk.Label(root, text='DESKTOP ASSISTANT')

canvas1.create_window(250, 50, window=label1)


root.mainloop()
