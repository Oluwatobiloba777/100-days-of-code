import requests
from datetime import datetime


#pixela api endpoint
PIXELA_ENDPOINT = "https://pixe.la/v1/users"
TOKEN = "CREATEYOUROWNTOKEN"
USERNAME = "YOUR USERNAME"
GRAPH_ID = "graph1"
usersParams = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}


userResponse = requests.post(url=PIXELA_ENDPOINT, json=usersParams)
# to test if user has been created successfully{it should return a success message in json format}
# print(userResponse.json())


#pixela graph
GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"

graphConfig = {
    "id": GRAPH_ID,
    "name": "Reading Graph",
    "unit": "Hr",
    "type": "float",
    "color": "ajisai",
}
#this is required for authorisation
headers = {
    "X-USER-TOKEN": TOKEN,

}

graphResponse = requests.post(url=GRAPH_ENDPOINT, json=graphConfig, headers=headers)
#to test if the graph response is working
# print(graphResponse.text)

today = datetime(year=2020, month=10, day=17)


#creating a pixel graph for user
PIXEL_CREATION_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"
pixelData = {
    "date":today.strftime("%Y%m%d"),
    "quantity": input("How many hours did you read today? "),
}

pixelResponse = requests.post(url=PIXEL_CREATION_ENDPOINT, json=pixelData, headers=headers)
#to test if pixel response is working
# print(pixelResponse.text)


#the pixel put request for updating
UPADATE_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

newPixelData = {
    "quantity": "2.3"
}

updateResponse = requests.put(url=UPADATE_ENDPOINT, json=newPixelData, headers=headers)
#to test if update response is working
# print(updateResponse.text)

#delete a pixel graph
DELETE_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
deleteResponse = requests.delete(url=DELETE_ENDPOINT, headers=headers)