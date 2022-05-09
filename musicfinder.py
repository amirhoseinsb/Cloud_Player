#!/usr/bin/env python3

from bs4 import BeautifulSoup
import requests

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
        
def run_script():
    
    try:
        banner()
        
    except:
        print('banner Error!')
        
    try:
        name_input()
        requests_google()
        content_filter()
        link_finder()
        output_google()
    except:
        print('ERROR !')
        
        
run_script()