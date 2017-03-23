import math

i = 2
X = int(raw_input("Enter an integer: "))
isPrime = True
while i < int(math.sqrt(X)):
    if X % i == 0:
        isPrime = False
        break
    i += 1
if isPrime:
    print X," is prime"
else:
    print X," is not prime"
