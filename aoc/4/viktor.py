def checkwinnings(winningnr, lotterynr):
    points = 0
    for n in lotterynr:
        if n in winningnr and n != "":
            points += 1
    return points

def countcards(winnings):
    for win in winnings.keys():
        indexStart = list(winnings.keys()).index(win) + 1
        for n in range(indexStart, indexStart + int(winnings.get(win))):
            cards[list(winnings.keys())[n]] += cards.get(win)
    

cards = {}
winnings = {}

with open('input.txt') as f:
    lines = f.readlines()

total = 0 
for line in lines:
    cardNumbers = line.split(":")
    numbers = cardNumbers[1].split("|")
    winningnr = numbers[0].strip().split(" ")
    lotterynr = numbers[1].strip().split(" ")
    points = checkwinnings(winningnr, lotterynr)
    winnings[cardNumbers[0]] = points


for win in winnings.keys():
    cards[win] = 1

countcards(winnings)


for card in cards:
    total += cards.get(card)

#print(lotterynr)

#print(points)
print(total)
