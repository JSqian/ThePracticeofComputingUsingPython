points = int(raw_input("Enter the lead in points: "))
points -= 3

has_ball = raw_input("Does the lead team have the ball (Yes or No): ")

if has_ball == 'Yes':
    points += 0.5
else:
    points -= 0.5

if points < 0:
    points = 0

points = points ** 2

seconds = int(raw_input("Enter the number of seconds remaining: "))

if points > seconds:
    print "Lead is safe."
else:
    print "Lead is not safe."
