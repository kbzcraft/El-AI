import webbrowser
import pyautogui
from time import sleep
import json
import pyperclip
import subprocess
def getBardCookies():
    # Move the mouse cursor to the target position
    pyautogui.moveTo(25, 100)

    try:
        subprocess.run(["clear"])
        print("Google Chrome is closed.")
    except Exception as e:
        print(f"An error occurred: {e}")
        # print("chrome is already close.")
    sleep(.5)
    url = "https://bard.google.com/"
    webbrowser.open(url)
    sleep(5)
    pyautogui.click(x=557, y=107)
    sleep(1)
    pyautogui.click(x=426, y=285)
    sleep(1)
    pyautogui.click(x=347, y=138)
    sleep(1)

    # Your provided list of cookie objects
    data = pyperclip.paste() 
    if data is not None:
        print('Cookie Extraction sucessfull \n')

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
    pyautogui.hotkey('ctrl', 'w')
    return cookie_dict

