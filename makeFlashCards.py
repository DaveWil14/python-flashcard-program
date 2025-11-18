import random
import sys
import os
import json
for i in range(5):
	os.system('cls')
	newdata = {
		"E": input("type in your english word for card "+str(i+1)+" "),
		"J": input("type in your japanese word for card "+str(i+1)+" ")
		}
	os.system('cls')
	with open('cards.json', 'r', encoding='utf-8') as FH:
		data = json.load(FH)

	x = "card"+str(len(data["cards"])+1)
	data["cards"][x] = newdata

	with open('cards.json', 'w', encoding='utf-8') as FH:
		json.dump(data, FH, indent=4)

