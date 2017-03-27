def moveL(olist,k):
    modilist = olist[:]
    storelist = modilist[:k]
    #print storelist
    for i in range(k,len(modilist)):
        modilist[i-k] = modilist[i]
    storeIndex = 0
    for i in range(len(modilist)-k,len(modilist)):
        modilist[i] = storelist[storeIndex]
        storeIndex += 1
    return modilist
    
def moveR(olist,k):
    modilist = olist[:]
    storelist = modilist[len(olist)-k:]
    print storelist
    for i in range(len(modilist)-k-1,-1,-1):
        modilist[i+k] = modilist[i]
    
    storeIndex = 0
    for i in range(len(modilist)-k-1):
        #print (i,storeIndex)
        modilist[i] = storelist[storeIndex]
        storeIndex += 1
        
    return modilist
