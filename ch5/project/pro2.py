def find(someStr,subStr,start,end):
    for i in range(start,end + 1 - len(subStr) + 1):
        index = i
        cmpStr = someStr[index:index+len(subStr)]
        if cmpStr != subStr:
            continue
        elif cmpStr == subStr:
            return index
    return -1

def  multiFind(someStr,subStr,start,end):
    indexStr = ""
    i = find(someStr,subStr,start,end)
    while i != -1:
        indexStr += (str(i) + ",")
        i = find(someStr,subStr,i+1,end)
    else:
        indexStr = indexStr.rstrip(',')
        return indexStr
