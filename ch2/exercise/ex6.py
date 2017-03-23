numStr = raw_input("Input an integer: ")

while not numStr.isdigit():
    print "Error: try again. ",
    numStr = raw_input("Input an integer: ")
else:
    print "The integer is %d" % (int(numStr))
