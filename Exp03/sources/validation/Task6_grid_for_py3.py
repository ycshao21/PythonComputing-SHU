"""This module contains code from
Think Python by Allen B. Downey
http://thinkpython.com

Copyright 2012 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html

"""
import os

folder_path = "../../outputs"
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

# here is a mostly-straightforward solution to the
# two-by-two version of the grid.

from pycallgraph2 import PyCallGraph
from pycallgraph2.output import GraphvizOutput

def do_twice(f):
    f()
    f()

def do_four(f):
    do_twice(f)
    do_twice(f)

def print_beam():
    print('+ - - - -', end=' ')

def print_post():
    print('|        ', end=' ')

def print_beams():
    do_twice(print_beam)
    print('+')

def print_posts():
    do_twice(print_post)
    print('|')

def print_row():
    print_beams()
    do_four(print_posts)

def print_grid():
    do_twice(print_row)
    print_beams()

graphviz = GraphvizOutput()
graphviz.output_file = '../../outputs/grid_2.png'
with PyCallGraph(output=graphviz):
    print_grid()

# here is a less-straightforward solution to the
# four-by-four grid

def one_four_one(f, g, h):
    f()
    do_four(g)
    h()

def print_plus():
    print('+', end=' ')

def print_dash():
    print('-', end=' ')

def print_bar():
    print('|', end=' ')

def print_space():
    print(' ', end=' ')

def print_end():
    print()  # 换行

def nothing():
    return

def print1beam():
    one_four_one(nothing, print_dash, print_plus)

def print1post():
    one_four_one(nothing, print_space, print_bar)

def print4beams():
    one_four_one(print_plus, print1beam, print_end)

def print4posts():
    one_four_one(print_bar, print1post, print_end)

def print_row():
    one_four_one(nothing, print4posts, print4beams)

def print_grid():
    one_four_one(print4beams, print_row, nothing)

graphviz = GraphvizOutput()
graphviz.output_file = '../../outputs/grid_4.png'
with PyCallGraph(output=graphviz):
    print_grid()
