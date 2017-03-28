def ispalindrome(str1,str2):
    list1 = list(str1)
    list2 = list(str2)
    if list2.reverse() == list1:
        return True
    else:
        return False

def main():
    str1 = raw_input("Enter the first string:").lower().replace(' ','')
    str2 = raw_input("Enter the second string:").lower().replace(' ','')
    print ispalindrome(str1,str2)
