import requests
import os

def send_slack(message):
    webhook = os.getenv("SLACK_WEBHOOK")

    if not webhook:
        print("No webhook set")
        return

    try:
        requests.post(webhook, json={"text": message})
    except:
        print("Slack alert failed")
