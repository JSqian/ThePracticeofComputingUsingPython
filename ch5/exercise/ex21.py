def showNum(A,B):
    setNums = "13489"
    if A > B:
        A,B = B,A
    count = 0
    for num in range(A,B+1):
        isShow = True
        for i in str(num):
            if not i in setNums:
                isShow = False
        else:
            if isShow:
                if count % 10 == 0:
                   print
                count += 1
                print num,
