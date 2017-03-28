myDict = {'a':15,'b':20,'c':35}

keyLst = myDict.keys()
valLst = myDict.values()
keyVallist = myDict.items()

print keyLst
print valLst
print keyVallist
keyVallist.sort()
print keyVallist

valkeylst = []
for key,val in keyVallist:
    valkeylst.append((val,key))
valkeylst.sort()
print valkeylst
