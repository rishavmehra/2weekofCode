#Day5/100 #100daysofCode #Loops

# fruits=["Apple","Peach","Pear"]
# for fruit in fruits:
#     print(fruit)

# #Average Height
# student_heights = input("Input a list of student heights ").split()
# for n in range(0, len(student_heights)):
#   student_heights[n] = int(student_heights[n])
# # print(student_heights)
# add=0
# count=0
# for x in student_heights:
#     add += x
# # print(add)
# count=0
# for y in student_heights:
#     count += 1
# # print(count)
# final=add/count
# print(round(final))

        # #OR
        # for x in student_heights:
        #     add += x
        #     count += 1
        # final=add/count
        # print(round(final))


# #Highest Score
# student_scores = input("Input a list of student scores ").split()
# for n in range(0, len(student_scores)):
#   student_scores[n] = int(student_scores[n])
# print(student_scores)
# largest=student_scores[0]
# for large in student_scores:
#         if large > largest:
#                 largest=large

# print(f"The highest score in the class is:{largest}")

# total=0
# for x in range(0,101,2):
#         total += x
# print(total)

# #FizzBuzz
# for x in range(1,101):
#   if x % 3 ==0 and x % 5==0:
#     print("FizzBuzz")
#   elif x % 3==0:
#     print("Fizz")
#   elif x % 5==0:
#     print("Buzz")
#   else:
#     print(x)

#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password_list=[]
for char in range(1,nr_letters,+1):
        password_list.append(random.choice(letters))
for char in range (1,nr_numbers,+1):
        password_list.append(random.choice(numbers))
for char in range (1,nr_symbols,+1):
        password_list.append(random.choice(symbols))
# print(password_list)
random.shuffle(password_list)
# print(password_list)

password=""
for char in password_list:
        password +=char
print(f"Your Password is:{password}")

