import re
linez = {}
with open('input.txt') as openfileobject:
    for line in openfileobject:
        nombo = line.split(":")[:1]
        nombo = re.findall('\d+',nombo[0])
#        print(nombo[0])
        line = re.sub('.*:','', line)
        thingo = line.split(";")
        #print(thingo)
        linez[nombo[0]] = thingo

def regexboi(aaa):
    p1 = '(1[3-9]|[2-9]\d)\sred'
    p2 = '(1[4-9]|[2-9]\d)\sgreen'
    p3 = '(1[5-9]|[2-9]\d)\sblue'
    m1 = re.search(p1,aaa)
    m2 = re.search(p2,aaa)
    m3 = re.search(p3,aaa)
    if(bool(m1) or bool(m2) or bool(m3)):
        return True
    else:
        return False
summa = 0
for l in linez:
    print(linez[l])
    shudAdd = True
    for x in linez[l]:
        if(regexboi(x)) is True:
            shudAdd = False
    if(shudAdd is True):
        summa += int(l)        
print(summa)
