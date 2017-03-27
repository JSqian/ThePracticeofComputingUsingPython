# Find a word with a single example of the vowels a,e,i,o,u in that order

dataFile = open("dictionary.txt","r")

def cleanWord(word):
    return word.strip().lower()

def getVowelsInWord(word):
    vowelStr = "aeiou"
    vowelsInWord = ""
    for char in word:
        if char in vowelStr:
            vowelsInWord += char
    return vowelsInWord

# main program
print "Find words containing vowels 'aeiou' in that order:"
for word in dataFile:
    word = cleanWord(word)
    if len(word) <= 6:
        continue
    vowelStr = getVowelsInWord(word)
    if vowelStr = "aeiou":
        print word
