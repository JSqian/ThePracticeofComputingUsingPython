import string

inputStr = "Chapman, Graham Arthur"
for char in inputStr:
    if char in string.punctuation:
        modifiedStr = inputStr.replace(char,'')

first,middle,last = modifiedStr.split()
resultStr = middle + ' ' + last + ' ' + first
print resultStr
