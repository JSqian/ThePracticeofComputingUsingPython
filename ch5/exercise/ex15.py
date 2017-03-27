def commonMulti(x,y,z):
    if x > y:
        x,y = y,x
    if y > z:
        print "check"
    else:
        for i in range(y,z+1,y):
            if i % x == 0 and i % y == 0:
                print i,
    
