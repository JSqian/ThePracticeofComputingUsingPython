import turtle

edge = int(raw_input("Enter the edge number of shape: "))
turnAngle = 180 - (edge - 2) * 180 / edge
turtle.forward(100)
turtle.fillcolor('red')
turtle.fill(True)
for i in range(edge-1):
    turtle.right(turnAngle)
    turtle.forward(100)
turtle.fill(False)

