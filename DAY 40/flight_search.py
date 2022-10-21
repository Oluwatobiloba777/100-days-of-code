from pprint import pprint

import requests
from flight_data import FlightData


TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_API_KEY = "YOUR_API_KEY_HERE"

LOCATION_ENDPOINT = f"{TEQUILA_ENDPOINT}/locations/query"


class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def get_destination_code(self, city_name):
        # Return "TESTING" for now to make sure Sheety is working. Get TEQUILA API data later.
        headers = {"apikey": TEQUILA_API_KEY}
        query = {"term": city_name, "location_types": "city"}
        response = requests.get(url=LOCATION_ENDPOINT, headers=headers, params=query)
        result = response.json()["locations"]
        code = result[0]["code"]
        return code

    def checkFlights(self, originCityCode, fromTime, toTime, destinationCityCode):
        headers = {"apikey": TEQUILA_API_KEY}
        query = {
            "fly_from": originCityCode,
            "fly_to": destinationCityCode,
            "date_from": fromTime.strftime("%d/%m/%Y"),
            "date_to": toTime.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 14,
            "nights_in_dst_to": 30,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "USD"
        }

        response = requests.get(url=f"{TEQUILA_ENDPOINT}/v2/search", headers=headers, params=query)

        try:
            data = response.json()["data"][0]

        except IndexError:
            query["max_stopovers"] = 1
            response = requests.get(url=f"{TEQUILA_ENDPOINT}/v2/search",headers=headers, params=query)
            data = response.json()["data"][0]
            pprint(data)
            flightData = FlightData(
                price=data["price"],
                originCity=data["route"][0]["cityFrom"],
                originAirport=data["route"][0]["flyFrom"],
                destinationCity=data["route"][1]["cityTo"],
                destinationAirport=data["route"][1]["flyTo"],
                outDate=data["route"][0]["local_departure"].split("T")[0],
                returnDate=data["route"][2]["local_departure"].split("T")[0],
                stopOver=1,
                viaCity=data["route"][0]["cityTo"]
            )
            # print(f"No flights for {destinationCityCode} found")
            return flightData
        else:
            flightData = FlightData(
                price=data["price"],
                originCity=data["route"][0]["cityFrom"],
                originAirport=data["route"][0]["flyFrom"],
                destinationCity=data["route"][0]["cityTo"],
                destinationAirport=data["route"][0]["flyTo"],
                outDate=data["route"][0]["local_departure"].split("T")[0],
                returnDate=data["route"][1]["local_departure"].split("T")[0]
            )
            print(f"{flightData.destinationCity}: N{flightData.price}")
            return flightData