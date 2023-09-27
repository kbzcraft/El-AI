from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


import warnings
warnings.simplefilter("ignore")
print("Import done.")
chrome_options = Options()
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
chrome_options.add_argument('--log-level=3')
chrome_options.add_argument("--use-fake-ui-for-media-stream") #Allows microphone ascess
chrome_options.add_argument("--use-fake-device-for-media-stream")
chrome_options.add_argument("--headless=new")
# initialize th Webdriver 
url = "https://dictation.io/speech"

print("opening the browser")
driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
driver.get(url)
sleep(.5)
try:
    print("Eating Cookies")
    driver.find_element(By.XPATH, "/html/body/div[1]/div").click()
except:
    print("Didn't like those cookies")
try:
    print("Connecting to microphone.")
    driver.execute_script('navigator.mediaDevices.getUserMedia({ audio:true })')
except:
    print("Unable to excess microphone")
    exit()
try:
    print("Setting Language to en-in")
    driver.execute_script("localStorage.setItem('language','en-in')")
except:
    print("unable to clear set language to en-in")
try:
    print("Clearing my throat")
    driver.execute_script("localStorage.setItem('dictation','<p><br></p>')")
    driver.refresh()
except:
    print("Unable to clear Throat.")

sleep(.5)
driver.execute_script("dictation('clear')")
# clearBtnXPATH = "/html/body/div[3]/section/div/div/div[2]/div/div[3]/div[2]/a[8]/span"
startBtnXPATH = "/html/body/div[3]/section/div/div/div[2]/div/div[3]/div[1]/a"
# copyBtnXPATH = "/html/body/div[3]/section/div/div/div[2]/div/div[3]/div[2]/a[1]"
textXPATH = "/html/body/div[3]/section/div/div/div[2]/div/div[2]"
# clearBtn = driver.find_element(By.XPATH,clearBtnXPATH)
startBtn = driver.find_element(By.XPATH,startBtnXPATH)
# copyBtn = driver.find_element(By.XPATH,copyBtnXPATH)
current_text = driver.find_element(By.XPATH,textXPATH)


print("We can having conversation now.")
def listen():
    with open("Database/current_query.txt","w") as f:
        f.write("")
        f.close()    
    startBtn.click()
    while True:
        transcript = current_text.text
        if len(transcript) != 0:
            print(transcript)
            with open("Database/current_query.txt","w") as f:
                f.write(transcript)
                f.close()
            # clearBtn.click()
            driver.execute_script("dictation('clear')")

listen()