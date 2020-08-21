#!/bin/py
from turtle import *
from random import randint

penup()
speed(0)
goto(-140,140)


# for step in range(6):
#   write(step)
#   forward(20)
for step in range(17):
  write(step, align='center')
  speed(0)
  right(90)
  forward(10)
  for i in range(7):
    pendown()
    forward(10)
    penup()
    forward(10)
  backward(150)
  left(90)
  forward(20)


ada = Turtle()
ada.color('red')
ada.shape('turtle')

ada.penup()
ada.speed(0)
ada.goto(-160,100)
ada.speed(5)
for i in range(10):
  ada.right(36)
ada.pendown()

bob = Turtle()
bob.color('blue')
bob.shape('turtle')

bob.penup()
bob.speed(0)
bob.goto(-160,70)
bob.speed(5)
for i in range(10):
  bob.right(36)
bob.pendown()

mac = Turtle()
mac.color('green')
mac.shape('turtle')

mac.penup()
mac.speed(0)
mac.goto(-160,40)
mac.speed(5)
for i in range(10):
  mac.right(36)
mac.pendown()

don = Turtle()
don.color('yellow')
don.shape('turtle')

don.penup()
don.speed(0)
don.goto(-160,10)
don.speed(5)
for i in range(10):
  don.right(36)
don.pendown()

for turn in range(100):
  ada.forward(randint(1,5))
  bob.forward(randint(1,5))
  mac.forward(randint(1,5))
  don.forward(randint(1,5))
