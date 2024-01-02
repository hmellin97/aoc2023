rejs = {}
t = input().split()
d = input().split()
print(t)
rejs[t[1]] = d[1]
rejs[t[2]] = d[2]
rejs[t[3]] = d[3]
rejs[t[4]] = d[4]
totalWaysToWin = []
for r in rejs:
    record = rejs[r]
    waysToWin = 0
    for windUpTime in range(int(r)):
        timeToRace = int(r)-windUpTime
        #print("timeToRace " + str(timeToRace))
        #print("windUpTime " + str(windUpTime))
        if (windUpTime*timeToRace > int(record)):
            waysToWin += 1
    totalWaysToWin.append(waysToWin)
result = 1
for twtw in totalWaysToWin:
    result *= twtw
print(result)
