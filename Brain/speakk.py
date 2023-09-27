# Import necessary packages
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import warnings
from selenium.webdriver.common.keys import Keys
import pathlib
from dotenv import load_dotenv
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
load_dotenv()

warnings.simplefilter("ignore")
url = "https://pi.ai/talk"
scriptDirectory = pathlib.Path().absolute()
# chrome_driver_path = 'Brain\\chromedriver.exe'
chrome_options = Options()
chrome_options.add_argument("--headless=new")
# chrome_options.headless=False
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
chrome_options.add_argument('--log-level=3')
# chrome_options.add_argument('--detach=true')
# service = Service(chrome_driver_path)
user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
chrome_options.add_argument(f'user-agent={user_agent}')
driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
driver.get(url)
sleep(.5)
driver.refresh()

FB_ID = os.environ.get("_FB_ID")
FB_PASS = os.environ.get("_FB_PASS")

def click_element_with_wait(driver, by, value, timeout=10):
    try:
        element = WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((by, value)))
        element.click()
    except Exception as e:
        print(f"Failed to click element: {e}")

def enter_text_with_wait(driver, by, value, text, timeout=10):
    try:
        element = WebDriverWait(driver, timeout).until(EC.presence_of_element_located((by, value)))
        element.send_keys(text)
    except Exception as e:
        print(f"Failed to enter text: {e}")


def Login(Id, Passcode):

    try:
        # Click the first button
        print("Trying to login")
        click_element_with_wait(driver, By.XPATH, "/html/body/div/main/div/div/div[3]/button")
        sleep(1)
        # Click the second button
        click_element_with_wait(driver, By.XPATH, "/html/body/div/main/div/div/div[3]/div[2]/button[1]")
        sleep(2)
        # Click the third button
        click_element_with_wait(driver, By.XPATH, "/html/body/div/main/div/div/div[1]/div/div/div[1]/div/div[1]/div[2]/button")
        sleep(2.5)
        # Enter Id and Passcode
        enter_text_with_wait(driver, By.XPATH, "//*[@id='email']", Id)
        # /html/body/div[1]/div[2]/div[1]/div/div/div[2]/div[1]/form/div/div[1]/input
        enter_text_with_wait(driver, By.XPATH, "//*[@id='pass']", Passcode)
        sleep(.5)
        # Click the login button
        click_element_with_wait(driver, By.XPATH, "//*[@id='loginbutton']")
        sleep(5)
        print("log in was sucessfull")
    except Exception as e:
        print(e)
voiceButtonXpath="/html/body/div/main/div/div/div[2]/div/div[2]/button"
def SendQuery(text):
    enter_text_with_wait(driver=driver,by=By.XPATH, value="//*[@id='__next']/main/div/div/div[1]/div[4]/div/div[2]/div/div/textarea", text=text)
    click_element_with_wait(driver=driver,by=By.XPATH,value="/html/body/div/main/div/div/div[1]/div[4]/div/div[2]/div/button")

AnswerXpath="/html/body/div/main/div/div/div[1]/div[2]/div/div/div[3]/div/div/div[2]"
# /html/body/div/main/div/div/div[1]/div[2]/div/div/div[3]/div/div/div[2]/div
# /html/body/div/main/div/div/div[1]/div[2]/div/div/div[3]/div/div/div[2]
# /html/body/div/main/div/div/div[1]/div[2]/div/div/div[3]/div/div/div[2]/div
def talkMode(mode=True):
    
    if mode == True:
        driver.refresh()
        click_element_with_wait(driver=driver, by=By.XPATH, value="//*[@id='__next']/main/div/div/div[2]/div/div[2]/button")


def getAnswer():
    sleep(1)
    while True:
        driver.refresh()
        try:
            WebDriverWait(driver,10).until(EC.presence_of_all_elements_located((By.XPATH,AnswerXpath)))
            # sleep(1)
            text = driver.find_element(By.XPATH,AnswerXpath)
        except:
            continue
        if len(text.text) > 2:
            break
    print(text.text)
    talkMode(True)
    
Login(FB_ID,FB_PASS)


while True:
    q = input("query: ")
    SendQuery(q)
    sleep(2)
    getAnswer()
    
    
    
    
