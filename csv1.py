
# data = pandas.read_csv("weather_data.csv")
# type(data)
# print(data)
# data_dict = data.to_dict()
# print(data)

# temp_list = data["temp"].to_list()
# print(len(temp_list))
# sum(temp_list)
# average_temp = sum(temp_list)/len(temp_list)
# print(average_temp)
# print(data["temp"].mean())
# print(data["temp"].max())
# print(data[data.temp == data.temp.max()])
# print(data.day)

import pandas
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray = len(data[data["Primary Fur Color"] == "Gray"])
black = len(data[data["Primary Fur Color"] == "Black"])
cinnamon = len(data[data["Primary Fur Color"] == "Cinnamon"])
print(gray)
print(black)
print(cinnamon)
data_dict = {"Fur Color": ["Gray", "Cinnamon", "Black"],
             "Count": [gray, cinnamon, black]
             }
df = pandas.DataFrame(data_dict)
df.to_csv("Squirrel_count.csv")



