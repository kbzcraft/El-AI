import sys
sys.path.append("/home/kb/el/") #import your project parent dir here
from functions.updateBardCookies import getBardCookies as gbc
from bardapi import BardCookies
import datetime
import re
from collections import Counter


cookie_dict = gbc()
bard = BardCookies(cookie_dict=cookie_dict)




while True:
    Query = input("\nEnter Your Query:\n===>")
    BardReply = bard.get_answer(Query)['content']
    date=datetime.datetime.now()
    current_date=date.strftime("%y%b%a_%mm-%Ss")
    with open(f"Database/BardReplies/{current_date}.txt","w") as f:
        f.write(f"Q: {Query}\nA: {BardReply}")
    print(BardReply.split(".")[0])

        


