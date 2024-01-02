cards = {}
ticketsAndWinners = []
with open('input.txt') as openfileobject:
    cardcounter = 0
    for line in openfileobject:
        cardcounter += 1
        cards[cardcounter] = 0 
        winner = line.split("|")[0].split()[2:]
        ticket = line.split("|")[1].split()
        ticketsAndWinners.append([ticket]+[winner])

def countWinners(row):
    matches = 0
    for t in ticketsAndWinners[row][0]:
        if t in ticketsAndWinners[row][1]:
            matches += 1
    return matches

for idx,c in enumerate(cards):
    cnt = cards[c]
    nrOfCardsToIncrement = countWinners(idx)
    for i in range(1+cnt):
        for n in range(nrOfCardsToIncrement):
            try:
                cards[idx+n+2] += 1
            except:
               pass 
totalsum = 0
for c in cards:
    totalsum += 1
    totalsum += cards[c]
print(totalsum)


x = [1,2,3]
