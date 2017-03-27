def structNumList(numList):
    newList = []
    mid = len(numList)/2
    if len(numList) % 2 == 0:
        for i in range(mid):
            res = numList[i] + numList[len(numList)-i-1]
            newList.append(res)
    else:
        for i in range(mid):
            res = numList[i] + numList[len(numList)-i-1]
            newList.append(res)
        newList.append(numList[mid])
    return newList
