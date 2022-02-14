# My Weather Alert Automation bot using Python
# SMS Automated using Twilio

import requests
import os
from twilio.rest import Client 
from twilio.http.http_client import TwilioHttpClient

api_key = "e476c0984403f0f81fd86e758b52c235"
account_sid = "AC4dc7e5a723d650f89ade64ad79f8054c"
auth_token = "cf7d57a12a7eb5b7dc78404c0f285dec"
parameters = {
    "lat":13,
    "lon":80,
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
        to="+918870166755", 
        from_="+18126338878",
        body="Bring an Umbrella !"
    )
    print(message.status)
