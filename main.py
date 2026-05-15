import requests
import time
import random

BOT_TOKEN = https://api.telegram.org/bot8921402434:AAE_YHXjrCtPPZjlaq5b4oevkH7sazigfIc/getUpdates
CHAT_ID = 6402289413

pairs = [
    "EUR/USD OTC",
    "GBP/JPY OTC",
    "USD/JPY OTC",
    "EUR/GBP OTC",
    "AUD/USD OTC",
    "USD/CAD OTC",
    "NZD/USD OTC",
    "EUR/JPY OTC",
    "GBP/USD OTC",
    "USD/CHF OTC"
]

timeframes = ["5M", "10M"]
actions = ["BUY 📈", "SELL 📉"]

def send(msg):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": msg})

while True:
    pair = random.choice(pairs)
    tf = random.choice(timeframes)
    action = random.choice(actions)

    message = f"""
🔥 Peace Rich Alpha Signals Pro 🔥

PAIR: {pair}
TIMEFRAME: {tf}
ACTION: {action}

📊 Strategy: Trend + Momentum Confirmation
⏱ OTC Market Analysis

⚠️ Risk: 1–2%
"""

    send(message)
    time.sleep(300)
