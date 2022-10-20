#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

#objects
dataManager = DataManager()
sheetyData = dataManager.sheetData()
flightSearch = FlightSearch()
notifyManager = NotificationManager


ORIGIN_CITY_IATA = "LON"


if sheetyData[0]["iataCode"] == "":
    for row in sheetyData:
        row["iataCode"] = flightSearch.get_destination_code(row["city"])
    dataManager.sheetData = sheetyData
    dataManager.sheetUpdate()

tomorrow = datetime.now() + timedelta(days=1)
sixMonthFromToday = datetime.now() + timedelta(days=(6 * 30))

for destination in sheetyData:
    flight = flightSearch.checkFlights(
        ORIGIN_CITY_IATA, destination["iataCode"], fromTime= tomorrow,toTime=sixMonthFromToday
    )

    if flight.price < destination["lowestprice"]:
        notifyManager.send_sms(
            message=f"Low price alert! only N{flight.price} to fly from {flight.originCity}-{flight.originAirport} to {flight.destinationCity}-{flight.destinationAirport}, from {flight.outDate} to {flight.returnDate}."
        )