def palindrome(checkStr):
    length = len(checkStr)
    for i in range(length/2):
        if checkStr[i] != checkStr[length-1-i]:
            return False
    return True
        
    
