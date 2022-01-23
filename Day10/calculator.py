
from ast import operator
from art import logo



def add(n1,n2):
    return n1+n2
def subtract(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1*n2
def division(n1,n2):
    return n1/n2

cal_dic={
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":division,
}
def calculator():
    print(logo)
    num1=int(input("What's the First Number: "))
    for symbol in cal_dic:
        print(symbol)
    should_continue=True

    while should_continue:
        operation_symbol=input("Pick An Operations: ")
        num2=int(input("What's the next Number: "))
        cal_function=cal_dic[operation_symbol]  
        answer=cal_function(num1,num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer}, or type 'n'  to start new calculation ")=="y":
            num1=answer
        else:
            should_continue=False
            calculator()
calculator()