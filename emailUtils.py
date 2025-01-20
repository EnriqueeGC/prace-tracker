import yagmail
import os
from dotenv import load_dotenv

load_dotenv()

EMAIL_ADDRESS = os.getenv('EMAIL')
EMAIL_PASSWORD = os.getenv('PASSWORD')

def sendEmail(subject, body, toEmail):
    try:
        yag = yagmail.SMTP(EMAIL_ADDRESS, EMAIL_PASSWORD)
        
        yag.send(subject=subject, contents=body, to=toEmail)
    except Exception as e:
        print(f"Error al enviar el correo: {e}")



    