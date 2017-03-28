def readInt(prompt):
    numStr = raw_input(prompt)
    while not isDigit(numStr):
        print 'Not a valid integer,try again'
        numStr = raw_input(prompt)
    return int(numStr)
                      
