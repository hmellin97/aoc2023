universe = []
with open('input.txt') as openfileobject:
    for line in openfileobject:
        universe.append(list(line.rstrip()))
def pu():
    for u in universe:
        for uu in u:
            print(uu, end="")
        print("")
emptyRows = []
emptyColumns = []

rowCount = 0
#pu()
for u in universe:
    #print(u)
    if "#" not in u:
        print("davinki")
        emptyRows.append(rowCount)
    rowCount += 1

columnCount = 0
for u in zip(*universe):
    if "#" not in u:
        emptyColumns.append(columnCount)
    columnCount += 1

#print("ec")
#print(emptyColumns)
for e in emptyRows:
    print(e)

offset = 0
for ec in emptyColumns:
    for u in universe:
        u.insert(ec+offset,".")
    offset += 1
counta = 1
coords = {}
emptyRows = list(map(lambda x: x+1, emptyRows))
for er in emptyRows:
    universe.insert(er,["."]*len(universe[0]))
    emptyRows = list(map(lambda x: x+1, emptyRows))
print(f"universeLength is {len(universe[0])}")


for y,u in enumerate(universe):
    for x,uu in enumerate(u):
        if uu is "#":
            #print(counta)
            coords[counta] = [x,y] 
            counta += 1 


def manhattan_distance(x1, y1, x2, y2):
    #print("comparing coord [" + str(x1) + "," + str(y1) + "] with [" + str(x2) + "," + str(y2) + "]") 
    return abs(x2 - x1) + abs(y2 - y1)

pu()
summer = 0
pairs = 0

for k1, v1 in coords.items():
    shortest = 1000000
    for k2, v2 in coords.items():
        if k1 is k2:
            continue
        if k1 > k2:
            continue
        pairs += 1
        x1 = v1[0]
        y1 = v1[1]
        x2 = v2[0]
        y2 = v2[1]
#        print("comparing " + str(k1) + " with " + str(k2))
        dist = manhattan_distance(x1,y1,x2,y2)
 #       print("dist was " + str(dist))
        summer += dist
    
#print("compared " + str(pairs) + " pairs")
print(summer)
#for c in coords:
#    print(coords[c])
#    break


