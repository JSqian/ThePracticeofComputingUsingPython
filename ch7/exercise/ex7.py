def checkPuzzle(str1,str2):
    list1 = sorted(str1)
    list2 = sorted(str2)
    if list1 == list2:
        return True
    else:
        return False
    

def main():
    str1 = raw_input("Enter the first word")
    str2 = raw_input("Enter the second word")
    res = checkPuzzle(str1,str2)
    print res
