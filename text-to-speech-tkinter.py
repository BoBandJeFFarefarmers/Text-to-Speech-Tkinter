from tkinter import *
import pyttsx3

root = Tk()
root.title("Text to Speech Converter")
root.geometry("500x500")
root.resizable(False, False)

def speech():
    text_speech = pyttsx3.init()

    text_speech.say(entry.get())

    text_speech.runAndWait()

question = Label(root, text="What do you want to convert to speech?", font=("Comic Sans MS", 17))
question.pack()

entry = Entry(root, width=500)
entry.pack(pady=20)

convertButton = Button(root, text="Convert to Speech", font=("Comic Sans MS", 17), command=speech)
convertButton.pack(pady=20)


root.mainloop()