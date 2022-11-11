from art import logo
from replit import clear

def add(n1,n2):
    """
    This function adds two numbers
    and return the summed value
    """
    return n1 + n2

def subtract(n1,n2):
    """
    This function subtract two numbers
    and return the result
    """
    return n1 - n2

def multiply(n1,n2):
    """
    This function multiply two numbers
    and return their multiplication
    """
    return n1 * n2

def divide(n1,n2):
    """
    This function divides the first number
    with the second numbers
    and return their division
    """
    return n1/n2

def continue_calculation(ans=""):
    """
    this function is used to ask if
    user wants to continue using calculator
    :param ans:
    :return: "y","yes","n","no"
    """
    while not ans.lower() in ["y","yes","n","no"]:
        ans=input("continue calculating? y/n ")
        if not ans.lower() in ["y","yes","n","no"]:
            print("please enter a correct character")
    return ans

def use_prev_answer(cont=""):
    """
    this function asks the user
    if the user wants to use previously
    calculated result in next calculation
    :param cont:
    :return: "y", "yes", "n", "no"
    """
    while not cont.lower() in ["y", "yes", "n", "no"]:
        cont = input(f"continue using answer value {answer} ? y/n ")
        if not cont.lower() in ["y", "yes", "n", "no"]:
            print("Please enter a correct character ")
    return cont

def get_num1(cont,answer):
    """
    get the first number
    :param cont:
    :param answer:
    :return:
    """
    if cont in ["no", "n"]:
        clear()
        print(logo)
        num1 = float(input("What is the first number  : "))
    else:
        num1 = answer
    return num1

def get_num2():
    """
    get the second number
    :param cont:
    :param answer:
    :return:
    """
    num2 = float(input("What is the second number : "))
    return num2

def get_operator(operations={},operator_symbol=""):
    """
    gets the operator used to calculate
    :param operations:
    :param operator_symbol:
    :return: +, -, *, /
    """
    while not operator_symbol in operations.keys():
        operator_symbol=input(f"Which operator will you use: {[i for i in operations.keys()]} : ")
        if not operator_symbol in operations.keys():
            print("please enter a correct symbol ")
    return operator_symbol

def perform_calculation_print_answer(operations={},operator_symbol="",num1=0,num2=0):
    calculation_function = operations[operator_symbol]
    answer = calculation_function(num1, num2)
    print(f"{num1} {operator_symbol} {num2} = {answer}")
    return answer

operations ={
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide
}
operator_symbol = ""
calculate= True
ans=""
cont = "n"
answer = 0

print(logo)



while calculate:

    num1 = get_num1(cont, answer)
    operator_symbol = get_operator(operations)
    num2 = get_num2()
    answer = perform_calculation_print_answer(operations, operator_symbol, num1, num2)

    ans = continue_calculation().lower()

    if ans in ["n", "no"]:
        calculate = False
        print("Thank you, bye bye")
        break
    elif ans in ["y", "yes"]:
        cont = use_prev_answer().lower()




