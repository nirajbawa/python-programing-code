# from win32com.client import Dispatch

# get =  raw_input()

# speak = Dispatch("SAPI.SpVoice")
# speak.Speak(get)


# Python program to show 
# how to convert text to speech 
import pyttsx3 
  
# Initialize the converter 
converter = pyttsx3.init() 
  
# Set properties before adding 
# Things to say 
  
# Sets speed percent  
# Can be more than 100 
converter.setProperty('rate', 50) 
# Set volume 0-1 
converter.setProperty('volume', 20) 
  
# Queue the entered text  
# There will be a pause between 
# each one like a pause in  
# a sentence 

get = raw_input("inter input")

converter.say(get) 

  
# Empties the say() queue 
# Program will not continue 
# until all speech is done talking 
converter.runAndWait() 

