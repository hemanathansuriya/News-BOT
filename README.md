# 📰 WhatsApp News Bot using Twilio

This project sends trending news updates directly to your WhatsApp using the Twilio API and NewsData.io.

---

## 🚀 Features

- Get top trending news headlines (custom topic or default fallback)
- Sends alerts to WhatsApp every hour
- Easily configurable using `.env` file

---

## 📦 Tech Stack

- Python
- Twilio API (WhatsApp messaging)
- NewsData.io API
- `requests`, `python-dotenv`

---

## 🔐 Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/whatsapp-news-bot.git
cd whatsapp-news-bot

2️⃣
 Create and activate virtual environment
pip install -r requirements.txt

3️⃣ Create .env file and add your API keys
NEWSDATA_API_KEY=your_newsdata_api_key
TWILIO_SID=your_twilio_sid
TWILIO_AUTH_TOKEN=your_twilio_auth_token
FROM_WHATSAPP_NUMBER=whatsapp:+14155238886
TO_WHATSAPP_NUMBER=whatsapp:+91XXXXXXXXXX

4️⃣ Run the bot
python bot.py

THANKYOU!..


