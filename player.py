#!/usr/bin/env python3

import multiprocessing
from playsound import playsound

counter = 0

def file_open():
    global mp3
    file_name = input('Enter the txt file name !')
    file = open(file_name, "r")
    mp3 = []
    for i in file:
        mp3.append(i)
        
def play():
    global music    
    try:
       music = multiprocessing.Process(target=playsound, args=(mp3[counter],))
       music.start()
    except:
        print('\n Error : Invalid Url Address !')
        
def change_music():
        input('\nPress Enter to Next Music !')
        music.terminate()

        
file_open()        
while True:
    play()
    change_music()
    counter +=1

    
