def main():
    irisDict = {'setosa':{'sepal length':0,'sepal width':0,'petal length':0,'petal width':0},\
                'virginica':{'sepal length':0,'sepal width':0,'petal length':0,'petal width':0},\
                'versicolor':{'sepal length':0,'sepal width':0,'petal length':0,'petal width':0}\
                }
    countDict = {'setosa':0,'virginica':0,'versicolor':0}
    fObj = open('iris.txt','r')
    for line in fObj:
        processLine(line,irisDict,countDict)
    getResult(irisDict,countDict)
    print irisDict

def processLine(line,irisDict,countDict):
    irisList = line.strip().split(',')
    if len(irisList) == 1:
        return 
    if irisList[4] == "Iris-setosa":
        countDict['setosa'] += 1
        irisDict['setosa']['sepal length'] += float(irisList[0])
        irisDict['setosa']['sepal width'] += float(irisList[1])
        irisDict['setosa']['petal length'] += float(irisList[2])
        irisDict['setosa']['petal width'] += float(irisList[3])
    elif irisList[4] == "Iris-versicolor":
        countDict['versicolor'] += 1
        irisDict['versicolor']['sepal length'] += float(irisList[0])
        irisDict['versicolor']['sepal width'] += float(irisList[1])
        irisDict['versicolor']['petal length'] += float(irisList[2])
        irisDict['versicolor']['petal width'] += float(irisList[3])
    elif irisList[4] == "Iris-virginica":
        countDict['virginica'] += 1
        irisDict['virginica']['sepal length'] += float(irisList[0])
        irisDict['virginica']['sepal width'] += float(irisList[1])
        irisDict['virginica']['petal length'] += float(irisList[2])
        irisDict['virginica']['petal width'] += float(irisList[3])

def getResult(irisDict,countDict):
    irisDict['setosa']['sepal length'] /= countDict['setosa']
    irisDict['setosa']['sepal width']  /= countDict['setosa']
    irisDict['setosa']['petal length'] /= countDict['setosa']
    irisDict['setosa']['petal width']  /= countDict['setosa']

    irisDict['versicolor']['sepal length'] /= countDict['versicolor']
    irisDict['versicolor']['sepal width']  /= countDict['versicolor']
    irisDict['versicolor']['petal length'] /= countDict['versicolor']
    irisDict['versicolor']['petal width']  /= countDict['versicolor']

    irisDict['virginica']['sepal length'] /= countDict['virginica']
    irisDict['virginica']['sepal width']  /= countDict['virginica']
    irisDict['virginica']['petal length'] /= countDict['virginica']
    irisDict['virginica']['petal width']  /= countDict['virginica']

    
