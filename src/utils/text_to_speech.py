import pyttsx3
import os


engine = pyttsx3.init()

id = 1

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[id].id)

# Change the speed
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-30)  # Decrease the speed by 50

# The text that you want to convert to audio
file_name = "Chapter_1.txt"

file = open(file_name, "r", encoding="utf8")
mytext = file.read()


engine.save_to_file(mytext, 'welcome_' + str(id) + '.mp3')

engine.runAndWait()