
import requests
import time

config = {"telegram" : { "token" : "1050323242:AAEfmwVfdedfFG-97STdNH78EVs6wr1Zi_Mxwsd32", "chat_id" : "-1301267345033" }}

def notifyTelegram(message):
    try:
        token = config["telegram"]["token"]
        chat_id = config["telegram"]["chat_id"]
    except KeyError:
        print("Please define Telegram config to enable notifications")
        return

    telegramUrl = "https://api.telegram.org/bot{}/sendMessage".format(token)

    # Slice the message in multiple part
    msgs = [message[i:i + 4096] for i in range(0, len(message), 4096)]
    for text in msgs:
        requests.post(telegramUrl, json={'text': text, 'chat_id': chat_id})
        time.sleep(5)
