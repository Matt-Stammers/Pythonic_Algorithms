# This visually demonstrates recursion using turtle:

import turtle

myTurtle = turtle.Turtle()
myWin = turtle.Screen()

def drawSpiral(myTurtle, lineLen):
    if lineLen > 0:
        myTurtle.forward(lineLen)
        myTurtle.right(90)
        drawSpiral(myTurtle,lineLen-5)

drawSpiral(myTurtle,200)
myWin.exitonclick()

# as you can see the turtle spins in itself until it reaches a centrepoint.

# now we can use recursion to build a 'fractal' (something that looks the same at all degrees of magnification like a coastline - property of self-similarity.). 
# we can make a tree using turtle:

import turtle

def tree(branchLen,t):
    if branchLen > 5:
        t.forward(branchLen)
        t.right(20)
        tree(branchLen-20,t)
        t.left(40)
        tree(branchLen-15,t)
        t.right(20)
        t.backward(branchLen)

def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("green")
    tree(75,t)
    myWin.exitonclick()

main()

# this creates a wonky tree. You can experiment with all sorts of other options

# This will make a much thinner tree:

import turtle

def tree(branchLen,t):
    if branchLen > 5:
        t.forward(branchLen)
        t.right(15)
        tree(branchLen-15,t)
        t.left(30)
        tree(branchLen-15,t)
        t.right(15)
        t.backward(branchLen)

def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(150)
    t.down()
    t.color("green")
    tree(85,t)
    myWin.exitonclick()

main()
