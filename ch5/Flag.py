import turtle

turtle.speed(0)
recWidth = 320
recHeight = 210
lineHeight = recHeight / 7
starEdgeLen = 20
starDistance = 80
leftSpace = 60
colSpace = 30

def drawStar():
    turtle.fillcolor("white")
    turtle.fill(True)
    for i in range(4):
        turtle.forward(starEdgeLen)
        turtle.right(144)
    turtle.forward(starEdgeLen)
    turtle.fill(False)

def drawRectangle(width=recWidth,height=recHeight,color="blue"):
    turtle.fillcolor(color)
    turtle.fill(True)
    for i in range(2):
        turtle.forward(width)
        turtle.right(90)
        turtle.forward(height)
        turtle.right(90)
    turtle.fill(False)

def setPosition(x,y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.setheading(0)

def drawOddStarline():
    drawStar()
    for i in range(2):
        turtle.setheading(0)
        turtle.forward(starDistance)
        drawStar()

def drawEvenStarline():
    drawStar()
    turtle.setheading(0)
    turtle.forward(starDistance)
    drawStar()

# main program
#draw rectangle
setPosition(-recWidth,recHeight)
drawRectangle()

#draw stars
for i in range(1,6):
    if i % 2 == 1:
        setPosition(-recWidth+leftSpace,recHeight-colSpace * i)
        drawOddStarline()
    else:
        setPosition(-recWidth+leftSpace+starDistance/2,recHeight-colSpace*i)
        drawEvenStarline()

# Draw line right to the rectangle
for i in range(7):
    setPosition(0,recHeight-lineHeight*i)
    if i % 2 == 0:
        drawRectangle(recWidth,lineHeight,"red")
    else:
        drawRectangle(recWidth,lineHeight,"white")

# draw lines on the bottom
for i in range(1,7):
    setPosition(-recWidth,-(i-1)*lineHeight)
    if i % 2 == 0:
        drawRectangle(recWidth*2,lineHeight,"red")
    else:
        drawRectangle(recWidth*2,lineHeight,"white")


