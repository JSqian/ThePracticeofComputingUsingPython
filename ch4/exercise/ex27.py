inputStr = raw_input("Enter the string:")
findCh = raw_input("Enter the character to find:")
index = 0
while index < len(inputStr):
    targetIndex = inputStr.find(findCh,index)
    if targetIndex == -1:
        break
    else:
        print targetIndex,
        index = targetIndex + 1
    
