import pandas


data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
data_dict = data.to_dict()
gray= 0
cinnamon = 0
black = 0
cinnamon = len(data[data["Primary Fur Color"] == "Cinnamon"])

gray = len(data[data["Primary Fur Color"] == "Gray"])

black = len(data[data["Primary Fur Color"] == "Black"])

#print (f"Cinnamon = {cinnamon} \n Gray = {gray} \n Black = {black}")
new_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray, cinnamon, black]
}
data11 = pandas.DataFrame(new_dict)
data11.to_csv("squirrel_color_data.csv")