# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 15:04:51 2020

@author: Sahil Shaikh
"""


import speech_recognition as sr
AUDIO_FILE=("answer.wav")
#use audio file as source

r=sr.Recognizer() #intialize the recogniser
print('Heloo')
with sr.AudioFile(AUDIO_FILE) as source:
    audio=r.record(source) 
#reads the audio file
    
try:
    print('hiii')
    print("audio file contains "+r.recognize_google(audio))
except sr.UnknownValueError :
    print("Google Speech Recognition could not understand audio")
except sr.RequestError :
    print("could'nt get the result from Google Speech Recognition")