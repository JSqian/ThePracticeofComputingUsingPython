import string

def isLeap(year):
    if year % 400 == 0:
        return True
    elif year % 4 == 0 and year % 100 != 0:
        return True
    else:
        return False

def checkOnlyNum(timeStr):
    goodChars = "/: "
    for i in timeStr:
        if i not in goodChars and not i.isdigit();
            return False
    return True

def checkMonth(monthStr):
    return 1<= int(monthStr) <= 12

def checkDay(yearStr,monthStr,dayStr):
    year = int(yearStr)
    month = int(monthStr)
    day = int(dayStr)
    has31 = monthStr in ("1 3 5 7 8 10 12".split())
    has30 = monthStr in ("4 6 9 11".split())
    if  day > 31:
        return False
    elif day == 31:
        if has31:
            return True
        else:
            return False
    elif day == 30:
        if has30:
            return True
        else:
            return False
    elif day == 29:
        if isLeap(year):
            return True
        else:
            return False
    else:
        return True


def printTime(timeStr):
    '''
    MM/DD/YYYY HR: MIN: SEC
    '''
    if not checkOnlyNum(timeStr):
        print "Invalid time string"
        return
    
    #check month
    monthF = timeStr.find('/')
    monthStr = timeStr[:monthF]
    if not checkMonth(monthStr):
        print "Invalid month"
        return

    #check day
    dayF = timeStr.find('/',monthF+1)
    dayStr = timeStr[monthF+1:dayF]
    yearF = timeStr.find(' ')
    yearStr = timeStr[dayF:yearF]
    if int(yearStr) <= 0:
        print "invalid year"
        return
    
    if not checkDay(yearStr,monthStr,dayStr):
        print "Invalid day"
        return

    #check hour
    hourF = timeStr.find(':')
    hourStr = timeStr[yearF+1:hourF]
    if not 0 <= int(hourStr) <= 23:
        print "Invalid hour"
        return

    #check minute
    minuteF = timeStr.find(':',hourF+1)
    minuteStr = timeStr[hourF+1,minuteF]
    if not 0 <= int(minuteStr) <= 59:
        print "Invalid minute"
        return

    #check second
    secondStr = timeStr[minuteF+1:]
    if not 0 <= int(secondStr) <= 59:
        print "Invalid seconds"
        return

    print dayStr,"/",monthStr,"/",yearStr
    print hourStr,"/",minuteStr,"/",secondStr
    print monthStr,"/",yearStr
    if int(hourStr) > 12:
        print "PM"
    else:
        print "AM"








    
     
