# highest mileage data

def createMileageList(epaFile):
    mileageList = []
    for line in epaFile:
        if line[0:5] == 'CLASS' or 'VAN' in line or 'PICKUP' in line:
            continue
        lineList = line.split(',')
        # tuple (mileage,make,model)
        carTuple = (int(lineList[9]),lineList[1],lineList[2])
        mileageList.append(carTuple)
    return mileageList

def findMaxMinMileage(mileageList,maxMileage,minMileage):
    maxMileageList = []
    minMileageList = []

    for carTuple in mileageList:
        if carTuple[0] == maxMileage:
            maxMileageList.append(carTuple)
        if carTuple[0] == minMileage:
            minMileageList.append(carTuple)
    return maxMileageList, minMileageList

# open EPA data file
epaFile = open('epaData.csv','rU')

print "EPA Car Mileage"
print

mileageList = createMileageList(epaFile)

# find max and min mileage
maxMileage = max(mileageList)[0]
minMileage = min(mileageList)[0]

print "Max and Min Mileage: ",maxMileage,minMileage
print

maxMileageList,minMileageList = \
               findMaxMinMileage(mileageList,maxMileage,minMileage)

print "Maximum Mileage Cars:"
for carTuple in maxMileageList:
    print " ",carTuple[1],carTuple[2]
print "Minimun Mileage Cars: "
for carTuple in minMileageList:
    print " ",carTuple[1],carTuple[2]







