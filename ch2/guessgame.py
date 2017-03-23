import random
number = random.randint(0,100)#get a number between 0 and 100 inclusive

print "Hi-Lo Number Guessing Game:between 0 and 100 inclusive."
print

# get an initial guess
guessString = raw_input("Guess a number: ")
guess = int(guessString)

while 0 <= guess <= 100:
    if guess > number:
        print "Guessed Too High."
    elif guess < number:
        print "Guessed Too Low."
    else:
        print "You guessed it. The number was:",number
        break

    guess = int(raw_input("Guess a number: "))
else:
    print "You quit early,the number was:",number
