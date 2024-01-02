instructions = {}
cunta = 0
with open('input.txt') as openfileobject:
    for line in openfileobject:
        goo =  line.split()
        instructions[cunta] = {"d":goo[0],"l":int(goo[1]), "c": goo[2]}
        #print(instructions[cunta]["Direction"])
        #print(instructions[cunta]["Length"])
        #print(instructions[cunta]["Color"])
        cunta += 1

dimensions = {"xMin":0,"xMax":0,"yMin":0,"yMax":0}
currX = 0
currY = 100
for i in instructions:
    c = instructions[i]
    #print(c["d"])    
    if c["d"] is "L":
       currX -= c["l"]

    if c["d"] is "R":      
       currX += c["l"]         

    if c["d"] is "D":
       currY -= c["l"]

    if c["d"] is "U":      
       currY += c["l"]         
    
    if currX > dimensions["xMax"]:
        dimensions["xMax"] = currX
   
    if currX < dimensions["xMin"]:
        dimensions["xMin"] = currX

    if currY > dimensions["yMax"]:
        dimensions["yMax"] = currY

    if currY < dimensions["yMin"]:
        dimensions["yMin"] = currY

rows = dimensions["xMax"]-dimensions["xMin"]+100
cols = dimensions["yMax"]-dimensions["yMin"]
print(rows)
print(cols)
diggo = [[0] * rows for _ in range(cols)]
def pd():
    for d in diggo:
       for dd in d:
           print(dd,end="")
       print("")
for x in range(0,rows):
    for y in range(0,cols):
        #print(f"X is {x}, Y is {y}")
        diggo[y][x] = "."
print(dimensions)
pd()
cx = 100
cy = 350
diggo[cy][cx] = "X"
edges = []
b = 0
for i in instructions:
    c = instructions[i]
    x1,y1 = cx,cy
    print(c)
    if c["d"] is "L":
       print("left")
       for m in range(0,c["l"]):
          b += 1
          cx -= 1
          diggo[cy][cx] = "X"

    if c["d"] is "R":      
       print("right")
       for m in range(0,c["l"]):
          b += 1
          cx += 1
          diggo[cy][cx] = "X"

    if c["d"] is "D":
       print("down")
       for m in range(0,c["l"]):
          b += 1
          cy += 1
          diggo[cy][cx] = "X"

    if c["d"] is "U":      
       print("up")
       for m in range(0,c["l"]):
          b += 1
          cy -= 1
          diggo[cy][cx] = "X"         
    x2,y2 = cx,cy
    edges.append([x1,y1,x2,y2])
print(edges[:10])
#pd() 

#print(rows)
#print(cols)
def ray_casting(y, x):
    # Count the number of intersections between the ray and the polygon edges
    intersection_count = 0

    # Iterate over each column of the matrix
    for e in edges:
        x1,y1,x2,y2 = e
        if (y < y1) != (y < y2) and x < x1 + ((y-y1)/(y2-y1))*(x2-x1):
            intersection_count += 1
    return intersection_count % 2 is 1
    
    # Check if the number of intersections is odd (point inside the polygon)

    return intersection_count % 2 == 1
#ray_casting(0,0)
#print(ray_casting(35,243))
#print(ray_casting(35,245))
i = 0
for y in range(cols):
   shouldFill = False
   xx = 0
   filled = 0
   intersects = 0
   for x in range(rows-2):
      if(ray_casting(y,x) and diggo[y][x] is "."):
         i += 1
         diggo[y][x] = "O"
   #print("i at brk " + str(i))
pd()
print(f"i is {i} b is {b}")
area = i + (b/2) -1 #Picks sats
print("area is " + str(area))
i = 0
b = 0
for y in range(cols):
   for x in range(rows):
      if diggo[y][x] is "O":
         i += 1
      if diggo[y][x] is "X":
         b += 1
print(f"i is {i} b is {b}")
area = i + (b/2) -1 #Picks sats
print("area is " + str(area))
