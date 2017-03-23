
isPerfect = False
while not isPerfect:
    theNum = int(raw_input("Enter the number: "))
    divisor = 1
    sumOfDivisors = 0
    while divisor < theNum:
        if theNum % divisor == 0:
            sumOfDivisors = sumOfDivisors + divisor
        divisor += 1
            
    if theNum == sumOfDivisors:
        isPerfect = True
        print theNum,"is perfect"
