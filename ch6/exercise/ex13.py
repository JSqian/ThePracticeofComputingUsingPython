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

def makeCount(speech):
    unique = []
    wordAndCount = []
    for word in speech:
        if word not in unique:
            count = 0
            for word1 in speech:
                if word == word1:
                    count += 1
            unique.append(word)
            wordTuple = word,count
            wordAndCount.append(wordTuple)
    
    return wordAndCount

def sortedWordList(tupleList):
    sortedList = []
    
    #select sort
    for i in range(len(tupleList)-1):
        for j in range(i+1,len(tupleList)):
            if tupleList[j][1] > tupleList[i][1]:
                tupleList[i],tupleList[j] = tupleList[j],tupleList[i]

    for t in tupleList:
        sortedList.append(t[0])
    
    return sortedList
    

####################
gFile = open("gettysburg.txt","rU")
speech = makeWordList(gFile)

wordAndCount = makeCount(speech)
sortedWordList = sortedWordList(wordAndCount)
print wordAndCount
print sortedWordList

