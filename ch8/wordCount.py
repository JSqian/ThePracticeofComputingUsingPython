import string
import pylab
import numpy

def processLine(line,wcDict):
    line = line.strip()
    wordList = line.split()
    for word in wordList:
        if word != '--':
            word = word.lower().strip()
            word = word.strip(string.punctuation)
            addWord(word,wcDict)

def addWord(w,wcDict):
    if w in wcDict:
        wcDict[w] += 1
    else:
        wcDict[w] = 1

def prettyPrint(wcDict):
    valKeyList = []
    for key,val in wcDict.items():
        if val > 2 and len(key) > 3:
            valKeyList.append((val,key))
    valKeyList.sort(reverse=True)
    print '%-10s %10s' % ('Word','Count')
    print '_'*21
    for val,key in valKeyList:
        print '%-12s %3d' % (key,val)

def barGraph(wcDict):
    wordList = []

    for key,val in wcDict.items():
        if val > 2 and len(key) > 3:
            wordList.append((key,val))
    wordList.sort()
    keyList = [key for key,val in wordList]
    valList = [val for key,val in wordList]

    barWidth = 0.5
    xVals = numpy.arange(len(keyList))
    pylab.xticks(xVals+barWidth/2.0,keyList,rotation=45)
    pylab.bar(xVals,valList,width=barWidth,color='r')
    pylab.show()

def main():
    wcDict = {}
    fObj = open('gettysburg.txt','r')
    for line in fObj:
        processLine(line,wcDict)
    print 'Length of the dictionary:',len(wcDict)
    prettyPrint(wcDict)
    barGraph(wcDict)
