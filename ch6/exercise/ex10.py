def myMin(listA):
    minVal = listA[0]
    for i in listA:
        if i < minVal:
            minVal = i
    return minVal

def myMax(listA):
    maxVal = listA[0]
    for i in listA:
        if i > maxVal:
            maxVal = i
    return maxVal

    
