---
layout: post
title: Multiple Turtle Movements using QtPy5 UI 🐢
category: [turtle,]
tag: [Python, QtPy, GUI]
comments : true
excerpt_separator: <!-- more -->
---
<!-- DACON 2020 TITLE -->

<!-- IT -->
<img width="125" align="left" style="padding: 0px 10px 0px 0px;" src="/images/post_img/20200328-00.png" >

'<span id="start-ch">The</span>'
python 'turtle' is a simple drawing tool which is based on one of the representative python GUI toolkits, 'tkinter'. It is simeple and easy to use so that many python trainee learns 'turtle' as one of the must-have-courses.

<!-- more -->



<br><br>

<!-- NARUTO SHADOW CLONE! -->
<img width="320" style="padding: 60px 0px 0px 10px;" align="right"
src="/images/post_img/20200328-01.png" >

<!-- The -->
'<span id="start-ch">Because</span>' the commands are so intuitive and simple like penup(), pendown(), many beginners are learn it through simple built-in IDE, or text editor. If you already learned it, are bored by simeple move and complicated input, why don't you try to multiple move of turtles and much beautiful choriographs. plus, let's try more of PyQt5, famous window GUI. let's gives turtle a shadow clone jutsu.



<br><br>

<!-- I -->
'<span id="start-ch">I</span>'
use the folder structure is as below, but you can change it. because I add another modules below 'k-mooc-reboot', I just set like this according to my coding note.

```python
  /[k-mook-reboot]
      |
      +-/[module_turtle]
        * turtles_multiple_moves.py
           |
           +-/[_ assets]
           | * __ init __ .py
           | * _ add_syspath_root.py
           | * modules_qt.py
           |
           +-/[_ statics]
           | * turtle_echo.txt
```


<br><br>

<!-- I -->
'<span id="start-ch">I</span>'
__atteched gitGist, which will be located at the directory above__

1. turtles_mulple_moves.py - main
1. __ init __ is just a name-only file, blank inside.
1. _ add_syspath_root.py - to set full path or root.
1. modues_gt.py - QtPy5 class file.
1. turtle_echo.txt - pre-inputted coordination file.
  > * if you draw something by one-by-one input method, you just copy a commandline echo and make a text file.
  > * in the text file, there are blank inputs. it means skip an input (press-enter) which means use same former coordination. if there's no change to punch in, just press Enter.



[[__GitGist Code__](https://bit.ly/3f16h9b)]: turtles_multiple_moves.py





<br><br>

<!-- How -->
'<span id="start-ch">How</span>'
__to stack multiple turtle drawing__

<img width="700" src="/images/post_img/20200328-02.png" />

* STEP.1 - draw something via dialog box using just 1 turtle.
* STEP.2 - drag command line, and make echo.txt file.
* STEP.3 - select pre-input option, draw it with multiple turtles.




<br><br>

<!-- The -->
'<span id="start-ch">The</span>'
__Exampes__

<img width="500" src="/images/post_img/20200328-03.png" />

<img width="500" src="/images/post_img/20200328-04.png" />




<br><br>

<!-- The -->
'<span id="start-ch">The</span>'
__main code block__

* [[__GitGist Code__](https://bit.ly/3f16h9b)]: turtles_multiple_moves.py



{% highlight python linenos %}
"""
# Test Turtle : multiple turtles movement
"""
# - Enable = blank enter
# - Enable = set number of turtles
# - Enable = echo dict drawing (record drawing)

print(__doc__)

import sys
import turtle

from _assets._add_syspath_root import root
from _assets.modules_qt import (QApplication, MyApp)

FILE_DIR = root + 'module_turtle\\_statics\\'
FILENAME_ECHO = FILE_DIR + 'turtle_echo.txt'

POSXY = (1300, 900)
WINDOWSIZE = (400,300)

def main():
    global MA, NUM_TURTLES, TURTLES
    MA = MyApp()
    NUM_TURTLES = int(qt_input('NUMBERS OF TURTLES? : '))
    TURTLES = [turtle.Turtle() for i in range(NUM_TURTLES)]

    mode_select = qt_input('MODE - [Enter]=DRAW / [1]=DICT INPUT : ')

    turtle.speed('fastest')

    if mode_select.startswith('1'):
        echoes = get_read_echo(filename_echo=FILENAME_ECHO)
        dict_moves = get_moves_from_echoes(echoes)
        draw_from_dict(TURTLES, dict_moves)
    else:
        draw_from_manual(TURTLES)

def qt_input(captionHead="INPUT :", winTitle="TITLE!"):
    MA.setGeometry(*POSXY, *WINDOWSIZE)
    qtInput = MA.getText(winTitle, captionHead)
    if qtInput: return qtInput
    return ""

def get_read_echo(filename_echo):
    """ """
    with open(filename_echo, mode='r', encoding='utf8') as f:
        echoes_string = f.read()
    return echoes_string

def get_moves_from_echoes(echoes):
    """ get string-moves array from string-echoes"""
    echoes_array = echoes.split('\n')
    moves_array = [echo.split(':')[1]
                    for echo in echoes_array
                    if echo.startswith('*** ENTER ANGLE')]
    dict_moves = {}
    for i, move in enumerate(moves_array, 1):
        if move != '':
            angle, move = move.split(',')
            angle, move = int(angle.strip()), int(move.strip())
            temp_move = (angle, move)
        dict_moves[i] = temp_move
    return dict_moves

def draw_from_dict(turtles, dict):
    """ # read movements from dict, draw multi-turtles"""
    start=True

    for vals in dict.values():
        moves = "{}, {}".format(vals[0], vals[1])
        print(f"*** ENTER ANGLE, FORWARD MOVE : {moves}")

        if start:
            move_turtles(turtles, moves, start=True)
            start = False
        else:
            move_turtles(turtles, moves, start=False)

    qt_input('QUIT : [Enter]')
    quit()

def draw_from_manual(turtles):
    """ # manual draw """
    start = True

    while True:
        # CASE-01: correct moves     = Move, Angle
        # CASE_02: Incorrect moves   = Enter (blank), ?
        moves = qt_input('ENTER ANGLE, FORWARD MOVE : ')
        print(f"*** ENTER ANGLE, FORWARD MOVE : {moves}")

        if moves.startswith('?'):
            quit()

        if len(moves):
            move_turtles(turtles, moves, start=start)
            temp_moves = moves
            start = False
        else:
            move_turtles(turtles, temp_moves, start=False)

def move_turtles(turtles, moves, start=True):
    """ to move muti-turtles along w/ (angle,move)
    # move_turtles(turtles, moves, start=True):
    #  - turtles = list of turtle objects
    #  - moves   = input str 'angle,move' will be --> int (angle, move)
    #  - start   = if True, when First movements set
    #              radiation directions of each turtles by 360/n
    """
    angle, move = get_angle_move_from(moves)
    heads = [n for n in range(0, 361, int(360/NUM_TURTLES))]

    for i, tur in enumerate(turtles):
        if start:
            tur.setheading(heads[i])

        tur.left(angle) if angle > 0 else tur.right(abs(angle))
        tur.forward(move)

def get_angle_move_from(moves):
    """ to make str-moves into int(angle, move)
    # get_angle_move_from(moves):
    #  - return int (angle, move)
    """
    angle, move = moves.split(",")
    angle, move = angle.strip(), move.strip()
    return int(angle), int(move)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main()
    sys.exit(app.exec_())
{% endhighlight python linenos %}
