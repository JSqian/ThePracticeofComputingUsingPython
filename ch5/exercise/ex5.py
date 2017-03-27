def showAllFib(n):
    for i in range(n):
        showNthFib(i+1)

def showNthFib(n):
    n1 = 1
    n2 = 1
    if n == 1:
        print n1,
    elif n == 2:
        print n2,
    else:
        i = 3
        while i <= n:
            num = n1 + n2
            n1 = n2
            n2 = num
            i += 1
        print num,
                        
            
