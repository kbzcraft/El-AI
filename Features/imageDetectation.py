
from bardapi import BardCookies
import datetime

import json

import webbrowser
import pyautogui
#import keyboard
import pyperclip
from time import sleep
from collections import Counter
import re

webbrowser.open("https://bard.google.com/")
sleep(5)
pyautogui.click(x=557, y=107)
sleep(1)
pyautogui.click(x=426, y=285)
sleep(1)
pyautogui.click(x=347, y=138)
sleep(1)
#print(pyautogui.position())
#print(pyperclip.paste())

# Your provided list of cookie objects
data = pyperclip.paste() 
if data is not None:
    print('Cookie Extraction sucessfull \n')

# Parse the clipboard content as JSON
try:
    cookies_list = json.loads(data)
except json.JSONDecodeError:
    print("Error parsing clipboard data as JSON.")
    cookies_list = []


cookie_dict = {
    "__Secure-1PSID" : "",
    "__Secure-1PSIDTS" : "",
    "__Secure-1PSIDCC" : ""
}



for d in cookies_list:
    if d['name']=='__Secure-1PSID':
        cookie_dict["__Secure-1PSID"] = d["value"]
        # print(d['value'])
    if d['name']=='__Secure-1PSIDTS':
        # print(d['value'])
        cookie_dict["__Secure-1PSIDTS"] = d["value"]
    if d['name']=='__Secure-1PSIDCC':
        # print(d['value'])
        cookie_dict["__Secure-1PSIDCC"] = d["value"]


print(cookie_dict)

bard = BardCookies(cookie_dict=cookie_dict)




while True:
    imagepath = str(input("Enter Image path:\n===> "))
    image = open(imagepath, 'rb').read()
    BardReply = bard.ask_about_image('What is in this image?', image=image)['content']
    paragraphs = BardReply.split('\n\n')
    data = paragraphs[:2]
    separator = ', '
    imgInfo = separator.join(data) 
    print(imgInfo)
