# # import csv
# #
# # with open("weather_data .csv") as data_file:
# #     data = csv.reader(data_file)
# #     temperatures= []
# #     for row in data:
# #         if row[1]!="temp":
# #             temperatures.append(int(row[1]))
# #     print(temperatures)
#
# import pandas as pd
#
# # data = pd.read_csv("weather_data .csv")
# # print(type(data))
# # print(type(data["temp"]))
#
# # data_dict = data.to_dict()
# # print(data_dict)
#
# # temp_list= data["temp"].to_list()
#
# # print(data["temp"].mean())
# # print(data["temp"].max())
# # # Get Data in Columns
# # print(data["condition"]) #Bu ve aşağıdaki aynı işi yapar
# # print(data.condition)
#
# #Get Data in Row
#
# # print(data[data.day=="Monday"])
# # print(data[data.temp == data.temp.max()])
#
# # monday = data[data.day=="Monday"]
# #
# # monday_temp = monday.temp[0]
# # print(monday.condition)
# # print(monday_temp*9/5 +32)
#
#
# # Create a dataframe from scratch
#
#
# data_dict = {
#     "students": ["Amy","James","Angela"],
#     "scores" : [76,56,65]
#
# }
#
# data = pd.DataFrame(data_dict)
# data.to_csv("new_data.csv")
from itertools import count

import pandas as pd

data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20241229.csv")

cinnamon_squirrel_count=len(data[data["Primary Fur Color"] =="Cinnamon"])
gray_squirrel_count=len(data[data["Primary Fur Color"] =="Gray"])
black_squirrel_count=len(data[data["Primary Fur Color"] =="Black"])

data_dict = {
    "Fur Color": ["Gray","Cinnamon","Black"],
    "Count":[gray_squirrel_count,cinnamon_squirrel_count,black_squirrel_count]
}

df = pd.DataFrame(data_dict)

df.to_csv("squirrel_cont.csv")
