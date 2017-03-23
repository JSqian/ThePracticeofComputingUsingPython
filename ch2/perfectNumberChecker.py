# perfect number checker

# get a number to check
theNum = int(raw_input("Please enter a number to check:"))

# find and sum up the divisors
divisor = 1
sumOfDivisors = 0
while divisor < theNum:
    if theNum % divisor == 0:
        sumOfDivisors += divisor
    divisor += 1

#classify the result
if theNum == sumOfDivisors:
    print theNum,"is perfect"
else:
    print theNum,"is not perfect"
