
#Question 21
#Level 3
#
#Question£º
#A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps. The trace of robot movement is shown as the following:
#UP 5
#DOWN 3
#LEFT 3
#RIGHT 2
#¡­
#The numbers after the direction are steps. Please write a program to compute the distance from current position after a sequence of movement and original point. If the distance is a float, then just print the nearest integer.
#Example:
#If the following tuples are given as input to the program:
#UP 5
#DOWN 3
#LEFT 3
#RIGHT 2
#Then, the output of the program should be:
#2
#
#Hints:
#In case of input data being supplied to the question, it should be assumed to be a console input.

pos_x = 0
pos_y = 0
while True:
    s = input()
    if not s:
        break
    pos = s.split(' ')
    pos_type = pos[0]
    val = int(pos[1])
    if pos_type == 'UP':
        pos_x += val
    elif pos_type == 'DOWN':
        pos_x -= val
    elif pos_type == 'RIGHT':
        pos_y += val
    elif pos_type == 'LEFT':
        pos_y -= val
    else:
        pass
pos_fin = (str(pos_x), str(pos_y))
print(','.join(pos_fin))

