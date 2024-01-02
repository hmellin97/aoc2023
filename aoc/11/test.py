freq = [2000,3000,4000,5000,6000,7000,8000,9000,10000,11000,12000]
for f in freq:
    print(abs(f)-10000)
    if(abs(f-10000) <= 1):
        print("hejjj")
    else:
        print("nej")
