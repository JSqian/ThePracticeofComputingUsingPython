'''
import itertools

def getExpression(operatorList,operandsList):
    # like '012' means '+-*'
    operatorPermutation = getPermutation(len(operatorList))
    # positions can insert operator is 1,2,3
    for i in range(1,4):
        explist = operandsList[:]
            

def getPermutation(allnum,count):
    numlist = [str(x) for x in range(allnum)]
    print numlist
    numStr = ''.join(numlist)
    plist = list(itertools.permutations(numStr,count))
    return plist

'''
'''
2,3,4,5 + - * / ** get 26
'''
'''
operatorList = ['+','-','*','/','**']
operandsList = ['2','3','4','5']
plist = getPermutation(len(operatorList),3)
print len(plist)
'''
