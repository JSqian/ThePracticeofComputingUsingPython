theStr = raw_input("Enter the string: ")
count = 0
outStr = ''
for i in theStr:
    count += 1
    if count % 3 == 0:
        outStr += i
print outStr

