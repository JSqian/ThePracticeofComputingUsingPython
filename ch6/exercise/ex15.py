def genList(listA):
    resList = []
    for i in range(len(listA)):
        glist = listA[-1-i:]
        resList.append(glist)
    
    return resList 
