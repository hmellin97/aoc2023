cards = {}
ranksToHandOut = 0
with open('input4.txt') as openfileobject:
    for line in openfileobject:
        line = line.split()
        cards[line[0]] = [line[1],0]
        ranksToHandOut += 1
import re
def find_hand(hand):
    occ = {}
    jokerCount = 0
    for h in hand:
        if not h in occ:
            occ[h] = 1
        else:
            occ[h] += 1
        if h is "J":
            jokerCount += 1
    sortedOcc = sorted(occ.items(), key=lambda x:x[1], reverse=True)
    print(sortedOcc[0])
    hand = ""
    #print(jokerCount)
    for idx,s in enumerate(sortedOcc):
        val = sortedOcc[idx][1]
        nextVal = -1 
        if len(sortedOcc)-idx > 1:
            nextVal = sortedOcc[idx+1][1]
        #print("val is " + str(val))
        #print("nextVal is " + str(nextVal))
        if val is 5 - jokerCount:
            return "5oak"
        if val is 4 - jokerCount:
            return "4oak"
        if val is 3 - jokerCount and nextVal is 2 - jokerCount:
            return "fh"
        if val is 3 - jokerCount:
            return "3oak"
        if val is 2-jokerCount and nextVal is 2-jokerCount:
            return "tp"
        if val is 2-jokerCount:
            return "p"
    #print("got here")
    return "hc"
hand_list = {}
for c in cards:
    hand = find_hand(c)
    #print(c)
    if not hand in hand_list:
        hand_list[hand] = [c]
    else:
        hand_list[hand].append(c)
print(hand_list)

stronkness = {'A': 14, 'K': 13, 'Q': 12, "J": 11, 'T': 10, '9': 9, '8':8, '7':7, '6': 6, '5': 5,
        '4': 4, '3': 3,'2':2,'1':1}
hand_stronkness = ["5oak","4oak","fh","3oak","tp","p","hc"]


for hs in hand_stronkness: #sort by strength
    if hs in hand_list: #if this strength exists
        templist = {}
        for hl in hand_list[hs]: # print all those combinations
            summer = 0
            powerOfTen = 10000000000 # FUCK MEEEEEEEEEEEEEEEEEEEEEEE
            for x in hl:
                #print(stronkness[x])
                #print(powerOfTen)
                summer += stronkness[x]*powerOfTen
                powerOfTen /= 100
            templist[hl] = summer
        templist = sorted(templist.items(), key=lambda x:x[1], reverse=True)
        for t in templist:
            #print(cards[t[0]][0])
            cards[t[0]][1] = ranksToHandOut
            ranksToHandOut -= 1
        #print(templist)
finalSum = 0
#print(cards)
count = 0
for c in cards:
    count += 1
    bid = cards[c][0]
    rank = cards[c][1]
    if rank is 1:
        print(rank)
        print(c)
    if rank is 2:
        print(rank)
        print(c)
    if rank is 3:
        print(rank)
        print(c)
    finalSum += (int(bid)*int(rank))
print(finalSum)






































