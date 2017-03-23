X = int(raw_input("Enter the end number:"))

for i in range(1,X+1):
    theSum = 0
    for j in range(1,i+1):
        theSum += j
    print theSum
