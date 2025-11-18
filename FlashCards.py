import random
import sys
import os
import json


def displayCards():
	reshuffle = ""
	cards = list(card_dict["cards"].values())
	if input("if you would only like to do the last 5 cards type 1\nif not just press enter\n\n") == "1":
		cards = cards[-5:]
	if input("if you would only like to shuffle your cards type 1\nif not just press enter\n\n") == "1":
		random.shuffle(cards)
		reshuffle = "1"
	x = ""
	while x == "":
		for i in range(len(cards)):
			os.system('cls')
			print(cards[i]["J"])
			print("\n\n")
			input("press enter to see the other side of the card")
			os.system('cls')
			print(cards[i]["E"])
			print("\n\n")
			input("press enter to see the next card")
		os.system('cls')
		x = input("press enter to redo the flash cards\ntype anything to exit\n\n")
		os.system('cls')
		if reshuffle == "1":
			random.shuffle(cards)

with open('cards.json', 'r', encoding='utf-8') as FH:
	data = FH.read()
	card_dict = json.loads(data)

	
displayCards()













#Random things held over from testing just incase I need them later

#cards = list(card_dict["cards"].values())
#random.shuffle(cards)
#print(cards[1]["J"])
#print(cards[1]["E"])
#input()

#cards = list(card_dict["cards"].values())
#random.shuffle(cards)

#input()


"""
	for card in card_dict["cards"].values():
		os.system('cls')
		print(card["J"])
		print("")
		print("")
		print("")
		input("press enter to see the other side of the card")
		os.system('cls')
		print(card["E"])
		print("")
		print("")
		print("")
		input("press enter to see the next card")




def shuffledCards():
	cards = list(card_dict["cards"].values())
	random.shuffle(cards)
	for i in range(len(cards)):
		os.system('cls')
		print(cards[i]["J"])
		print("")
		print("")
		print("")
		input("press enter to see the other side of the card")
		os.system('cls')
		print(cards[i]["E"])
		print("")
		print("")
		print("")
		input("press enter to see the next card")
		
"""
