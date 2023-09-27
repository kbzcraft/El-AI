from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import sys
sys.path.append("/home/kb/el/") #import your project parent dir here

import warnings
warnings.simplefilter("ignore")
print("Import done.")
chrome_options = Options()
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
chrome_options.add_argument('--log-level=3')
chrome_options.add_argument("--use-fake-ui-for-media-stream")  # This flag grants permission to access the microphone
chrome_options.add_argument("--use-fake-device-for-media-stream")
chrome_options.add_argument("--headless=new")

# initialize th Webdriver 
url = "http://127.0.0.1:8000/"

print("opening the browser")
driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
driver.get(url)
driver.execute_script('navigator.mediaDevices.getUserMedia({ audio:true })')



while True:
    
    text = driver.find_element(By.ID,"txt").text
    if len(text) > 1:
        print(text)
        driver.refresh()
    else:
        continue