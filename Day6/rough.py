##Hurdle1 reetorg
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
# def jump():
#     move()
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()
# for x in range(6):
#     jump()

# #Hurdle2 reetorg
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
# def jump():
#     move()
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()
# while not at_goal():
#     jump()



# #Hardle3
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
# def jump():
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()
    
# while not at_goal():
#     if front_is_clear():
#         move()
#     elif wall_in_front():
#         jump()

# # #Hardle4
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
# def jump():
#     turn_left()
#     while wall_on_right():
#         move()
#     turn_right()
#     move()
#     turn_right()
#     while front_is_clear():
#         move()
#     turn_left()
# while not at_goal():
#     if front_is_clear():
#         move()
#     elif wall_in_front():
#         jump()


# #maze
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
# while front_is_clear():
#     move()
# turn_left()
# while not at_goal():
#     if front_is_clear() and wall_on_right():
#         move()
#     elif front_is_clear() and right_is_clear():
#         turn_right()
#         move()
#     elif front_is_clear():
#         move()
#     elif wall_in_front() and right_is_clear():
#         turn_right()
#         move()
#     else:
#         turn_left()

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(raw_input().strip())

if n %2!=0:
    print("Weird")
if n%2==0 and range(2,5):
    print("Not Weird")
if n%2==0 and range(6,20):
    print("Weird")
if n%2==0 and n>20:
    print("Weird")