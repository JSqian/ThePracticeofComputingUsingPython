def checkStrLength(originalStr):
    if len(originalStr) < 160:
        return originalStr
    else:
        return originalStr[0:160]

def checkWordNum(originalStr):
    cleanStr = originalStr.strip()
    if len(cleanStr.split()) < 20:
        return originalStr
    else:
        print "Your message was too long"
      
