# My Weather Alert Automation bot using Python
# SMS Automated using Twilio

import requests
import os
from twilio.rest import Client 
from twilio.http.http_client import TwilioHttpClient

api_key = "THE API KEY"
account_sid = "TWILIO ACCOUNT SID"
auth_token = "TWILIO AUTH TOKEN"
parameters = {
    "lat":"YOUR LOCATION'S LATITUDE",
    "lon":"YOUR LOCATION'S LONGTITUDE",
    "exclude":"daily",
    "appid":api_key
}
response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall",params=parameters)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]
will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code)<=700:
        will_rain = True

if(will_rain):
    #proxy_client = TwilioHttpClient()
    #proxy_client.session.proxies = {'https': os.environ['https_proxy']}
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        to="YOUR NUMBER", 
        from_="TWILIO NUMBER",
        body="Bring an Umbrella !"
    )
    print(message.status)
