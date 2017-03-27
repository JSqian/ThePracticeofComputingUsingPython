def countHole(word):
    holeSet = 'abdegopq'
    upperHoleSet = 'ABDGOPQ'
    count = 0
    for i in word:
        if i in holeSet or i in upperHoleSet:
            count += 1
    return count

def showTwoHoleWord(wordlist):
    for word in wordlist:
        if countHole(word) >= 2:
            print word
