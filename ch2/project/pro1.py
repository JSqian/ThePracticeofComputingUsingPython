count = 0
for i in range(65):
    count += 2**i

weight = count * 50 / 1000 / 1000 #KG
print "The total number is: ",count
print "The totoal weight is %d kg" % (weight)
