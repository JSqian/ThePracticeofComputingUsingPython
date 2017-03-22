poundInKG = 0.453592
inchInMeter = 0.0254

weight = float(raw_input("Enter weight in pounds:"))
height = float(raw_input("Enter height in inches:"))
BMI = weight * poundInKG / (height * inchInMeter)**2
