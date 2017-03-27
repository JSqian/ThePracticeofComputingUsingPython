# do not use the time module
def showBar():
    seconds = int(raw_input("Enter the seconds:"))
    timeSlice = seconds / 10
    for i in range(11):
        print "At %-5d secs:    " % (i*timeSlice),"X"*i

showBar()
