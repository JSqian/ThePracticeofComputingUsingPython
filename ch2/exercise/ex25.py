for i in range(1,10):
    for j in range(10):
        theNum = i * 10 + j
        square = theNum ** 2
        if square > 999:
            continue
        if(square % 100 == theNum):
            print theNum,
