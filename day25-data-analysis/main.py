# import csv

# temperatures = []
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     for row in data:
#         if row[1] !="temp":
#             temperatures.append(row[1])

# print(temperatures)


import pandas
# read files using pandas
data = pandas.read_csv("weather_data.csv")

#get data in column
print(data["temp"])

#get data in row
print(data[data.day == "Monday"])

#calculate max in a column
print(data["temp"].max())

#use mean and other functions
print(data["temp"].mean())

#get individual values
monday_data = data[data.day == "Monday"]
monday_temp = monday_data.temp
print(monday_temp)

#create a dataframe from dict
data_dict = {
    "students":["james","mark", "angela"],
    "scores" : [76,89,98]
}

data = pandas.DataFrame(data_dict)
print(data)