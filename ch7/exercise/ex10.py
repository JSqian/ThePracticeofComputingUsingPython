def deleteEvens(list1):
    for num in list1:
        if num % 2 == 0:
            list1.remove(num)
    return list1

def deleteOdds(list1):
    for num in list1:
        if num % 2 == 1:
            list1.remove(num):
    return list1

def deleteNum(list1,isOdd):
    if isOdd:
        return deleteOdds(list1)
    else:
        return deleteEvens(list1)
