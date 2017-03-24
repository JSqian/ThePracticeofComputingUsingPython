originalStr = raw_input("Enter the string: ")
modifiedStr = ''
for char in originalStr:
    if char.isupper():
        mchar = chr(ord(char)+32)
        modifiedStr += mchar
    else:
        modifiedStr += char

print modifiedStr
