def transform(list1,list2,r1,r2):
    slice1 = sorted(list1[r1:r2])
    slice1.reverse()
    for s in slice1:
        list2.append(s)
    for i in range(r1,r2):
        list1.pop(r1)
    print list1
    return list2
