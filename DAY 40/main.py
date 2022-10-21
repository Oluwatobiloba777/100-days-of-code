# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

# objects
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
####destinations
destinations = {
    data["iataCode"]: {
        "id": data["id"],
        "city": data["city"],
        "price": data["lowestPrice"]
    } for data in sheetyData}

tomorrow = datetime.now() + timedelta(days=1)
sixMonthFromToday = datetime.now() + timedelta(days=(6 * 30))

for code in destinations:
    flight = flightSearch.checkFlights(
        ORIGIN_CITY_IATA, code, fromTime=tomorrow, toTime=sixMonthFromToday
    )
    print(flight.price)
    if flight is None:
        continue
    if flight.price < destinations[code]["price"]:
        users = dataManager.customerEmails()
        emails = [row["email"] for row in users]
        names = [row["firstName"] for row in users]
        message = f"Low price alert! only N{flight.price} to fly from {flight.originCity}-{flight.originAirport} to {flight.destinationCity}-{flight.destinationAirport}, from {flight.outDate} to {flight.returnDate}."

        if flight.stopOver > 0:
            message += f"\n Flight has {flight.stopOver} stop over, via {flight.viaCity}."
            link = f"https://www.google.com/flights?hl=en#flt={flight.originAirport}.{flight.destinationAirport}.{flight.outDate}*{flight.destinationAirport}.{flight.originAirport}.{flight.returnDate}"

            notifyManager.sendEmail(emails, message, link)
