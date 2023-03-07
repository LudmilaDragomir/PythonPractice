# https://docs.python.org/3/library/turtle.html#
import turtle
from turtle import *

color('red', 'yellow')
begin_fill()

while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()


# turtle.forward(15)
# turtle.right(25)