x = int(raw_input("Enter the number of record:"))
n = int(raw_input("Enter the number of rows in one page:"))
c = int(raw_input("Enter the columns of rows:"))
page = x / (n * c)
x = x - page * n * c
row = x / c
x = x - row * c
col = x
print "page %d,row %d,column %d" % (page,row,col)
