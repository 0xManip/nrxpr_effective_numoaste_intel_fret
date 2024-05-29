import requests
import json
import random
import string
import time
import os

def send_message(channel_id, message, token):
    url = f"https://discord.com/api/v10/channels/{channel_id}/messages"

    headers = {
        "accept": "*/*",
        "accept-language": "en-US,en-GB;q=0.9",
        "content-type": "application/json",
        "origin": "https://discord.com",
        "sec-ch-ua-mobile": "?0",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "x-debug-options": "bugReporterEnabled",
        "x-discord-locale": "en-US",
        "Authorization": f"{token}",
    }

    payload = {
        "content": message,
    }

    response = requests.post(url, headers=headers, data=json.dumps(payload))

    if response.status_code != 200:
        print(f"Falha ao enviar mensagem: {response.status_code} - {response.text}")


def generate_random_message():
    length = random.randint(20, 100)
    random_string = ''.join(random.choices(string.ascii_letters, k=length))
    return random_string


if __name__ == "__main__":
    spam_channel = os.getenv("dach")
    
    tokens = [
        os.getenv("acc_1"),
        os.getenv("acc_2"),
        os.getenv("acc_3"),
        os.getenv("acc_4"),
        os.getenv("acc_5"),
        os.getenv("acc_6")
    ]

    while True:
        for token in tokens:
            time.sleep(0.4)
            send_message(spam_channel, generate_random_message(), token)
