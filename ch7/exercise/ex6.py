def mirror(pair):
    if type(pair) != type((1,2)) and type(pair) != type([]):
        print "Invalid input"
        return
    return pair[1],pair[0]
    
