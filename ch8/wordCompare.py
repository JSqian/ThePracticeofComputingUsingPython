import string

def addWord(w,theSet):
    '''Add the word to the set. No word smaller than length 3.'''
    if len(w) > 3:
        theSet.add(w)

def processLine(line,theSet):
    '''Process the line to get lowercase words to be added to the set.'''
    line = line.strip()
    wordList = line.split()
    for word in wordList:
        # ignore the '--' that is in the file
        if word != '--':
            word = word.strip()
            word = word.strip(string.punctuation)
            word = word.lower()
            addWord(word,theSet)

def main():
    '''Compare the Gettysburg Address and the Declaration of Independence.'''
    GASet = set()
    DoISet = set()
    GAFileObj = open('gettysburg.txt')
    DoIFileObj = open('declOfInd.txt')
    for line in GAFileObj:
        processLine(line,GASet)
    for line in DoIFileObj:
        processLine(line,DoISet)
    prettyPrint(GASet,DoISet)

def prettyPrint(gaSet,doiSet):
    print 'Count of unique words of length 4 or greater'
    print 'Gettysburg Addr: %d,Decl of Ind: %d\n' % (len(gaSet),len(doiSet))
    print '%15s %15s' % ('Operation','Count')
    print '-'*35
    print '%15s %15d' % ('Union',len(gaSet.union(doiSet)))
    print '%15s %15d' % ('Intersection',len(gaSet.intersection(doiSet)))
    print '%15s %15d' % ('Sym Diff',len(gaSet.symmetric_difference(doiSet)))
    print '%15s %15d' % ('GA-DoI',len(gaSet.difference(doiSet)))
    print '%15s %15d' % ('DoI-GA',len(doiSet.union(gaSet)))

    intersectionSet = gaSet.intersection(doiSet)
    wordList = list(intersectionSet)
    wordList.sort()
    print '\n Common words to both'
    print '-'*20
    cnt = 0
    for w in wordList:
        if cnt % 5 == 0:
            print
        print '%13s' % (w),
        cnt += 1









    
    
