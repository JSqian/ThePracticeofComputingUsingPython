# algorithm to judge whether a number is
# in 2-20 and mod 3 = 0
numStr = raw_input("Enter an integer between 2 and 20:")
while not numStr.isdigit:
    print "Pay attention"
    numStr = raw_input("Enter an integer between 2 and 20:")
numInt = int(numStr)

if 2 <= numInt <= 20 and numInt % 3 == 0:
    print "yes"
else:
    print "no"
