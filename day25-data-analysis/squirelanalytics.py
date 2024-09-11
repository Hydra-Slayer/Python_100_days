import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

# print(data.keys())

gray_squirrels = data[data["Primary Fur Color"] == "Gray"]
print(len(gray_squirrels))

cin_squirrels = data[data["Primary Fur Color"] == "Cinnamon"]
print(len(cin_squirrels))

black_squirrels = data[data["Primary Fur Color"] == "Black"]
print(len(black_squirrels))


data_dict = {
    "Primary Fur Color" : ["Gray","Cinnamon", "Black"],
    "Count": [len(gray_squirrels), len(cin_squirrels),len(black_squirrels)]
}

dataframe = pandas.DataFrame(data=data_dict)

dataframe.to_csv("squirrel_count.csv")