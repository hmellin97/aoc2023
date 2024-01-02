rejs = {}
t = input().split()
d = input().split()
print(t)
rejs[t[1]] = d[1]
rejs[t[2]] = d[2]
rejs[t[3]] = d[3]
rejs[t[4]] = d[4]
bigrejs = {}
bigtime = int(str(t[1])+str(t[2])+str(t[3])+str(t[4]))
bigdist = int(str(rejs[t[1]])+str(rejs[t[2]])+str(rejs[t[3]])+str(rejs[t[4]]))
bigrejs[bigtime] = bigdist
print("bigtime + " + str(bigtime))
print("bigdist + " + str(bigdist))

totalWaysToWin = []
for r in bigrejs:
    record = bigrejs[r]
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
