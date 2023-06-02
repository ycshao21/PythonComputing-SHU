"""
This module contains code from
Think Python by Allen B. Downey
http://thinkpython.com

Copyright 2012 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""
import math


try:
    # see if Swampy is installed as a package
    from swampy.TurtleWorld import *
except ImportError:
    # otherwise see if the modules are on the PYTHONPATH
    from TurtleWorld import *


def square(t, length):
    """Draws a square with sides of the given length.

    Returns the Turtle to the starting position and location.
    """
    for i in range(4):
        fd(t, length)
        lt(t)


def polyline(t, n, length, angle):
    """Draws n line segments.

    t: Turtle object
    n: number of line segments
    length: length of each segment
    angle: degrees between segments
    """
    for i in range(n):
        fd(t, length)
        lt(t, angle)


def polygon(t, n, length):
    """Draws a polygon with n sides.

    t: Turtle
    n: number of sides
    length: length of each side.
    """
    angle = 360.0 / n
    polyline(t, n, length, angle)


def arc(t, r, angle):
    """Draws an arc with the given radius and angle.

    t: Turtle
    r: radius
    angle: angle subtended by the arc, in degrees
    """
    arc_length = 2 * math.pi * r * abs(angle) / 360
    n = int(arc_length / 4) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n

    # making a slight left turn before starting reduces
    # the error caused by the linear approximation of the arc
    lt(t, step_angle / 2)
    polyline(t, n, step_length, step_angle)
    rt(t, step_angle / 2)


def circle(t, r):
    """Draws a circle with the given radius.

    t: Turtle
    r: radius
    """
    arc(t, r, 360)


'''
操作乌龟的函数
'''


def moveTurtle(bob, x, y):
    # x>0：蛇的前方
    # y>0：蛇的左侧
    fd(bob, x)
    if y != 0:
        lt(bob)
        fd(bob, y)
        rt(bob)


def rotateTurtle(bob, angle):
    # angle>0：顺时针旋转angle度
    rt(bob, angle)


'''
绘制蛇的函数
'''


def drawHead(bob, radius):
    # 绘制蛇头形状
    bob.set_pen_color("green")
    moveTurtle(bob, -radius, 0)
    rotateTurtle(bob, 90)
    # {@ 面朝下绘制半圆
    pd(bob)
    arc(bob, radius, 180)
    pu(bob)
    # @ 面朝上}
    moveTurtle(bob, 0, -2 * radius)
    # {@ 面朝下绘制半圆
    pd(bob)
    arc(bob, 2 * radius, 180)
    pu(bob)
    # @ 面朝上}

    moveTurtle(bob, 0, radius)

    # 绘制眼睛
    bob.set_pen_color("blue")
    eye_offset = radius / 1.4  # 眼睛与当前位置的距离
    radius_eye = radius / 8
    length_eye = radius / 3
    moveTurtle(bob, -eye_offset, 0)
    # {@ 面朝上，绘制一个圆和正六边形
    pd(bob)
    circle(bob, radius_eye)
    pu(bob)
    moveTurtle(bob, -length_eye / 2, - length_eye * math.sqrt(3) / 2 + radius_eye)
    pd(bob)
    polygon(bob, 6, length_eye)
    pu(bob)
    moveTurtle(bob, length_eye / 2, length_eye * math.sqrt(3) / 2 - radius_eye)
    # @ 面朝下}

    # 绘制蛇信子
    bob.set_pen_color("red")
    tongue_offset = radius / 4
    tongue_inner = radius / 3
    tongue_outer = radius / 2
    tongue_angle = 30
    moveTurtle(bob, eye_offset + radius + tongue_offset, 0)
    # {@ 面朝下绘制左半部分
    pd(bob)
    rotateTurtle(bob, tongue_angle)
    moveTurtle(bob, tongue_inner, 0)
    rotateTurtle(bob, -tongue_angle)
    moveTurtle(bob, -tongue_outer, 0)
    pu(bob)
    # @ 面朝下}
    moveTurtle(bob, 0, tongue_inner)
    # {@ 面朝下绘制右边部分
    pd(bob)
    moveTurtle(bob, tongue_outer, 0)
    rotateTurtle(bob, 180-tongue_angle)
    moveTurtle(bob, tongue_inner, 0)
    rotateTurtle(bob, tongue_angle)
    pu(bob)
    # @ 面朝上}
    moveTurtle(bob, tongue_offset + radius, 0)
    rotateTurtle(bob, 90)


def drawBody(bob, radius, neck, body):
    bob.set_pen_color("green")
    rotateTurtle(bob, 90)
    # {@ 面朝下绘制身体外侧
    pd(bob)
    moveTurtle(bob, neck, 0)
    arc(bob, 4 * radius, 90)
    moveTurtle(bob, body, 0)
    arc(bob, 4 * radius, 90)
    pu(bob)
    # @ 面朝上}
    moveTurtle(bob, neck, body + 6 * radius)
    rotateTurtle(bob, 180)
    # {@ 面朝下，绘制身体内侧
    pd(bob)
    moveTurtle(bob, neck, 0)
    arc(bob, 2 * radius, 90)
    moveTurtle(bob, body + 2 * radius, 0)
    arc(bob, 2 * radius, 90)
    pu(bob)
    # @ 面朝上}
    rotateTurtle(bob, 90)


def writePython(turtle, radius, neck, body):
    turtle.set_pen_color("purple")
    height = 1.2 * neck
    width = body + 2 * radius
    halfLetterHeight = (height - 2 * height / 8) / 2

    # {@ 面朝右，绘制矩形
    pd(turtle)
    moveTurtle(turtle, width, height)
    moveTurtle(turtle, -width, -height)
    pu(turtle)
    # @ 面朝右}
    moveTurtle(turtle, width / 8, height / 8)
    rotateTurtle(turtle, -90)
    # {@ 面朝上绘制字母P
    pd(turtle)
    moveTurtle(turtle, 2 * halfLetterHeight, 0)
    rotateTurtle(turtle, 90)
    moveTurtle(turtle, width / 20, 0)
    arc(turtle, halfLetterHeight / 2, -180)
    moveTurtle(turtle, width / 20, 0)
    pu(turtle)
    # @ 面朝左}
    moveTurtle(turtle, -width / 6, halfLetterHeight)
    rotateTurtle(turtle, 90)
    # {@ 面朝上绘制字母Y
    pd(turtle)
    moveTurtle(turtle, halfLetterHeight, 0)
    rotateTurtle(turtle, -30)
    moveTurtle(turtle, halfLetterHeight * 2 / math.sqrt(3), 0)
    pu(turtle)
    moveTurtle(turtle, -halfLetterHeight * 2 / math.sqrt(3), 0)
    rotateTurtle(turtle, 60)
    pd(turtle)
    moveTurtle(turtle, halfLetterHeight * 2 / math.sqrt(3), 0)
    rotateTurtle(turtle, 60)
    pu(turtle)
    # @ 面朝右}
    moveTurtle(turtle, width / 30, 0)
    # {@ 面朝右绘制字母T
    pd(turtle)
    moveTurtle(turtle, width / 10, 0)
    moveTurtle(turtle, - width / 20, 0)
    rotateTurtle(turtle, 90)
    moveTurtle(turtle, 2 * halfLetterHeight, 0)
    pu(turtle)
    # @ 面朝下}
    moveTurtle(turtle, 0, width / 12)
    # {@ 面朝下绘制字母H
    pd(turtle)
    moveTurtle(turtle, -2 * halfLetterHeight, 0)
    moveTurtle(turtle, halfLetterHeight, width / 12)
    moveTurtle(turtle, halfLetterHeight, 0)
    moveTurtle(turtle, -2 * halfLetterHeight, 0)
    pu(turtle)
    # @ 面朝下}
    moveTurtle(turtle, halfLetterHeight / 2, width / 22)
    # {@ 面朝下绘制字母O
    pd(turtle)
    moveTurtle(turtle, halfLetterHeight, 0)
    arc(turtle, halfLetterHeight / 2, 180)
    moveTurtle(turtle, halfLetterHeight, 0)
    arc(turtle, halfLetterHeight / 2, 180)
    pu(turtle)
    # @ 面朝下}
    moveTurtle(turtle, 3 * halfLetterHeight / 2, width / 8)
    # {@ 面朝下绘制字母N
    pd(turtle)
    moveTurtle(turtle, -2 * halfLetterHeight, 0)
    rotateTurtle(turtle, -30)
    moveTurtle(turtle, halfLetterHeight * 4 / math.sqrt(3), 0)
    rotateTurtle(turtle, -150)
    moveTurtle(turtle, 2 * halfLetterHeight, 0)
    pu(turtle)
    # @ 面朝上}


if __name__ == '__main__':
    radius = 22
    neck = 60
    body = 250

    # 初始化画布和画笔
    TurtleWorld()
    bob = Turtle()  # 默认面朝右
    bob.delay = 0.02

    # 绘制蛇
    pu(bob)
    moveTurtle(bob, -140, 100)
    drawHead(bob, radius)
    moveTurtle(bob, radius, 0)
    drawBody(bob, radius, neck, body)
    moveTurtle(bob, - body - 4 * radius, -radius / 2)
    writePython(bob, radius, neck, body)
    die(bob)
    wait_for_user()

