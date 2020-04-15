# Case-study #1
# Developers: Sharkov Kirill 40%
#             Keda Svetlana 30%
#             Ermolenko Vladimir 30%
import turtle
import math
import time

def paragram1(x,y,a,color):
    '''
       Function, drawing parallelogram 1.
       :param x: upper left corner coordinate x
       :param y: upper left corner coordinate y
       :param a: side length of a parallelogram
       :return: None
    '''
    turtle.fillcolor(color)
    turtle.pencolor(color)
    turtle.up()
    turtle.setposition(x, y)
    turtle.begin_fill()
    turtle.down()
    turtle.forward(math.sqrt(2)*a/2)
    turtle.right(45)
    turtle.forward(a)
    turtle.right(135)
    turtle.forward(math.sqrt(2)*a/2)
    turtle.right(45)
    turtle.forward(a)
    turtle.right(135)
    turtle.end_fill()
    turtle.up()

def paragram2(x,y,a,color):
    '''
          Function, drawing parallelogram 2.
          :param x: upper left corner coordinate x
          :param y: upper left corner coordinate y
          :param a: side length of a parallelogram
          :return: None
    '''
    turtle.fillcolor(color)
    turtle.pencolor(color)
    turtle.up()
    turtle.setposition(x, y)
    turtle.begin_fill()
    turtle.down()
    turtle.right(45)
    turtle.forward(math.sqrt(2) * a/2)
    turtle.right(45)
    turtle.forward(a)
    turtle.right(135)
    turtle.forward(math.sqrt(2) * a/2)
    turtle.right(45)
    turtle.forward(a)
    turtle.right(90)
    turtle.end_fill()
    turtle.up()

def paragram3(x,y,a,color):
    '''
          Function, drawing parallelogram 3.
          :param x: upper left corner coordinate x
          :param y: upper left corner coordinate y
          :param a: side length of a parallelogram
          :return: None
    '''
    turtle.fillcolor(color)
    turtle.pencolor(color)
    turtle.up()
    turtle.setposition(x, y)
    turtle.forward(a)
    turtle.begin_fill()
    turtle.down()
    turtle.right(90)
    turtle.forward(a)
    turtle.right(45)
    turtle.forward(math.sqrt(2) * a/2)
    turtle.right(135)
    turtle.forward(a)
    turtle.right(45)
    turtle.forward(math.sqrt(2) * a/2)
    turtle.right(45)
    turtle.end_fill()
    turtle.up()

def paragram4(x,y,a,color):
    '''
          Function, drawing parallelogram 4.
          :param x: upper left corner coordinate x
          :param y: upper left corner coordinate y
          :param a: side length of a parallelogram
          :return: None
    '''
    turtle.fillcolor(color)
    turtle.pencolor(color)
    turtle.up()
    turtle.setposition(x, y)
    turtle.forward(a)
    turtle.begin_fill()
    turtle.down()
    turtle.forward(a)
    turtle.right(135)
    turtle.forward(math.sqrt(2) * a/2)
    turtle.right(45)
    turtle.forward(a)
    turtle.right(135)
    turtle.forward(math.sqrt(2) * a/2)
    turtle.right(45)
    turtle.end_fill()
    turtle.up()

def paragram5(x,y,a,color):
    '''
          Function, drawing parallelogram 5.
          :param x: upper left corner coordinate x
          :param y: upper left corner coordinate y
          :param a: side length of a parallelogram
          :return: None
    '''
    turtle.fillcolor(color)
    turtle.pencolor(color)
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.begin_fill()
    turtle.right(45)
    turtle.forward(math.sqrt(2.25)*a)
    turtle.right(45)
    turtle.forward(a)
    turtle.right(135)
    turtle.forward(math.sqrt(2.25)*a)
    turtle.right(45)
    turtle.forward(a)
    turtle.right(90)
    turtle.end_fill()
    turtle.up()

def square1(x,y,a,color):
    '''
          Function, drawing square 1.
          :param x: upper left corner coordinate x
          :param y: upper left corner coordinate y
          :param a: side length of a square
          :return: None
    '''
    turtle.fillcolor(color)
    turtle.pencolor(color)
    turtle.begin_fill()
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(90)
    turtle.end_fill()
    turtle.up()

def square2(x,y,a,color):
    '''
              Function, drawing square 2.
              :param x: upper left corner coordinate x
              :param y: upper left corner coordinate y
              :param a: side length of a square
              :return: None
    '''
    turtle.fillcolor(color)
    turtle.pencolor(color)
    turtle.up()
    turtle.setposition(x, y)
    turtle.forward(a/math.sqrt(2))
    turtle.down()
    turtle.begin_fill()
    turtle.right(45)
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(45)
    turtle.end_fill()
    turtle.up()

def triangle1(x,y,a,color):
    '''
              Function, drawing triangle 1.
              :param x: upper left corner coordinate x
              :param y: upper left corner coordinate y
              :param a: side length of a triangle
              :return: None
    '''
    turtle.fillcolor(color)
    turtle.pencolor(color)
    turtle.up()
    turtle.setposition(x, y)
    turtle.right(90)
    turtle.forward(a)
    turtle.down()
    turtle.begin_fill()
    turtle.left(90)
    turtle.forward(a)
    turtle.left(90)
    turtle.forward(a)
    turtle.left(135)
    turtle.forward(math.sqrt(2)*a)
    turtle.left(135)
    turtle.end_fill()
    turtle.up()

def triangle2(x,y,a,color):
    '''
            Function, drawing triangle 2.
            :param x: upper left corner coordinate x
            :param y: upper left corner coordinate y
            :param a: side length of a triangle
            :return: None
        '''
    turtle.fillcolor(color)
    turtle.pencolor(color)
    turtle.up()
    turtle.setposition(x,y)
    turtle.down()
    turtle.begin_fill()
    turtle.right(90)
    turtle.forward(a)
    turtle.left(90)
    turtle.forward(a)
    turtle.left(135)
    turtle.forward(math.sqrt(2) * a)
    turtle.right(135)
    turtle.end_fill()
    turtle.up()

def triangle3(x,y,a,color):
    '''
              Function, drawing triangle 3.
              :param x: upper left corner coordinate x
              :param y: upper left corner coordinate y
              :param a: side length of a triangle
              :return: None
    '''
    turtle.up()
    turtle.fillcolor(color)
    turtle.pencolor(color)
    turtle.setposition(x, y)
    turtle.down()
    turtle.begin_fill()
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(135)
    turtle.forward(math.sqrt(2) * a)
    turtle.right(135)
    turtle.end_fill()
    turtle.up()

def triangle4(x,y,a,color):
    '''
              Function, drawing triangle 4.
              :param x: upper left corner coordinate x
              :param y: upper left corner coordinate y
              :param a: side length of a triangle
              :return: None
    '''
    turtle.up()
    turtle.fillcolor(color)
    turtle.pencolor(color)
    turtle.setposition(x, y)
    turtle.begin_fill()
    turtle.down()
    turtle.forward(a)
    turtle.right(135)
    turtle.forward(math.sqrt(2) * a)
    turtle.right(135)
    turtle.forward(a)
    turtle.right(90)
    turtle.end_fill()
    turtle.up()

def triangleleft(x,y,a,color):
    '''
            Function, drawing left triangle.
            :param x: upper left corner coordinate x
            :param y: upper left corner coordinate y
            :param a: side length of a triangle
            :return: None
      '''
    turtle.fillcolor(color)
    turtle.pencolor(color)
    turtle.up()
    turtle.setposition(x, y)
    turtle.forward(a/2)
    turtle.down()
    turtle.begin_fill()
    turtle.right(90)
    turtle.forward(a)
    turtle.right(135)
    turtle.forward(math.sqrt(0.5)*a)
    turtle.right(90)
    turtle.forward(math.sqrt(0.5) * a)
    turtle.right(45)
    turtle.end_fill()
    turtle.up()

def triangleright(x,y,a,color):
    '''
            Function, drawing right triangle.
            :param x: upper left corner coordinate x
            :param y: upper left corner coordinate y
            :param a: side length of a triangle
            :return: None
          '''
    turtle.fillcolor(color)
    turtle.pencolor(color)
    turtle.setposition(x, y)
    turtle.down()
    turtle.begin_fill()
    turtle.right(45)
    turtle.forward(math.sqrt(0.5)*a)
    turtle.right(90)
    turtle.forward(math.sqrt(0.5) * a)
    turtle.right(135)
    turtle.forward(a)
    turtle.right(90)
    turtle.end_fill()
    turtle.up()

def triangleup(x,y,a,color):
    '''
                Function, drawing up triangle.
                :param x: upper left corner coordinate x
                :param y: upper left corner coordinate y
                :param a: side length of a triangle
                :return: None
          '''
    turtle.fillcolor(color)
    turtle.pencolor(color)
    turtle.setposition(x, y)
    turtle.up()
    turtle.forward(a/2)
    turtle.down()
    turtle.begin_fill()
    turtle.right(45)
    turtle.forward(math.sqrt(0.5) * a)
    turtle.right(135)
    turtle.forward(a)
    turtle.right(135)
    turtle.forward(math.sqrt(0.5) * a)
    turtle.right(45)
    turtle.end_fill()
    turtle.up()

def triangledown(x,y,a,color):
    '''
                Function, drawing down triangle.
                :param x: upper left corner coordinate x
                :param y: upper left corner coordinate y
                :param a: side length of a triangle
                :return: None
          '''
    turtle.fillcolor(color)
    turtle.pencolor(color)
    turtle.setposition(x, y)
    turtle.down()
    turtle.begin_fill()
    turtle.forward(a)
    turtle.right(135)
    turtle.forward(math.sqrt(0.5) * a)
    turtle.right(90)
    turtle.forward(math.sqrt(0.5) * a)
    turtle.right(135)
    turtle.end_fill()
    turtle.up()

def kvadrat():
#Function, drawing a big square.
    triangledown(-50,50,100,"red")
    triangleup(-25,0,50,"pink")
    triangleright(-50,50,100,"yellow")
    paragram4(-75,-25,50,"green")
    square2(0,25,math.sqrt(2)*25,"orange")
    triangleleft(25,50,50,"purple")
    triangle1(0,0,50,'blue')

def rabbit():
#Function, drawing a rabbit.
    triangle4(-200, -270, 30, "yellow")
    triangle1(-200, -240, 30, "red")
    triangleright(-169, -260, 20, "pink")
    square1(-169, -230, 20, "orange")
    paragram1(-200, -208, 30, "green")
    triangle1(-200, -280, 20, "blue")
    triangle2(-180, -285, 15, "purple")

def fish():
#Function, drawing a fish.
    triangle3(0, -200, 50, "orangered")
    triangle1(0, -250, 50, "gold")
    square2(17, -234, 23, "orange")
    triangle4(-8, -250, 23, "pink")
    paragram1(-30, -226, 32, "green")
    triangle1(-31, -250, 23, "purple")
    triangleright(50, -225, 50, "blue")

def fox():
#Function, drawing a fox.
    triangleright(100, 100, 60, "blue")
    triangleleft(130, 100, 60, "red")
    square2(102, 65, 40, "orange")
    triangleleft(93, 16, 100, "green")
    triangleright(148, 16, 120, "pink")
    triangle1(109, -50, 100, "grey")
    paragram4(192, -130, 40, "yellow")

def swan():
#Function, drawing a swan.
    triangle1(300, 100, 40, "orange")
    paragram2(344, 100, 45, "red")
    square2(314, 54, 38, "pink")
    triangleright(313, 22, 49, "grey")
    triangleleft(313, 9, 85, "green")
    triangle2(360, 9, 84, "blue")
    triangledown(365, 9, 115, "purple")

def dragon():
#Function, drawing a dragon.
    triangle3(300, -120, 40, "red")
    paragram5(343, -120, 40, "orange")
    square1(388, -163, 40, "blue")
    triangle2(388, -205, 60, "green")
    triangle4(430, -100, 60, "yellow")
    triangle2(431, -163, 40, "grey")
    triangleleft(474, -158, 90, "pink")

def helicopter():
#Function, drawing a helicopter.
    triangleright(250,-225,50, "red")
    triangleleft(225,-225,50, "yellow")
    paragram4(235,-210,30, "green")
    triangleup(215,-207,35, "blue")
    triangleup(209,-251,30, "purple")
    triangledown(192,-251,30, "pink")
    square2(169,-230,20, "orange")
def rocket():
#Function, drawing a rocket.
    triangleup(-220,140,70, "pink")
    triangle3(-220,102,70, "blue")
    triangleright(-223,101,140, "green")
    triangleleft(-221,29,140, "red")
    paragram2(-148,-41,70, "yellow")
    square2(-255,-42,45, "orange")
    triangleright(-257,-76,67, "purple")

def main():
    '''
       Main function.
       :return: None
       '''
    kvadrat()
    rabbit()
    fish()
    fox()
    swan()
    dragon()
    helicopter()
    rocket()
    turtle.done()

if __name__ == '__main__':
    main()
