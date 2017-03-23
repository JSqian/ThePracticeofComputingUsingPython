import math

flag = b**2 - 4 * a * c
if flag == 0:
    print "One root %f" % (float(-b))
elif flag > 0:
    root1 = -b + math.sqrt(flag)/(2*a)
    root2 = -b - math.sqrt(flag)/(2*a)
    print "Two real roots %f and %f" % (root1,root2)
else:
    root1 = -b + math.sqrt(flag)j/(2*a)
    root2 = -b - math.sqrt(flag)j/(2*a)
    print "Two complex roots",root1,' and ',root2
