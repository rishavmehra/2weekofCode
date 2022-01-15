print("Day4")

# import random
# random_integer=random.randint(1,10)
# print(random_integer)

# random_float=random.random(0-5)
# print(random_float)


# import random
# test_seed=int(input("Create a Seed number:"))
# random.seed(test_seed)
# random_int=random.randint(0,1)
# if random_int==0:
#     print("Heads")
# else:
#     print("Tails")


# Who's Paying
# import random
# test_seed=int(input("Create a Seed number:"))
# random.seed(test_seed)
# names_string = input("Give me everybody's names, separated by a comma. ")
# names = names_string.split(", ")
# num_items=len(names)
# random_name= random.randint(0,num_items-1)
# results=names[random_name]
# # result=(random.choice(names))
# # print(f"{result} is going to buy the meal today!")
# print(results,"is going to buy the meal today!")

# # Treasure Map
# row1 = ["⬜️","⬜️","⬜️"]
# row2 = ["⬜️","⬜️","⬜️"]
# row3 = ["⬜️","⬜️","⬜️"]
# map = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
# position = input("Where do you want to put the treasure? ")
# horizontal=int(position[0])
# vertical=int(position[1])
# map[vertical-1][horizontal-1]="X"
# print(f"{row1}\n{row2}\n{row3}")


#Rock Scissors Paper
import random
print("Hey it's Day 4: \U0001f603")
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_list=[rock,paper,scissors]
options=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
print(game_list[options])
# if options==0:
#     print(rock)
# elif options==1:
#     print(paper)
# elif options==2:
#     print(scissors)
# else:
#     print("Wrong Choice")

computer=random.randint(0,2)
print("Computer Choice:")
print(game_list[computer])
# print(computer)
# if computer==0:
#     print(rock)
# elif computer==1:
#     print(paper)
# elif computer==2:
#     print(scissors)
# else:
#     print("Wrong Choice")


if options>=3 or options<0:
  print("You type invaild Number")
elif options==0 and computer==2:
  print("You Win!")
elif options==2 and computer==0:
  print("You Lose!")
elif computer>options:
  print("You Lose!")
elif options>computer:
  print("You Win")
elif options==computer:
  print("Draw")
# elif options==1 and computer==0:
#   print("You Win!")
# elif options==2 and computer==1:
#   print("You Win")


