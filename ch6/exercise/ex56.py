'''
(7,18),(8,17),(9,16)
'''
def getSquareDiffer(num):
    squarelist = [4,9,16,25]
    ret = []
    for i in squarelist:
        differ = i - num
        if differ > 0 and differ <= 18:
         ret.append(differ)
    return ret

def getAllSquareTuple(numlist):
    used = []
    squareTL = []
    for i in numlist:
        used.append(i)
        differlist = getSquareDiffer(i)
        for di in differlist:
            if di > i:
                tu = i,di
                squareTL.append(tu)
    return squareTL

def printPartNumber(unTuplelist,checkNum):
    for tu in unTupleList:
     if tu[0] == checkNum:
        check = tu[1]
        flag = True
        for j in unTupleList[unTupleList.index(tu)+1:]:
            if j[0] == check or j[1] == check:
                flag = False
                break
        if flag:
            print check
            break
    


unsure = [1,2,3,4,5,6,7,8,910,11,12,13,14,15,16,17,18]
unTupleList = getAllSquareTuple(unsure)
printPartNumber(unTupleList,1)
