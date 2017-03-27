import turtle

turtle.speed(0)
recWidth = 320
recHeight = 210
lineHeight = recHeight / 7
starEdgeLen = 20
starDistance = 80
leftSpace = 60
colSpace = 30
edge = 13 # stars in circle

'''
def setScale(scale=1):
    recWidth *= scale
    recHeight *= scale
    lineHeight *= scale
    starEdgeLen *=scale
    starDistance *= scale
    leftSpace *= scale
    colSpace *= scale
'''

def drawStar():
    turtle1 = turtle.clone()
    turtle1.setheading(0)
    turtle1.fillcolor("white")
    turtle1.fill(True)
    for i in range(4):
        turtle1.forward(starEdgeLen)
        turtle1.right(144)
    turtle1.forward(starEdgeLen)
    turtle1.fill(False)

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

def drawStarInLine():
    for i in range(1,6):
        if i % 2 == 1:
            setPosition(-recWidth+leftSpace,recHeight-colSpace * i)
            drawOddStarline()
        else:
            setPosition(-recWidth+leftSpace+starDistance/2,recHeight-colSpace*i)
            drawEvenStarline()

def drawStarInCircle():
    '''
    13 stars
    '''
    setPosition(-recWidth/2-leftSpace/2-5,recHeight-20)
    drawStar()
    turnAngle = 180 - (edge - 2) * 180 / edge
    turtle.forward(40)
    for i in range(edge-1):    
        turtle.right(turnAngle)
        drawStar()
        turtle.forward(40)
    

# main program
#draw rectangle
scale = float(raw_input("Enter a positive number:"))
#set scale
recWidth *= scale
recHeight *= scale
lineHeight *= scale
starEdgeLen *=scale
starDistance *= scale
leftSpace *= scale
colSpace *= scale

#draw rectangle
turtle.hideturtle()
setPosition(-recWidth,recHeight)
drawRectangle(recWidth,recHeight)

#draw stars
drawStarInLine()
#drawStarInCircle()


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

