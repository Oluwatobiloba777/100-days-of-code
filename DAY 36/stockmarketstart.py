import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

#this will get the yesterday's stock prices
STOCK_KEY = ""

#news api key goes here
NEWS_KEY = ""

#twilio sid and auth token
TWILIO_SID = ""
AUTH_TOKEN = ""

    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
stockParameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_KEY,
}

response = requests.get(STOCK_ENDPOINT, params=stockParameters)
stockData = response.json()["Time Series (Daily)"]
dataList = [value for (key, value) in stockData.items()]
yDay = dataList[0]
yClosingPrice = yDay["4. close"]
print(yClosingPrice)
#TODO 2. - Get the day before yesterday's closing stock price
dayBeforeYData = dataList[1]
dayBeforeYClosingPrice = dayBeforeYData["4. close"]
print(dayBeforeYClosingPrice)
#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
positiveDifference = abs(float(yClosingPrice) - float(dayBeforeYClosingPrice))

#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
percentDifference = (positiveDifference / float(yClosingPrice)) * 100
print(percentDifference)
#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").
# if percentDifference > 5:
#     print("Get News")

    ## STEP 2: https://newsapi.org/
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
if percentDifference > 5:
    newParameters = {
        "apikey": NEWS_KEY,
        "qInTitle": COMPANY_NAME,
    }

    newsResponse = requests.get(NEWS_ENDPOINT, params=newParameters)
    newsData = newsResponse.json()["articles"]
#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation
    threeArticles = newsData[:3]

    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number.

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.
    articles = [f"Headline: {newsData['title']}. \nBrief: {newsData['description']}" for article in threeArticles]

#TODO 9. - Send each article as a separate message via Twilio.
    client = Client(TWILIO_SID, AUTH_TOKEN)
    for article in articles:
        message = client.messages.create(
            body=article,
            from_="YOUR TWILIO NUMBER",
            to="YOUR PHONE NUMBER"
        )


#Optional TODO: Format the message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

