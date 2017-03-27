def isLeap(year):
    if year % 400 == 0:
        return True
    elif year % 4 == 0 and year % 100 != 0:
        return True
    else:
        return False

def printSeconds(timeStr):
    '''
    MM/DD/YYYY HR:MIN:SEC
    '''
    monthF = timeStr.find('/')
    monthStr = timeStr[:monthF]
    dayF = timeStr.find('/',monthF+1)
    dayStr = timeStr[monthF+1:dayF]
    yearF = timeStr.find(' ')
    yearStr = timeStr[dayF:yearF]
    hourF = timeStr.find(':')
    hourStr = timeStr[yearF+1:hourF]
    minuteF = timeStr.find(':',hourF+1)
    minuteStr = timeStr[hourF+1,minuteF]
    secondStr = timeStr[minuteF+1:]
    isleap = isLeap(yearStr)
    secondsNum = calSeconds(monthStr,dayStr,hourStr,minuteStr,secondStr,isleap)
    print secondsNum
    
def allSeconds(monthStr,dayStr,hourStr,minuteStr,secondStr,isleap):
    day = int(dayStr)
    hour = int(hourStr)
    minute = int(minuteStr)
    second = int(secondStr)
    if monthStr == '1':
        days = day - 1
        seconds = calSeconds(days,hour,minute,second)
    if monthStr == '2':
        days = 31 + day - 1
        seconds = calSeconds(days,hour,minute,second)
    if monthStr == '3':
        if isleap:
            days = 31 + 29 + day - 1
        else:
            days = 31 + 28 + day - 1
        seconds = calSeconds(days,hour,minute,second)
    if monthStr == '4':
        if isleap:
            days = 31 + 29 + 31 + day - 1
        else:
            days = 31 + 28 + 31 + day - 1
        seconds = calSeconds(days,hour,minute,second)
    if monthStr == '5':
        if isleap:
            days = 31 + 29 + 31 + 30 + day - 1
        else:
            days = 31 + 28 + 31 + 30 + day - 1
        seconds = calSeconds(days,hour,minute,second)
    if monthStr == '6':
        if isleap:
            days = 31 + 29 + 31 + 30 + 31 + day - 1
        else:
            days = 31 + 28 + 31 + 30 + 31 + day - 1
        seconds = calSeconds(days,hour,minute,second)
    if monthStr == '7':
        if isleap:
            days = 31 + 29 + 31 + 30 + 31 + 30 + day - 1
        else:
            days = 31 + 28 + 31 + 30 + 31 + 30 + day - 1
        seconds = calSeconds(days,hour,minute,second)
    if monthStr == '8':
        if isleap:
            days = 31 + 29 + 31 + 30 + 31 + 30 + 31 + day - 1
        else:
            days = 31 + 28 + 31 + 30 + 31 + 30 + 31 + day - 1
        seconds = calSeconds(days,hour,minute,second)
    if monthStr == '9':
        if isleap:
            days = 31 + 29 + 31 + 30 + 31 + 30 + 31 + 31 + day - 1
        else:
            days = 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + day - 1
        seconds = calSeconds(days,hour,minute,second)
    if monthStr == '10':
        if isleap:
            days = 31 + 29 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + day - 1
        else:
            days = 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + day - 1
        seconds = calSeconds(days,hour,minute,second)
    if monthStr == '11':
        if isleap:
            days = 31 + 29 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + day - 1
        else:
            days = 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + day - 1
        seconds = calSeconds(days,hour,minute,second)
    if monthStr == '12':
        if isleap:
            days = 31 + 29 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30 + day - 1
        else:
            days = 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30 + day - 1
        seconds = calSeconds(days,hour,minute,second)
    return seconds

def calSeconds(days,hour,minute,second):
    seconds = days * 24 * 3600 + hour * 3600 + minute * 60 + second
    return seconds


    
