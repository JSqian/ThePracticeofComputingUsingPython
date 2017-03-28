def isFloat(aStr):
    print '*** In the isFloat function.'
    stripped = aStr.replace('.','',1)
    if 'e' in aStr:
        stripped = stripped.replace('e','')
    return stripped.isdigit()
