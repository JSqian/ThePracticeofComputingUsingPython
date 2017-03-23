import math

numStr = raw_input("Enter an integer greater than 2: ")
while not numStr.isdigit and int(numStr) <= 2:
    print "Error,try again."
    numStr = raw_input("Enter an integer greater than 2: ")

count = 0
theNum = int(numStr)
while not theNum < 2:
    count += 1
    print "%d: %.3f" % (count,math.sqrt(theNum))
    theNum = math.sqrt(theNum)
