import re
directions = ""
graph = {}
count = 0
aBois = []
with open('input.txt') as openfileobject:
    for line in openfileobject:
        if "RRRR" in line:
            directions = line
        else:
            res = re.findall(r'\w+', line)
            graph[res[0]] = [res[1],res[2]]
            if re.search("..A",res[0]):
                aBois.append(res[0])
print(aBois)
print(len(aBois))
currentNode = "AAA"
directions *= 10000000
totalNodes = len(graph)
visitedNodes = []
#print(directions)
diff = 0
cycles = []
for a in aBois:
    currentNode = a
    print("Testing " + str(a))
    count = 0
    for d in directions:
        if re.search("..Z",currentNode):
            cycles.append(count)
            print("visisted " + currentNode + " at " + str(count))
            break
        if d is "L":
            count += 1
            currentNode = graph[currentNode][0]
        elif d is "R":
            count += 1
            currentNode = graph[currentNode][1]
        #print("Visited " + currentNode +  "for the first time at iteration " + str(count))
        visitedNodes.append(currentNode)
print(cycles)

def compute_lcm(x, y):

   # choose the greater number
   if x > y:
       greater = x
   else:
       greater = y

   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1
   return lcm
smallcycles = []
for c in cycles:
    smallcycles.append(c/271)
import math

def lcm_of_list(numbers):
    lcm_result = 1
    for num in numbers:
        lcm_result = lcm(lcm_result, int(num))
    return lcm_result

def lcm(x, y):
    return abs(x * y) // math.gcd(x, y)

temp = lcm(cycles[0],cycles[1])
print(temp)
temp = lcm(temp,cycles[2])
print(temp)
temp = lcm(temp,cycles[3])
print(temp)
temp = lcm(temp,cycles[4])
print(temp)
temp = lcm(temp,cycles[5])
print(temp)


'''
for idx,c in enumerate(smallcycles):

    if idx is 0:
        continue
    print("L " + str(lcm))
    print("S " + str(smallcycles[idx+1]))
    try:
        lcm = compute_lcm(lcm,smallcycles[idx+1])
        lcm /= 67
        print("lcm is " + str(lcm))
    except:
        pass
print(lcm)
#print(compute_lcm(cycles[0],cycles[5]))

'''












