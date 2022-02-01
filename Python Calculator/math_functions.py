import itertools
from utils import *

#add function, adds a and b
def add(a, b):
    return a + b

#subtract function, subtracts b from a
def subtract(a, b):
    return a - b

#divide function, divides a by b
def divide(a, b):
    return a/b

#multiply function, multiplies b by a
def multiply(a, b):
    return a * b

#power function, returns a to the power of b
def pow(a,b):
    if(b == 0):
        return 1

    if(b == 1):
        return a

    count = 1
    answer = a
    while(count != b):
        answer = answer * a
        count += 1

    return answer

#function that solves a string equation recieved,"0 = X + 5"
def solve_equation(equation):
    count_positive = 0
    count_nagative = 0
    count_positive_numbers = 0
    count_nagative_numbers = 0

    new_equation = erase_space(equation)

    for idx, char in enumerate(new_equation):
        if((char == 'X') or (char == 'x')):
             if((char[idx - 1] == '+') or (char[idx - 1] == '=') ):
                    count_positive += 1
             if(char[idx -1] == '-'):
                    count_nagative += 1

        if((char != 'X') and (char != 'x') and (char != '=') and (char != '-') and (char != '+')):
            if(char[idx - 1] == '+'):
                    count_positive_numbers += 1
            if(char[idx -1] == '-'):
                    count_nagative_numbers += 1

    X = count_positive - count_nagative
    numbers = count_positive_numbers - count_nagative_numbers

    if(X == 0):return "error"

    if(X > 0 ):
        result = -(divide(numbers,X))
        return result

    if(X < 0):
        result = (divide(numbers,X))
        return result
    
    return 0

#function that recieves an equation, "Y = X + 2", and an X, and returns Y
def solve_y(equation, y):
    return 0