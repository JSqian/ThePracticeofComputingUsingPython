X = int(raw_input("Enter the end number:"))
theSum = 0

for i in range(1,X+1):
    theSum += i
if theSum % X == 0:
    print theSum
