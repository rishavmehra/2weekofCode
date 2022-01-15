# two_digit_number = input("Type a two digit number: ")

# sum=int(two_digit_number[0]) + int(two_digit_number[1])
# print(sum)

#Maths Operators
# print(3*(3+3)/3-3)

# BMI calculcator
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
BMI = float(weight)/float(height)**2
print("result is:",int(BMI))




#your life in weeks
# age = input("What is your current age?")
# years=90-int(age)
# days= 365 * int(years)
# weeks = 52 * int(years)
# months= 12 * int(years)
# message= f"You have {days} days, {weeks} weeks, and {months} months left."
# print(message)

# print("Welcome to the tip Calculator")
# bill=input("what was the total bill? $")
# percentage=input("How much tip would you like to give? 10, 12, or 15?")
# people=input("How many people to split the bill? $")
# per_12= int(percentage)/100*int(bill)
# total=per_12+int(bill)
# total_bill=total/int(people)
# print(round(total_bill, 2))




# print("Welcome to the tip Calculator")
# bill=float(input("what was the total bill? $"))
# tip=int(input("How much tip would you like to give? 10, 12, or 15?"))
# people=int(input("How many people to split the bill? $"))
# total_bill= tip/100 * bill + bill
# bill_per_head= total_bill/people
# result=round(bill_per_head, 2)
# print(f"Each person should pay: ${result}")