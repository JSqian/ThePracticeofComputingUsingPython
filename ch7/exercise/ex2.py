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

def makeUnique(speech):
    unique = []
    for word in speech:
        if word not in unique:
            unique.append(word)
    
    return unique

def printResult(speech):
    # print the speech and its length
    print "Speech Length: ",len(speech)
    unique = makeUnique(speech)
    print unique
    print "Unique Length: ",len(unique)

def main():
    gFile = open("gettysburg.txt","rU")
    speech = makeWordList(gFile)
    printResult(speech)


