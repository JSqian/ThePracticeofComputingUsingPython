str1 = raw_input("The first string:")
str2 = raw_input("The second string:")
smallStr = ""
for index in range(len(str1)):
    if str1[index] < str2[index]:
        smallStr = str1
        break
    elif str1[index] > str2[index]:
        smallStr = str2
        break
    if index + 1 == len(str2):#str2 shorter than str1
        if len(str1) == len(str2):# equal strings
            smallStr = str1
        elif len(str1) > len(str2):
            smallStr = str2
        break

if index < len(str2) - 1:
    smallStr = str1

print smallStr
