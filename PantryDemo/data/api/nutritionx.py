from dotenv import load_dotenv
import requests
import os

# load env
load_dotenv()

# set app id and api key
app_id = os.getenv('APP-ID')
app_key = os.getenv('API-KEY')

# URL and query
def get_nutritionx(query):
    url = f"https://trackapi.nutritionix.com/v2/search/instant/?query={query}"
    headers = {
        "Content-Type": "application/json",
        "x-app-id": app_id,
        "x-app-key": app_key,
        "x-remote-user-id": '0'
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for error HTTP statuses
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None