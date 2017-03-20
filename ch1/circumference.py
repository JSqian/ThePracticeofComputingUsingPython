# calculate the area and circumference of a circle from its radius
# Step 1: prompt for a radius
# Step 2: apply the area formula
# Step 3: Print out the results
import math

radiusString = raw_input("Enter the radius of your circle: ")
radiusInteger = int(radiusString)

circumference = 2 * math.pi * radiusInteger
area = math.pi * (radiusInteger ** 2)

print "The circumference is:",circumference, \
      ", and the area is:",area
