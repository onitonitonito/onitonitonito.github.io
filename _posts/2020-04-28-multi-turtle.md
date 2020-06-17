---
layout: post
title: Multiple Turtle Movements using QtPy5 UI 🐢
category: [turtle]
tag: drawing
comments : true
excerpt_separator: <!-- more -->
---
<!-- DACON 2020 TITLE -->

<!-- IT -->
<img width="125" align="left" style="padding: 0px 10px 0px 0px;" src="/images/post_img/20200428-00.png" >

'<b style="font-size: 1.8em;">The</b>'
python 'turtle' is a simple drawing tool which is based on one of the representative python GUI toolkits, 'tkinter'. It is simeple and easy to use so that many python trainee learns 'turtle' as one of the must-have-courses.

<!-- more -->



<br><br>

<!-- NARUTO SHADOW CLONE! -->
<img width="320" style="padding: 60px 0px 0px 10px;" align="right"
src="/images/post_img/20200428-01.png" >

<!-- The -->
'<b style="font-size: 1.8em;">Because</b>' the commands are so intuitive and simple like penup(), pendown(), many beginners are learn it through simple built-in IDE, or text editor. If you already learned it, are bored by simeple move and complicated input, why don't you try to multiple move of turtles and much beautiful choriographs. plus, let's try more of PyQt5, famous window GUI. let's gives turtle a shadow clone jutsu.



<br><br>

<!-- I -->
'<b style="font-size: 1.8em;">I</b>'
use the folder structure is as below, but you can change it. because I add another modules below 'k-mooc-reboot', I just set like this according to my coding note.

```python

  /[k-mook-reboot]
      |
      +-/[module_turtle]
        * turtles_multiple_moves.py
           |
           +-/[_assets]
           | * __init__.py
           | * _add_syspath_root.py
           | * modules_qt.py
           |
           +-/[_statics]
           | * turtle_echo.txt

```


<br><br>

<!-- I -->
'<b style="font-size: 1.8em;">I</b>'
__atteched gitGist, which will be located at the directory above__

1. turtles_mulple_moves.py - main
1. __ init __ is just a name-only file, blank inside.
1. _ add_syspath_root.py - to set full path or root.
1. modues_gt.py - QtPy5 class file.
1. turtle_echo.txt - pre-inputted coordination file.
  > * if you draw something by one-by-one input method, you just copy a commandline echo and make a text file.
  > * in the text file, there are blank inputs. it means skip an input (press-enter) which means use same former coordination. if there's no change to punch in, just press Enter.


<script src="https://bit.ly/3f16h9b"></script>

[[__GitGist Code__](https://bit.ly/3f16h9b)]: turtles_multiple_moves.py





<br><br>

<!-- How -->
'<b style="font-size: 1.8em;">How</b>'
__to stack multiple turtle drawing__

<img width="700" src="/images/post_img/20200428-02.png" />

* STEP.1 - draw something via dialog box using just 1 turtle.
* STEP.2 - drag command line, and make echo.txt file.
* STEP.3 - select pre-input option, draw it with multiple turtles.




<br><br>

<!-- The -->
'<b style="font-size: 1.8em;">The</b>'
__Exampes__

<img width="500" src="/images/post_img/20200428-03.png" />

<img width="500" src="/images/post_img/20200428-04.png" />




<br><br>

<!-- NARUTO SHADOW CLONE! - DIF-->
'<b style="font-size: 1.8em;">Naruto</b>'
__Shadow Clone Jutsu!__

[<img width="500" src="/images/post_img/20200428-ex1.gif" />](https://bit.ly/2WTouiy)

[[__REF:__] QUORA](https://bit.ly/2WTouiy)
