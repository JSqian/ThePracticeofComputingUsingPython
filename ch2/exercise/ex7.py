numStr = ''
for i in range(1,10):
    numStr += str(i)
    theSum = 0
    theSum += (int(numStr)*8 + i)
    print numStr,' * ',8,' + ',i,' = ',theSum
print

numStr = ''
for i in range(1,10):
    numStr += str(i)
    theSum = 0
    theSum += (int(numStr)*9 + i + 1)
    print numStr,' * ',9,' + ',i+1,' = ',theSum
print

numStr = ''
for i in range(1,9):
    numStr += str(10 - i)
    theSum = 0
    theSum += (int(numStr)*9 + 8 - i)
    print numStr,' * ',9,' + ',8 - i,' = ',theSum
print
print

for i in range(1,10):
    digitStr = '1'
    digitStr *= i
    theSum = 0
    theSum += (int(digitStr))**2
    print digitStr,' * ',digitStr,' = ',theSum
    
