import requests
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

endPoint = "API ENDPOINT ADDRESS"
apiKey = os.environ.get("YOUR API KEY")
#twilio
accountSID = "YOUR ACCOUNT SID"
authToken = os.environ.get("AUTH_TOKEN")

weatherParams = {
    "lat": 6.524379,
    "lon": 3.379206,
    "appid": apiKey,
    "exclude": "current,minutely,daily"
}

response = requests.get(endPoint, params=weatherParams)
response.raise_for_status()
data = response.json()
weatherSlice = data["hourly"][:12]

rain = False

for hourData in weatherSlice:
    conditionCode = hourData["weather"][0]["id"]
    if int(conditionCode) < 700:
        rain = True

if rain:
    proxyClient = TwilioHttpClient()
    proxyClient.session.proxies = {'https': os.environ['https_proxy']}

    client = Client(accountSID, authToken, http_client=proxyClient)
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an ☔ ",
        from_="YOUR TWILIO VIRTUAL NUMBER",
        to="YOUR TWILIO VERIFIED REAL NUMBER"
    )
    print(message.status)