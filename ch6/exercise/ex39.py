def makeWordList(gFile):
    '''Create a list of words from the file'''
    speech = [] # list of speech words

    for lineString in gFile:            # read file line by line
        lineList = lineString.split()   # split each line to a list of words
        for word in lineList:
            word = word.lower()
            word = word.strip('.,')
            if word != '--':
                speech.append(word)         # add words to list of speech words
    return speech

def makeTuple(wordList):
    i = 0
    tupleList = []
    while i < len(wordList):
        if i == len(wordList)-1:
            wordTuple = wordList[i],
        else:
            wordTuple = wordList[i],wordList[i+1]
        tupleList.append(wordTuple)
        i += 2
    return tupleList


gFile = open('gettysburg.txt','rU')
speech = makeWordList(gFile)
wordTuplst = makeTuple(speech)
print wordTuplst
