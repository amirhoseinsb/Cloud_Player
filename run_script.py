#!/usr/bin/env python3


from bs4 import BeautifulSoup
import requests
import multiprocessing
from playsound import playsound


def banner():
    print("""
                
     __  __           _        _____ _           _           
    |  \/  |_   _ ___(_) ___  |  ___(_)_ __   __| | ___ _ __ 
    | |\/| | | | / __| |/ __| | |_  | | '_ \ / _` |/ _ \ '__|
    | |  | | |_| \__ \ | (__  |  _| | | | | | (_| |  __/ |   
    |_|  |_|\__,_|___/_|\___| |_|   |_|_| |_|\__,_|\___|_|   
                                                             
    Created By : AmirhoseinSohrabi
    Gmail : amirhoseinsohrabi.official@gmail.com            
                
                """)
    
def name_input():# Input The Singer Name
    global singername
    singername = str(input("Enter The Singer Name :"))
    singername = singername.lower()
    print('\n')
    
def requests_google():# Send Request to google
    global req
    try:
        session = requests.session()
        session.headers.update({'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/64.0.3282.167 Chrome/64.0.3282.167 Safari/537.36'})
        req = session.get(f"https://www.google.com/search?q=intitle:index%20of%20mp3%20intext:{singername}")
    except:
        print('ERROR : check the internet connection !')
        
def content_filter():# Filter the Content
    global content
    try:
        soup = BeautifulSoup(req.content,'html.parser')
        content = soup.select('a')
    except:
        print('')
        
def link_finder():# Find the url
    global links
    links = []
    try:
        for i in content :
                link = (i.get('href'))
                links.append(link)

    except:
        print('')
        
def output_google():# Output The Links
    number = 0
    link = links[9:19]
    try:
        for i in link:
                number += 1
                print(f'Link : {number} {i}\n') 

    except:
        print('')
        
def input_url(link): # Input the url 
    global url
    try:
        url = link
    except:
        print('Error : Url not found !')

def request_site():# Send request to the site
    global response
    try:
        session = requests.session()
        session.headers.update({'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/64.0.3282.167 Chrome/64.0.3282.167 Safari/537.36'})
        response = session.get(url)
    except:
        print('Error : Request failed !')
        
def dl_link():# find the download link
    global dl__link
    try:
        soup = BeautifulSoup(response.content,'html.parser')
        dl__link = soup.select('a')
    except:
        print('Error : Link not found !')
        
def link_filter():# export the link
    global output
    output = []
    for i in dl__link:
         x = (i.get('href'))
         if '.mp3' in x:
            output.append(f'{url}{x}') 
         else:
             continue
 
def output_link():
    counter = 0
    for i in output:
        counter += 1
        print(f"{counter} : {i}\n") 
        
        
def downloadfile():# create the text file for download the music with download manager
    file_name = (f"{singername}.txt")
    print(f"{singername}.txt Created !")
    try:
        for i in output:
            file = open(file_name, "a+")
            file.write(f'{i}\n')
            file.close()
    except:
        print('ERROR : Download File Is Not Created !')
        
global number

def file_open():
    global mp3
    file_name = (f"{singername}.txt")
    file = open(file_name, "r")
    mp3 = []
    for i in file:
        mp3.append(i)
        
def change_music():
        input('''\nPress Enter to Next Music ! \nPress CTRL + Z for exit !
              ''')
        music.terminate()
        
def play():
    global music  
    z = 0
    try:
       for i in range(99999):   
           music = multiprocessing.Process(target=playsound, args=(mp3[z],))
           music.start()
           change_music()
           z +=1
    except:
        print('\n Error : Invalid Url Address !')
        

        
 

def run_script():

    banner()
    name_input()
    requests_google()
    content_filter()
    link_finder()
    output_google()
    link = links[9:19]
    for z in link:
        input_url(z)
        try:
           request_site()
           dl_link()
           link_filter()
           output_link()
           downloadfile()
        except:
                print('The link is not valid')
    file_open()
    while True:
        play()
        
     



run_script()
