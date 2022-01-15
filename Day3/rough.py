# print("Day3")

#RollerCoaster with Height
# print("RollerCoaster Check")
# height = int(input("what is your Height in cm: "))
# if height > 120:
#     print("You can Ride rollercoaster")
# else:
#     print("Sorry, You have to grow taller before you can ride.")


#1Even And Odd Check
# print("odd and Even Check")
# number = int(input("Which number do you want to check? "))
# if (number % 2) ==0:
#     print("no. is even")
# else:  
#     print("no. is odd")

#RollerCoaster With Age Nestes if else
# print("RollerCoaster Check")
# height = int(input("what is your Height in cm: "))
# if height >= 120:
#     print("You can Ride rollercoaster")
#     age=int(input("What is the age: "))
#     if age <= 18:
#         print("Pay $7")
#     else:
#         print("Pay $12")
# else:
#     print("Sorry, You have to grow taller before you can ride.")


#RollerCoaster With Age elif
# print("RollerCoaster Check")
# height = int(input("what is your Height in cm: "))
# if height >= 120:
#     print("You can Ride rollercoaster")
#     age=int(input("What is the age: "))
#     if age < 12:
#         print("Pay $5")
#     elif age <= 18:
#         print("Pay $7")
#     else:
#         print("Pay $12")
# else:
#     print("Sorry, You have to grow taller before you can ride.")


#BMI Calculator
# height = float(input("enter your height in m: "))
# weight = float(input("enter your weight in kg: "))
# BMI = weight / height**2
# Result=int(BMI)

# if BMI < 40:
#     if BMI <18:
#         print(f"Your {Result} is,you are underweight.")
#     elif BMI < 22:
#         print(f"Your {Result} is, you have a normal weight.")
#     elif BMI< 28:
#         print(f"Your {Result} is, you are slightly overweight.")
#     elif BMI< 33:
#         print(f"Your {Result} is, you are obese.")
# else:
#     print(f"Your {Result} is, you are clinically obese.")


#Leap Year Excercise

# year = int(input("Which year do you want to check? "))

# # if  ((year%400==0)or(year%100!=0)and (year%4==0)):
# #     print("given no. is Leap Year")
# # else:
# #     print("Given Year is not leap year")

# if year %4==0:
#     if year%100==0:
#         if year%400==0:
#             print("leap Year")
#         else:
#             print("NOt a Leap year")
#     else:
#         print("leap year")
# else:
#     print("NOt a Leap Year")


# #RollerCoaster With Multiple If Statements in Succession
# print("RollerCoaster Check")
# height = int(input("what is your Height in cm: "))
# bill=0
# if height >= 120:
#     print("You can Ride rollercoaster!")
#     age=int(input("What is the age: "))
#     if age < 12:
#         bill=5
#         print("child tickets are $5")
#     elif age <= 18:
#         bill=7
#         print("Youth tickets are $7")
    
#     else:
#         bill=12
#         print("Adult tickets are $12")

#     want_photo=input("do you want photo? Y or N ")
#     if want_photo=="Y":
#         bill += 3
#     print(f"Your Total Bill is ${bill}")
# else:
#     print("Sorry, You have to grow taller before you can ride.")


# #Python Pizza Deliveries!
# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M, or L ")
# add_pepperoni = input("Do you want pepperoni? Y or N ")
# extra_cheese = input("Do you want extra cheese? Y or N ")
# bill=0

# if size=="S":
#     bill+=15
# elif size=="M":
#     bill+=20
# elif size=="L":
#     bill+=25

# else:
#     print("we can understand your request")

# if add_pepperoni=="Y":
#     if size=="S":
#         bill += 2
#     else:
#         bill +=3


# if extra_cheese=="Y":
#     bill += 1

# print(f"Your Final Bill is ${bill}")

# #RollerCoaster With logical operator 
# print("RollerCoaster Check")
# height = int(input("what is your Height in cm: "))
# bill=0
# if height >= 120:
#     print("You can Ride rollercoaster!")
#     age=int(input("What is the age: "))
#     if age < 12:
#         bill=5
#         print("child tickets are $5")
#     elif age <= 18:
#         bill=7
#         print("Youth tickets are $7")
#     elif (age>=45) and (age<=55):
#         bill=0
#         print("Everything is Going to OK. have free ride on us!")
#     else:
#         bill=12
#         print("Adult tickets are $12")

#     want_photo=input("do you want photo? Y or N ")
#     if want_photo=="Y":
#         bill += 3
#     print(f"Your Total Bill is ${bill}")
# else:
#     print("Sorry, You have to grow taller before you can ride.")


# # Love calculator
# print("Welcome to the Love Calculator!")
# name1 = input("What is your name? \n")
# name2 = input("What is their name? \n")

# name = name1 + name2
# # print(name)
# lower=name.lower()
# c=("t","r","u","e")
# count=0
# for i in lower:
#   if str(i) in c:
#     count += 1
# # print(count)

# lower1=name.lower()
# d=("l","o","v","e")
# count1=0
# for i in lower1:
#   if str(i) in d:
#     count1 += 1
# # print(count1)
# result= str(count)+str(count1)
# result1=int(result)
# print(result1)


# if (result1 <= 10) or (result1 >=90):
#   print(f"Your score is {result}, you go together like coke and mentos.")
# elif (result1>=40) and (result1<=50):
#   print(f"Your score is {result1}, you are alright together.")
  
# else:
#   print(f"Your score is {result1}")
# # name1 = "Kanye West"
# # name2 = "Kim Kardashian"


##treasure-island-start
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 


choice1= input('You\'re at a crossroad. Where do you want to go? Type "left" or "right"').lower()

if choice1 == "left":
    choice2=input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.').lower()
    if choice2=="wait":
        choice3=input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?").lower()
        if choice3=="red":
            print("It's a room full of fire. Game Over.")
        elif choice3=="yellow":
            print("You found the treasure! You Win!")
        elif choice3=="blue":
            print("You enter a room of beasts. Game Over.") 
        else:
            print("You chose a door that doesn't exist. Game Over.")
    else:
        print("Attack by the trout, Game Over")
else:
    print("You fell into hole, Game Over")

