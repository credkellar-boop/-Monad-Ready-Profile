import requests

def send_slack_alert(webhook_url, message):
    payload = {"text": message}
    requests.post(webhook_url, json=payload)
