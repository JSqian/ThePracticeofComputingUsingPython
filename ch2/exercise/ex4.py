topNum = int(raw_input("What is the upper number for the range:"))
topNum = int(topNum)
theNum = 2
while theNum < topNum:
    divisor = 2
    sumOfDivisors = 1
    while divisor**2 < theNum:#improve the algorithm
        if theNum % divisor == 0:
            sumOfDivisors = sumOfDivisors + divisor + theNum / divisor
        divisor += 1
        
    # classify the number based on its divisor sum
    if theNum == sumOfDivisors:
        print theNum,"is perfect"
    elif theNum < sumOfDivisors:
        print theNum,"is abundant"
    else:
        print theNum,"is deficient"
    theNum += 1
