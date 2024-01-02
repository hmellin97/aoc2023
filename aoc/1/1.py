count = 0
summer = 0

while True:
    count += 1
    val = input()
    number1 = -1
    number2 = -1
    for v in val:
        if(v.isnumeric() and number1 is -1):
            number1 = v
        elif(v.isnumeric()):
            number2 = v
    if(number2 is -1):
        number2 = number1
    summer += int(str(number1)+str(number2))
    print(summer)
    
    
