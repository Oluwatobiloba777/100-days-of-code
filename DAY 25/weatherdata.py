

import pandas as pd

# data = pd.read_csv("weather_squirrel_data.csv")
# # print(data["temp"])
#
# #to covert to dictionary
#
# # dataDict = data.to_dict()
# # print(dataDict)
#
#
# tempList = data["temp"].to_list()
#
# maxTemp = data["temp"].max()
#
# #Get data in rows
# print(data[data.temp == maxTemp])

data = pd.read_csv("squirrel_count.csv")
graySquirrels = len(data[data["Primary Fur Color"] == "Gray"])
cinnamonSquirrels = len(data[data["Primary Fur Color"] == "Cinnamon"])
blackSquirrels = len(data[data["Primary Fur Color"] == "Black"])
dataDict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [graySquirrels, cinnamonSquirrels, blackSquirrels]
}
squirrelsData = pd.DataFrame(dataDict)
squirrelsData.to_csv("Squirrels Count.csv")



