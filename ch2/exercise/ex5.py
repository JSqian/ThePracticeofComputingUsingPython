weight = float(raw_input("Enter weight in KG:"))
height = float(raw_input("Enter height in M:"))
BMI = weight  / height**2

if BMI < 18.5:
    print "Too light"
elif 18.5 <= BMI <= 24.9:
    print "Normal"
elif 25.0 <= BMI <=29.9:
    print "Overweight"
elif BMI >= 30.0:
    print "fat"
    
