def reverseSentence(senStr):
    senStr = senStr.lower()
    wordList = senStr.split()
    wordList.reverse()
    wordStr = ' '.join(wordList)
    return wordStr
    
