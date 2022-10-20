import requests


SHEETY_ENDPOINT = "SHEETY ENDPOINT"



class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.sheetyData = {}

    def sheetData(self):
        sheetResponse = requests.get(url="SHEET ENDPOINT")
        sheetResponse.raise_for_status()
        data = sheetResponse.json()
        self.sheetyData = data['prices']

        return self.sheetyData

    #this updates the google sheet

    def sheetUpdate(self):
        for destination in self.sheetyData:
            newData = {
                "price": {
                    "iataCode": destination["iataCode"]
                }
            }
            sheetResponse = requests.put(url=f"{SHEETY_ENDPOINT}/{destination['id']}", json=newData)
            print(sheetResponse.text)