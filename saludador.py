import os
import requests

url = os.getenv("WEATHER_URL", "https://weatherapi-com.p.rapidapi.com/current.json")
querystring = {"q":"10.46, -73.25"}
headers = {
    "X-RapidAPI-Key": "SIGN-UP-FOR-KEY",
    "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
}

def handler(event, context):

    response = requests.get(url, headers=headers, params=querystring)

    return {
        'statusCode': 200,
        'body': response.json()
    }
