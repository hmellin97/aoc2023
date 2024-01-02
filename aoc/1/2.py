count = 0
summer = 0
gooba = [
    {"f": "o","k": "one", "v":1},
    {"f": "t","k": "two", "v":2},
    {"f": "t","k": "three", "v":3},
    {"f": "f","k": "four", "v":4},
    {"f": "f","k": "five", "v":5},
    {"f": "s","k": "six", "v":6},
    {"f": "s","k": "seven", "v":7},
    {"f": "e","k": "eight", "v":8},
    {"f": "n","k": "nine", "v":9},
        ]

while True:
    count += 1
    val = input()
 #  val = "psdkpvjkzrs3sixfive"
    number1 = -1
    number2 = -1
    valcount = 0
    for v in val:
        valcount += 1
   #     print(v.isnumeric)
        if(v.isnumeric() and number1 is -1):
            number1 = v
        for g in gooba:
            if g["f"] is v:
               # print(val[valcount-1:valcount+4])
               # print(g["k"])
               # print(g["k"] in val[valcount-1:valcount+4])
               # print("")
                if g["k"] in val[valcount-1:valcount+(len(g["k"])-1)] and number1 is -1:
                    number1 = g["v"]
                    break
                elif g["k"] in val[valcount-1:valcount+(len(g["k"])-1)]:
                    number2 = g["v"]
                    break
        if(v.isnumeric() and number1 is not -1):
            number2 = v
    if(number2 is -1):
        number2 = number1
    print(val)
    print(number1)
    print(number2)
    print("")
    summer += int(str(number1)+str(number2))
   # if(count is 1):
   #     break
    print(summer)
    
    
