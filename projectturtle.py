from turtle import *
setup()
colormode(255)
setup( width = 1080, height = 650, startx = None, starty = None)

heart_turtle = Turtle()
top_turtle = Turtle()
item_turtle = Turtle()
map_turtle = Turtle()
ground_turtle = Turtle()
wall_turtle = Turtle()
detail_turtle = Turtle()
item_turtle2 = Turtle()

###
heart_turtle.speed(0)
top_turtle.speed(0)
item_turtle.speed(0)
map_turtle.speed(0)
ground_turtle.speed(0)
wall_turtle.speed(0)
detail_turtle.speed(0)
item_turtle2.speed(0)
###

def draw_hearts(x,y,color1,color2):
    heart_turtle.penup()
    heart_turtle.goto(x,y)
    heart_turtle.right(180)
    heart_turtle.pendown()
    for i in range(3):
        heart_turtle.color(color1,color2)
        heart_turtle.begin_fill()
        heart_turtle.forward(15)
        heart_turtle.left(90)
        heart_turtle.forward(5)
        heart_turtle.right(90)
        heart_turtle.forward(5)
        heart_turtle.right(90)
        heart_turtle.forward(5)
        heart_turtle.left(90)
        heart_turtle.forward(15)
        heart_turtle.left(90)
        heart_turtle.forward(5)
        heart_turtle.right(90)
        heart_turtle.forward(5)
        heart_turtle.left(90)
        heart_turtle.forward(5)
        heart_turtle.right(90)
        heart_turtle.forward(5)
        heart_turtle.left(90)
        heart_turtle.forward(20)
        heart_turtle.left(90)
        heart_turtle.forward(5)
        heart_turtle.right(90)
        heart_turtle.forward(5)
        heart_turtle.left(90)
        heart_turtle.forward(5)
        heart_turtle.right(90)
        heart_turtle.forward(5)
        heart_turtle.left(90)
        heart_turtle.forward(5)
        heart_turtle.right(90)
        heart_turtle.forward(5)
        heart_turtle.left(90)
        heart_turtle.forward(5)
        heart_turtle.right(90)
        heart_turtle.forward(5)
        heart_turtle.left(90)
        heart_turtle.forward(5)
        heart_turtle.right(90)
        heart_turtle.forward(5)
        heart_turtle.left(90)
        heart_turtle.forward(5)
        heart_turtle.left(90)
        heart_turtle.forward(5)
        heart_turtle.right(90)
        heart_turtle.forward(5)
        heart_turtle.left(90)
        heart_turtle.forward(5)
        heart_turtle.right(90)
        heart_turtle.forward(5)
        heart_turtle.left(90)
        heart_turtle.forward(5)
        heart_turtle.right(90)
        heart_turtle.forward(5)
        heart_turtle.left(90)
        heart_turtle.forward(5)
        heart_turtle.right(90)
        heart_turtle.forward(5)
        heart_turtle.left(90)
        heart_turtle.forward(5)
        heart_turtle.right(90)
        heart_turtle.forward(5)
        heart_turtle.left(90)
        heart_turtle.forward(20)
        heart_turtle.left(90)
        heart_turtle.forward(5)
        heart_turtle.right(90)
        heart_turtle.forward(5)
        heart_turtle.left(90)
        heart_turtle.forward(5)
        heart_turtle.right(90)
        heart_turtle.forward(5)
        heart_turtle.end_fill()
        heart_turtle.right(90)
        heart_turtle.penup()
        heart_turtle.forward(60)
        heart_turtle.right(180)
        heart_turtle.pendown()
    heart_turtle.penup()
    heart_turtle.forward(250)
    heart_turtle.right(90)
    heart_turtle.forward(30)
    heart_turtle.right(90)
    heart_turtle.color(color2)
    heart_turtle.pensize(3)
    heart_turtle.pendown()
    heart_turtle.forward(50)
    heart_turtle.penup()
    heart_turtle.right(90)
    heart_turtle.forward(25)
    heart_turtle.left(90)
    heart_turtle.forward(10)
    heart_turtle.write("LIFE",font=("Arial", 32, "normal"))
    heart_turtle.forward(100)
    heart_turtle.left(90)
    heart_turtle.forward(25)
    heart_turtle.right(90)
    heart_turtle.pendown()
    heart_turtle.forward(50)

def top(x,y,color):
    top_turtle.color(color)
    top_turtle.penup()
    top_turtle.goto(x,y)
    top_turtle.left(90)
    top_turtle.pendown()
    top_turtle.begin_fill()
    top_turtle.right(90)
    top_turtle.forward(540)
    top_turtle.left(90)
    top_turtle.forward(300)
    top_turtle.left(90)
    top_turtle.forward(1080)
    top_turtle.left(90)
    top_turtle.forward(300)
    top_turtle.left(90)
    top_turtle.forward(540)
    top_turtle.end_fill()

def ground(x,y,color):
    ground_turtle.color(color)
    ground_turtle.penup()
    ground_turtle.goto(x,y)
    ground_turtle.pendown()
    ground_turtle.begin_fill()
    ground_turtle.forward(540)
    ground_turtle.right(90)
    ground_turtle.forward(600)
    ground_turtle.right(90)
    ground_turtle.forward(1080)
    ground_turtle.right(90)
    ground_turtle.forward(600)
    ground_turtle.right(90)
    ground_turtle.forward(540)
    ground_turtle.end_fill()

def draw_items(x,y,color1,color2):
    item_turtle.color(color1)
    item_turtle.penup()
    item_turtle.goto(x,y)
    item_turtle.left(90)
    item_turtle.pensize(3)
    item_turtle.pendown()
    item_turtle.right(90)
    item_turtle.forward(50)
    item_turtle.left(90)
    item_turtle.forward(80)
    item_turtle.left(90)
    item_turtle.forward(50)
    item_turtle.left(90)
    item_turtle.forward(80)
    item_turtle.left(90)
    item_turtle.penup()
    item_turtle.forward(90)
    item_turtle.pendown()
    item_turtle.forward(50)
    item_turtle.left(90)
    item_turtle.forward(80)
    item_turtle.left(90)
    item_turtle.forward(50)
    item_turtle.left(90)
    item_turtle.forward(80)
    item_turtle.penup()
    item_turtle.left(180)
    item_turtle.forward(60)
    item_turtle.left(90)
    item_turtle.forward(78)
    item_turtle.left(180)
    item_turtle.color(color2)
    item_turtle.write("B",font=("Arial", 32, "normal"))
    item_turtle.forward(90)
    item_turtle.write("A",font=("Arial", 32, "normal"))
    
def draw_map(x,y,color,part):
    map_turtle.penup()
    if part == 1:
        map_turtle.color(color)
        map_turtle.goto(x,y)
        map_turtle.left(180)
        ##################
        map_turtle.pendown()
        map_turtle.right(90)
        map_turtle.begin_fill()
        map_turtle.forward(110)
        map_turtle.left(90)
        map_turtle.forward(230)
        map_turtle.left(90)
        map_turtle.forward(110)
        map_turtle.left(90)
        map_turtle.forward(230)
        map_turtle.end_fill()

    elif part == 2:
        map_turtle.goto(x,y)
        map_turtle.color(color)
        map_turtle.left(180)
        map_turtle.forward(110)
        map_turtle.right(90)
        map_turtle.begin_fill()
        for i in range(4):
            map_turtle.forward(10)
            map_turtle.left(90)
        map_turtle.end_fill()

def draw_walls(x,y,color,wall):
    wall_turtle.color(color)
    wall_turtle.penup()
    wall_turtle.home()
    if wall == 1:
        wall_turtle.goto(x,y)
        wall_turtle.left(180)
        ####################
        wall_turtle.pendown()
        wall_turtle.left(90)
        wall_turtle.begin_fill()
        wall_turtle.forward(70)
        wall_turtle.right(45)
        wall_turtle.forward(20)
        wall_turtle.left(45)
        wall_turtle.forward(20)
        wall_turtle.right(90)
        wall_turtle.forward(200)
        wall_turtle.left(90)
        wall_turtle.forward(20)
        wall_turtle.right(45)
        wall_turtle.forward(20)
        wall_turtle.left(45)
        wall_turtle.forward(20)
        wall_turtle.right(45)
        wall_turtle.forward(20)
        wall_turtle.left(45)
        wall_turtle.forward(20)
        wall_turtle.right(45)
        wall_turtle.forward(20)
        wall_turtle.left(45)
        wall_turtle.forward(20)
        wall_turtle.right(45)
        wall_turtle.forward(20)
        wall_turtle.right(45)
        wall_turtle.forward(170)
        wall_turtle.right(90)
        wall_turtle.forward(241)
        wall_turtle.right(90)
        wall_turtle.forward(440)
        wall_turtle.end_fill()

    elif wall == 2:
        wall_turtle.goto(x,y)
        wall_turtle.right(90)
        wall_turtle.pendown()
        wall_turtle.begin_fill()
        wall_turtle.forward(200)
        wall_turtle.left(45)
        wall_turtle.forward(20)
        wall_turtle.right(45)
        wall_turtle.forward(20)
        wall_turtle.left(90)
        wall_turtle.forward(517)
        wall_turtle.left(90)
        wall_turtle.forward(235)
        wall_turtle.left(90)
        wall_turtle.forward(538)
        wall_turtle.end_fill()

    elif wall == 3:
        wall_turtle.goto(x,y)
        wall_turtle.pendown()
        wall_turtle.begin_fill()
        wall_turtle.forward(150)
        wall_turtle.right(45)
        wall_turtle.forward(20)
        wall_turtle.right(45)
        wall_turtle.forward(100)
        wall_turtle.left(90)
        wall_turtle.forward(800)
        wall_turtle.left(90)
        wall_turtle.forward(130)
        wall_turtle.right(90)
        wall_turtle.forward(120)
        wall_turtle.right(90)
        wall_turtle.forward(190)
        wall_turtle.right(90)
        wall_turtle.forward(1090)
        wall_turtle.right(90)
        wall_turtle.forward(180)
        wall_turtle.end_fill()


def details(x,y,color,number,lor):
    detail_turtle.color(color)
    detail_turtle.pensize(3)
    detail_turtle.penup()
    detail_turtle.home
    detail_turtle.goto(x,y)
    detail_turtle.setheading(0)
    detail_turtle.left(180)
    detail_turtle.pendown()
    for i in range(number):
        detail_turtle.forward(22)
        detail_turtle.left(45)
        detail_turtle.forward(10)
        detail_turtle.left(45)
        detail_turtle.forward(10)
        detail_turtle.left(180)
        detail_turtle.forward(17)
        detail_turtle.left(90)
    
def draw_items2(x,y,color,color2,color3):
    item_turtle2.color(color)
    item_turtle2.penup()
    item_turtle2.goto(x,y)
    item_turtle2.pendown()
    item_turtle2.begin_fill()
    item_turtle2.forward(15)
    item_turtle2.right(90)
    item_turtle2.forward(15)
    item_turtle2.right(45)
    item_turtle2.forward(15)
    item_turtle2.right(45)
    item_turtle2.forward(15)
    item_turtle2.right(90)
    item_turtle2.forward(15)
    item_turtle2.right(45)
    item_turtle2.forward(15)
    item_turtle2.end_fill()
    item_turtle2.penup()
    item_turtle2.right(135)
    item_turtle2.forward(40)
    item_turtle2.left(90)
    item_turtle2.forward(20)
    item_turtle2.color(color2)
    item_turtle2.write("X20",font=("Arial", 32, "normal"))
    item_turtle2.left(180)
    item_turtle2.forward(25)
    item_turtle2.left(180)
    item_turtle2.color(color)
    item_turtle2.pendown()
    item_turtle2.pensize(3)
    for i in range(4):
        item_turtle2.forward(15)
        item_turtle2.right(90)
    item_turtle2.right(90)
    item_turtle2.forward(15)
    item_turtle2.right(45)
    item_turtle2.forward(15)
    item_turtle2.back(7)
    item_turtle2.left(90)
    item_turtle2.forward(5)
    item_turtle2.stamp()
    item_turtle2.penup()
    item_turtle2.right(45)
    item_turtle2.forward(15)
    item_turtle2.left(90)
    item_turtle2.forward(25)
    item_turtle2.color(color2)
    item_turtle2.write("XA",font=("Arial", 32, "normal"))
    item_turtle2.color(color3)
    item_turtle2.left(180)
    item_turtle2.forward(15)
    item_turtle2.pendown()
    item_turtle2.begin_fill()
    for i in range(8):
        item_turtle2.forward(10)
        item_turtle2.left(45)
    item_turtle2.end_fill()
    item_turtle2.penup()
    item_turtle2.left(90)
    item_turtle2.forward(35)
    item_turtle2.left(90)
    item_turtle2.forward(15)
    item_turtle2.color(color2)
    item_turtle2.write("X3",font=("Arial", 32, "normal"))

def cave(x,y,color):
    penup()
    goto(x,y)
    pendown()
    left(90)
    begin_fill()
    forward(60)
    left(90)
    forward(60)
    left(90)
    forward(60)
    left(90)
    forward(60)
    end_fill()
    
top(0,190,(0,0,0))

ground(0,190,(255,211,172))

draw_walls(-110,190,(101, 217, 72),1)
draw_walls(0.00,190.00,(101, 217, 72),2)
draw_walls(-540,-160,(101, 217, 72),3)

details(-110,190,(0,0,0),16,1)
details(-110,170,(0,0,0),16,1)
details(-110,150,(0,0,0),16,1)
details(-110,130,(0,0,0),16,1)
details(-120,110,(0,0,0),16,1)
details(-325,90,(0,0,0),9,1)
details(-335,70,(0,0,0),8,1)
details(-345,50,(0,0,0),7,1)
details(-355,30,(0,0,0),6,1)
details(-365,10,(0,0,0),6,1)
details(-375,-10,(0,0,0),6,1)
details(-385,-170,(0,0,0),6,1)
details(-385,-190,(0,0,0),6,1)
details(-385,-210,(0,0,0),6,1)
details(-385,-230,(0,0,0),6,1)
details(-385,-250,(0,0,0),6,1)
details(-385,-270,(0,0,0),6,1)

details(553,190,(0,0,0),19,2)
details(553,170,(0,0,0),19,2)
details(553,150,(0,0,0),19,2)
details(553,130,(0,0,0),19,2)
details(553,110,(0,0,0),19,2)
details(553,90,(0,0,0),19,2)
details(553,70,(0,0,0),19,2)
details(553,50,(0,0,0),19,2)
details(553,30,(0,0,0),19,2)
details(553,10,(0,0,0),19,2)
details(570,-10,(0,0,0),19,2)

details(550,-150,(0,0,0),4,2)
details(550,-170,(0,0,0),4,2)
details(550,-190,(0,0,0),4,2)
details(550,-210,(0,0,0),4,2)
details(550,-230,(0,0,0),4,2)
details(550,-250,(0,0,0),4,2)
details(550,-280,(0,0,0),38,2)

cave(-200,85,(0,0,0))

draw_map(-140,200,(183,183,183),1)
draw_map(-140,200,(101, 217, 72),2)

draw_items2(-110,300,(255,205,79),(255,255,255),(0,0,255))

draw_items(0,210,(0,95,249),(255,255,255))

draw_hearts(290,260,(0,0,0),(255,0,0))

done()
