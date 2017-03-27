def displayMenu():
    print "1 Info"
    print "2 game"
    print "3 setting"
    choose = int(raw_input("Enter your choose(like '1'):"))
    return choose

def getChoose():
    choose = displayMenu()
    print "You choose",choose

getChoose()
