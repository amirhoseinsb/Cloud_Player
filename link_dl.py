#!/usr/bin/env python3

from bs4 import BeautifulSoup
import requests


def banner():
    print('''
 _     _       _    ____                      _                 _           
| |   (_)_ __ | | _|  _ \  _____      ___ __ | | ___   __ _  __| | ___ _ __ 
| |   | | '_ \| |/ / | | |/ _ \ \ /\ / / '_ \| |/ _ \ / _` |/ _` |/ _ \ '__|
| |___| | | | |   <| |_| | (_) \ V  V /| | | | | (_) | (_| | (_| |  __/ |   
|_____|_|_| |_|_|\_\____/ \___/ \_/\_/ |_| |_|_|\___/ \__,_|\__,_|\___|_|   
                                                                         
Created By : amirhoseinsohrabi
Gmail : amirhoseinsohrabi.official@gmail.com                                                                        

    ''')
    
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
    file_name = ("dl_link.txt")
    print("dl_link.txt Created !")
    try:
        for i in output:
            file = open(file_name, "a+")
            file.write(f'{i}\n')
            file.close()
    except:
        print('ERROR : Download File Is Not Created !')


def run_script():
    
        banner()
        input_url(input('Enter The Link !'))
        request_site()
        dl_link()
        link_filter()
        output_link()
        downloadfile()

run_script()