def getDataList(fileName):
    dataFile = open(fileName,"r")
    dataList = []
    for line in dataFile:
        # strip end-of-line,split on commas, and append items to list
        dataList.append(line.strip().split(','))
    return dataList

def getMonthlyAverages(dataList):
    monthlyAveragesList = []
    odate = dataList[1][0].split('-')
    volumeACLst = []
    for data in dataList[1:]:
        date = data[0].split('-')
        year,month = date[0],date[1]
        if year == odate[0] and month == odate[1]:
            pass
            #volumeAdjClose = (data[5],data[6])
            #volumeACLST.append(volumeAdjClose)
        else:
            averagePrice = getAveragePrice(volumeACLst)
            dateItem = odate[0]+"-"+odate[1]
            appendItem = (averagePrice,dateItem)
            monthlyAveragesList.append(appendItem)
            #clean data
            volumeACLst = []
            odate[0] = year
            odate[1] = month
            
        volumeAdjClose = (data[5],data[6])
        volumeACLst.append(volumeAdjClose)
    return monthlyAveragesList
    
def getAveragePrice(volumeACTupleLst):
    sumAll = 0
    volumeAll = 0
    for item in volumeACTupleLst:
        sumAll += float(item[0])*float(item[1])
        volumeAll += float(item[0])
    price = sumAll / volumeAll
    return price

# you can use sort() to improve this function but price should be the first
# in the tuple
def printInfo(monthlyAveragesList):
    '''
    highest = []
    lowest = []
    for i in range(6):
        highestPrice = getHighestPrice(monthlyAveragesList)
        lowestPrice = getLowestPrice(monthlyAveragesList)
        highest.append(highestPrice)
        lowest.append(lowestPrice) # list of tuple
    '''
    monthlyAveragesList.sort()
    print "%-15s %-15s" % ("Date","AveragePrice")
    monthlyAveragesList.reverse()
    for item in monthlyAveragesList[0:6]:
        print "%-15s %-15.2f" % (item[1],item[0])
    for item in monthlyAveragesList[-6:]:
        print "%-15s %-15.2f" % (item[1],item[0])
'''
# this method will change the list
def getHighestPrice(monthlyAveragesList):
    highestTuple = monthlyAveragesList[0]
    for tu in monthlyAveragesList:
        if tu[1] > highestTuple[1]:
            highestTuple = tu
    monthlyAveragesList.remove(highestTuple)
    return highestTuple
   
def getLowestPrice(monthlyAveragesList):
    lowestTuple = monthlyAveragesList[0]
    for tu in monthlyAveragesList:
        if tu[1] < lowestTuple[1]:
            lowestTuple = tu
    monthlyAveragesList.remove(lowestTuple)
    return lowestTuple
'''    

def main():
    dataList = getDataList("table.csv")
    printInfo(getMonthlyAverages(dataList))


    

