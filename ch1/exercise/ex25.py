#print the time in hour,minute,second
secondStr = raw_input("Enter the time in seconds(1-86400):")
seconds = int(secondStr)
hour = seconds / (60 * 60)
seconds = seconds - hour * 60 * 60
minute = seconds / 60
seconds = seconds - minute * 60
print "%d hour,%d minute,%d seconds" % (hour,minute,seconds)
