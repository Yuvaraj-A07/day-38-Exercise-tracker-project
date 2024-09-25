import requests
from datetime import datetime
import os
from requests.auth import HTTPBasicAuth
import manager as mg

API_ID = mg.API_ID
API_KEY = mg.API_KEY

USER = mg.USER
PASSWORD = mg.PASSWORD

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exe_header = {
    "x-app-id": API_ID,
    "x-app-key": API_KEY
}

exe_query = {
    "query": input("Tell me which exercise you did? ")
}

response = requests.post(url=exercise_endpoint, json=exe_query, headers=exe_header)
response.raise_for_status()

data = response.json()["exercises"][0]
duration_min = data["duration_min"]
nf_calories = data["nf_calories"]
name = data["name"].title()
today = datetime.now()
today_date = today.strftime("%Y/%m/%d")
today_time = today.strftime("%H:%M:%S")

sheety_endpoint = "https://api.sheety.co/3faead5c9d091473879dcd600616337d/workoutTracking/workouts"

# basic = HTTPBasicAuth(USER, PASSWORD)
# requests.get(url=sheety_endpoint, auth=(USER, PASSWORD))

sheety_config = {
    "workout": {
        "date": today_date,
        "time": today_time,
        "exercise": name,
        "duration": duration_min,
        "calories": nf_calories

    }
}

bearer_headers = {
    "Authorization": "Bearer yuvaraj@2004"
}

submit = requests.post(url=sheety_endpoint, json=sheety_config, headers=bearer_headers)
print(submit.text)

# # No Authentication
# sheet_response = requests.post(sheet_endpoint, json=sheet_inputs)
#
# # Basic Authentication
# sheet_response = requests.post(
#     sheet_endpoint,
#     json=sheet_inputs,
#     auth=(
#         YOUR USERNAME,
#     YOUR PASSWORD,
#     )
# )
#
# # Bearer Token Authentication
# bearer_headers = {
#     "Authorization": "Bearer YOUR_TOKEN"
# }
# sheet_response = requests.post(
#     sheet_endpoint,
#     json=sheet_inputs,
#     headers=bearer_headers
# )