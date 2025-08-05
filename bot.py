import os
import requests
from dotenv import load_dotenv
from twilio.rest import Client

# Load environment variables from .env file
load_dotenv()

# Read credentials and config
NEWS_API_KEY = os.getenv("NEWSDATA_API_KEY")
TWILIO_SID = os.getenv("TWILIO_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
FROM_WHATSAPP = os.getenv("FROM_WHATSAPP_NUMBER")
TO_WHATSAPP = os.getenv("TO_WHATSAPP_NUMBER")

# Setup Twilio Client
client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

def get_trending_news():
    url = f"https://newsdata.io/api/1/news?apikey={NEWS_API_KEY}&country=in&language=en&category=top"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data["results"]:
            headlines = [news["title"] for news in data["results"][:5]]
            return "\n\n".join(headlines)
        else:
            return None
    else:
        return None

def send_whatsapp(message):
    client.messages.create(
        from_=FROM_WHATSAPP,
        to=TO_WHATSAPP,
        body=message
    )

# Main logic
news = get_trending_news()
if news:
    send_whatsapp("🗞️ *Today's Top News:*\n\n" + news)
else:
    send_whatsapp("⚠️ No trending news found at the moment.")
