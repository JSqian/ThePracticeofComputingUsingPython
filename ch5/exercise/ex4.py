import string

def cleanStr(enStr):
    modifiedStr = enStr.strip().lower()
    result = ''
    for i in modifiedStr:
        if i in string.lowercase:
            result += i
    return result

def vowelNum():
    originalStr = raw_input("Enter the string:")
    cleanedStr = cleanStr(originalStr)
    vowels = "aeiou"
    vowNum = 0
    consonantNum = 0
    for i in cleanedStr:
        if i in vowels:
            vowNum += 1
        else:
            consonantNum += 1
    print "The number of vowel is",vowNum,",the number of consonantNum is"\
          ,consonantNum

vowelNum()
    
