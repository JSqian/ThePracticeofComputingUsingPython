def genList(ListA):
    ListB = []
    for index in range(len(ListA)):
        if index == 0:
            ListB[index] = ListA[0] + ListA[1]
        elif index == len(ListA) - 1:
            ListB[index] = ListA[-1] + ListA[-2]
        else:
            ListB[index] = ListA[index-1] + ListA[index+1]

    return ListB
