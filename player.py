#!/usr/bin/env python3

import playsound

global number

def file_open():
    global mp3
    file_name = input('Enter the txt file name !')
    file = open(file_name, "r")
    mp3 = []
    for i in file:
        mp3.append(i)
        
def play(input_music):
    playsound.playsound(input_music)
def change_music():
    for i in mp3:
        play(i)
        
file_open()  
while True:        
    change_music()


    
