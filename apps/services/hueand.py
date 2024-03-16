import requests
import os
import certifi

print(certifi.where())
BRIDGE_IP = os.getenv('HUE_BRIDGE_IP')
BRIDGE_USERNAME = os.getenv('HUE_BRIDGE_USERNAME')
HUE_BRIDGE_APPLICATION_KEY = os.getenv('HUE_BRIDGE_APPLICATION_KEY')


url = "https://" + BRIDGE_IP + "/clip/v2/resource/light/be2b2b03-fadd-428b-a59a-6927f839dba6"
headers = {
    "Content-Type": "application/json; charset=utf-8",
    "hue-application-key":HUE_BRIDGE_APPLICATION_KEY,
    "username": BRIDGE_USERNAME
    }
data = {"on": {"on": True}}

response = requests.put(url, headers=headers, json=data)

print("Status Code", response.status_code)
# print("JSON Response ", response.json())
