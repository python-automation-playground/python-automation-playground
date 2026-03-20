from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv()

client = Client(
    os.getenv("TWILIO_ACCOUNT_SID"),
    os.getenv("TWILIO_AUTH_TOKEN")
)

def send_whatsapp(phone, task):
    client.messages.create(
        from_="whatsapp:+14155238886",
        body=f"⏰ Reminder: It's time to *{task}*",
        to=f"whatsapp:{phone}"
    )
