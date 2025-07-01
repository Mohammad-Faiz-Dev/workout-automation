import requests
from datetime import datetime

# -------------------- NUTRITIONIX CONFIG --------------------

# Replace with your Nutritionix App ID and API Key
APP_ID = "YOUR_NUTRITIONIX_APP_ID"
API_KEY = "YOUR_NUTRITIONIX_API_KEY"

NUTRITIONIX_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

nutritionix_headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Content-Type": "application/json"
}

# Replace this with the text input describing your workout
user_input = "ran 3 miles and did 20 push-ups"

# Replace with your own physical data
nutritionix_params = {
    "query": user_input,
    "gender": "male",  # or "female"
    "weight_kg": 70,  # your weight in kg
    "height_cm": 175,  # your height in cm
    "age": 25  # your age in years
}


def log_exercises():
    # Make the POST request to Nutritionix
    response = requests.post(
        url=NUTRITIONIX_ENDPOINT,
        json=nutritionix_params,
        headers=nutritionix_headers
    )

    response.raise_for_status()
    result = response.json()
    exercises = result["exercises"]

    # -------------------- SHEETY CONFIG --------------------

    # Replace with your Sheety endpoint URL
    SHEETY_ENDPOINT = "https://api.sheety.co/YOUR_PROJECT_ID/YOUR_SHEET_NAME/workouts"

    now = datetime.now()
    current_date = now.strftime("%d/%m/%Y")
    current_time = now.strftime("%H:%M:%S")

    for exercise in exercises:
        sheet_input = {
            "workout": {
                "date": current_date,
                "time": current_time,
                "exercise": exercise["name"].title(),
                "duration": exercise["duration_min"],
                "calories": exercise["nf_calories"]
            }
        }

        sheet_response = requests.post(
            url=SHEETY_ENDPOINT,
            json=sheet_input
        )

        print(sheet_response.text)


if __name__ == "__main__":
    log_exercises()