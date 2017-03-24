'''
This version does not use function
'''
import random
# do not check input
#code = raw_input("Enter the code color:")
code = ''.join(random.sample("ABCDEF",4))
hisGuessAndFeed = "" # history guess string and feedback string
for i in range(12):# guess 12 times
    if i > 0:
        print "Your history guess and feedback is:\n",hisGuessAndFeed
    guess = raw_input("Enter your guess:")
    if code == guess:
        print "You win.The code is ",guess
        break
    feedback = ""
    for index in range(len(code)):
        if code[index] == guess[index]:
            feedback += "B"
        elif guess[index] in code:
            feedback += "W"
        else:
            feedback += "N"
    hisGuessAndFeed += guess + " feedback:"+feedback + "\n" 
else:
    print "You lose.The code is ",code
