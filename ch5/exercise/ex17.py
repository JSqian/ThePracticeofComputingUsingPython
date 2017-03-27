def calRate(completions,attempts,yards,touchDowns,interceptions):
    C = (((completions)*1.0/attempts)*100 - 30) / 20
    Y = (yards*1.0/attempts -3)/4
    T = (touchDowns*1.0/attempts)*20
    I = 2.375 - (interceptions*1.0/attempts)*25
    rate = (C+Y+T+I)/6*100
    return rate

def grade(rate):
    if rate <= 85:
        print "worse"
    elif rate <= 90:
        print "normal"
    elif rate <= 95:
        print "good"
    else:
        print "great"

completions = int(raw_input("Enter the number of completions:"))
attempts = int(raw_input("Enter the number of attempts:"))
yards = int(raw_input("Enter the yards:"))
touchDowns = int(raw_input("Enter the number of touchdowns:"))
interceptions = int(raw_input("Enter the number of interceptions:"))
rate = calRate(completions,attempts,yards,touchDowns,interceptions)
grade(rate)


