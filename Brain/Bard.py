
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
print(data)

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
    Query = input("\nEnter Your Query:\n===>")
    BardReply = bard.get_answer(Query)['content']
    # Reply = bert_model(BardReply, min_length=25, max_length=100)
    # Tokenize the text into words
    words = re.findall(r'\w+', BardReply.lower())
    # Calculate word frequency
    word_freq = Counter(words)
    # Calculate sentence scores based on word frequency
    sentences = re.split(r'[.!?]', BardReply)
    sentence_scores = {}
    for sentence in sentences:
        for word in re.findall(r'\w+', sentence.lower()):
            if word in word_freq:
                if sentence not in sentence_scores:
                    sentence_scores[sentence] = word_freq[word]
                else:
                    sentence_scores[sentence] += word_freq[word]

    # Sort sentences by score
    sorted_sentences = sorted(sentence_scores.keys(), key=lambda x: sentence_scores[x], reverse=True)

    # Print the top 3 sentences as the summary (you can adjust the number)
    summary = '. '.join(sorted_sentences[:1])
    print(summary)
    # print(BardReply)


