import json
import os
os.system('cls')
file = os.listdir()
files = []
for items in file:
    if items.endswith(".json"):
        files.append(items)



def chooseFlashCards():
    x = 1
    y = 0
    print("please pick which set of flash cards (the number) you want to add to, or you can press enter to make a new set\n")
    for items in files:
        print(x,items)
        x = x+1
    print("")
    while True:
        y = input("please make sure the number is between 1 and "+str(len(files))+":\n")
        if y == "":
            break
        elif int(y) <= len(files) and int(y) >= 1:
            y = int(y) - 1
            break
    return y

decknum = chooseFlashCards()

def makeFlashCards(decknum):
    y = decknum
    deckname = ""
    if y != "":
        deckname = files[decknum]
        return deckname
    else:
        deckname = input("type the name of the deck of your new flash cards: ")+".json"
        deckholder = {"cards":{}}
        with open(deckname, 'w') as json_file:
            json.dump(deckholder, json_file, indent=4)
        return deckname


deck = makeFlashCards(decknum)

num = int(input("how many flash cards do you want to add(recomended amount is 5 or less): "))
for i in range(num):
    os.system('cls')
    newdata = {
		"E": input("type in your english word for card "+str(i+1)+" "),
		"J": input("type in your japanese word for card "+str(i+1)+" ")
		}
    os.system('cls')
    with open(deck, 'r', encoding='utf-8') as FH:
        data = json.load(FH)

    x = "card"+str(len(data["cards"])+1)
    data["cards"][x] = newdata

    with open(deck, 'w', encoding='utf-8') as FH:
        json.dump(data, FH, indent=4)

