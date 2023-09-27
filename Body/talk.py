import os
from time import sleep
from dotenv import load_dotenv
from elevenlabs import set_api_key, generate, play  
import datetime
import sys
sys.path.append("/home/kb/el/") #import your project parent dir here
# Load environment variables from the .env file
load_dotenv()
# Access the API key using the os.environ dictionary
api_key = os.environ.get("_API_ELEVEN")
set_api_key(api_key=api_key)

def talk(query):
    audio = generate(
        text = query,
        voice = "Charlotte",
        model="eleven_monolingual_v1"
    )
    date = datetime.datetime.now()
    filename = query.split(" ")[0]
    filename += "--"
    filename += query.split(" ")[-1]
    date = date.strftime("%b-%mm%Ss")
    with open(f"Database/Voice-rec/{filename}-{date}.mp3","wb") as f:
        f.write(audio)
    play(audio)
    
current_reply = ""
while True:
    # sleep(1)
    sleep(1)
    with open("Database/chatGpt/current_reply.txt","r") as f:
        reply = f.read()
        if current_reply != reply:
            talk(reply)
            current_reply = reply
           
        else:
            pass
        