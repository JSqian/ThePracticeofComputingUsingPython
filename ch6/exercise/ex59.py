def ispalindrome(checkStr):
    for i in range(0,len(checkStr)/2):
        if checkStr[i] != checkStr[len(checkStr)-1-i]:
            return False
    return True

def get3P():
    ret = []
    for i in range(1,10):
        for j in range(0,10):
            expStr = str(i) + str(j) + str(i)
            ret.append(int(expStr))
    return ret


# main
list1 = [22,33,44,55,66,77,88,99]
list2 = get3P()
for i in list1:
    for j in list2:
        if i + j >= 1000 and ispalindrome(str(i+j)):
            print i+j,i,j
        
    
