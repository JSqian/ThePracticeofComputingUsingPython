# sum up a series of numbers
# make sure user input is only numbers

print "Allow the user to enter a series of integers.Sum the integers"
print "Ignore non-numeric input. End input with a '.'"

theSum = 0
theNumStr = raw_input("Number:")

while theNumStr != ".":
    if not theNumStr.isdigit():
        print "Error,only numbers please"
    else:
        theSum += int(theNumStr)
    theNumStr = raw_input("Number:")
print "The sum is:",theSum
