topNum = int(raw_input("What is the upper number for the range:"))
topNum = int(topNum)
for theNum in range(2,topNum):
    sumOfDivisors = 0
    for divisor in range(1,theNum):
        if theNum % divisor == 0:
            sumOfDivisors = sumOfDivisors + divisor
        divisor += 1
        
    # classify the number based on its divisor sum
    if theNum == sumOfDivisors:
        print theNum,"is perfect"
    elif theNum < sumOfDivisors:
        print theNum,"is abundant"
    else:
        print theNum,"is deficient"
    theNum += 1
