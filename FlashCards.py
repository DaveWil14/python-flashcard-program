import random
import sys
import os
import json
from operator import truediv

os.system('cls')

def displayCards():
	reshuffle = ""
	whichWord = 2
	cards = list(card_dict["cards"].values())
	amount = input("if you would only like to do a certian amount of your recent cards please type the amount you would like to do\nif not just press enter\n"+"\nin total you have "+str(len(cards))+" cards\n")
	if not (amount == ""):
		cards = cards[-int(amount):]
	if input("if you would only like to shuffle your cards type 1\nif not just press enter\n\n") == "1":
		random.shuffle(cards)
		reshuffle = "1"
	if input("if you would only like flip the cards to show you the english first type 1\nif not just press enter\n\n") == "1":
		whichWord = 1
	x = ""
	while x == "":
		for i in range(len(cards)):
			os.system('cls')
			if whichWord == 1:
				print(cards[i]["E"])
			else:
				print(cards[i]["J"])
			print("\ncard "+str(i+1)+" of "+str(len(cards))+"\n")
			input("press enter to see the other side of the card")
			os.system('cls')
			if whichWord == 1:
				print(cards[i]["J"])
			else:
				print(cards[i]["E"])
			print("\ncard "+str(i+1)+" of "+str(len(cards))+"\n")
			input("press enter to see the next card")
		os.system('cls')
		x = input("press enter to redo the flash cards\ntype anything to exit\n\n")
		os.system('cls')
		if reshuffle == "1":
			random.shuffle(cards)

def choosedeck():
    file = os.listdir()
    files = []
    for items in file:
        if items.endswith(".json"):
            files.append(items)
    x = 1
    y = 0
    print("please pick which set of flash cards (the number) you want to do\n")
    for items in files:
        print(x,items)
        x = x+1
    print("")
    while True:
        y = input("please make sure the number is between 1 and "+str(len(files))+":\n")
        if int(y) <= len(files) and int(y) >= 1:
            y = int(y) - 1
            return files[y]




deck = choosedeck()

with open(deck, 'r', encoding='utf-8') as FH:
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
