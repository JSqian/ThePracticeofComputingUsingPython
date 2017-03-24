# Palindrome tester
import string

originalString = raw_input('Input a string:')
modifiedStr = originalString.lower()

badChars = string.whitespace + string.punctuation

for char in modifiedStr:
    if char not in badChars: # store good characters
        modifiedStr += char 

if modifiedStr == modifiedStr[::-1]: # it is a palindrome
    print \
'The original string is: %s\n\
 the modified string is: %s\n\
 the reversal is:        %s\n\
 String is a palindrome' % (originalString,modifiedStr,modifiedStr[::-1])
else:
    print\
'The original string is: %s\n\
 the modified string is: %s\n\
 the reversal is:        %s\n\
 String is not a palindrome' % (originalString,modifiedStr,modifiedStr[::-1])
