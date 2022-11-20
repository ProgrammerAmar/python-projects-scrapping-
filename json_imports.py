import json

with open('friends_json.txt','r') as file:
	file_contents = json.load(file)

print(file_contents["data"][0])

cars = [
	{
	"name":"ford",
	"year":"1990"
	},
	{
	"name":"audi",
	"year":"1991"
	}
]

with open('cars_json.txt','w') as file:
	json.dump(cars,file)
	