import imaplib
import email
from bs4 import BeautifulSoup
import re

ORG_EMAIL = "@gmail.com"
FROM_EMAIL = "khagendrabhr" + ORG_EMAIL
FROM_PWD = 'epin azcw lcgk srqf'
SMTP_SERVER = "imap.gmail.com"
SMTP_PORT = 993

mail = imaplib.IMAP4_SSL(SMTP_SERVER)
mail.login(FROM_EMAIL, FROM_PWD)
mail.select('inbox')

result, data = mail.search(None, '(FROM "helpdesk@perplexity.ai")')

if result == 'OK':
    email_ids = data[0].split()
    for email_id in email_ids:
        result, email_data = mail.fetch(email_id, '(RFC822)')
        if result == 'OK':
            raw_email = email_data[0][1]
            email_message = email.message_from_bytes(raw_email)
            # Process the email message as needed

            pattern = r'\(https://www\.perplexity\.ai/api/auth/callback/email\?callbackUrl=.*?\)'
            email_content = email_message.as_string()

            # Search for the URL pattern in the email content
            matches = re.search(pattern, email_content)
            if matches:
                url = matches.group(1)
                print("Extracted URL:", url)
            else:
                print("URL not found in the email.")
        else:
            print("Error fetching email data.")

mail.close()
mail.logout()