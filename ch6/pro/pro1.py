def getTriangleList(height):
    if height == 1:
        return [[1]]
    elif height == 2:
        return [[1],[1,1]]
    else:
        listA = []
        listA.append([1])
        listA.append([1,1])
        for i in range(2,height):
            sub = []
            sub.append(1)
            for j in range(1,i):
                sub.append(listA[i-1][j-1]+listA[i-1][j])
            sub.append(1)
            listA.append(sub)
    return listA

# main
height =int(raw_input("Enter the height of triangle:"))
tlist = getTriangleList(height)
print tlist
