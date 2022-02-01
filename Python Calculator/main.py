#this is the main function
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from math_functions import *

# declare the window
window = tk.Tk()

# set window title
window.title("DS Calculator")

# set window width and height
window.geometry("500x500")

#creating some basic elements
first_label = tk.Label(text = "First input:")
first_input = tk.Entry()

second_label = tk.Label(text = "Second input:")
second_input = tk.Entry()

choose_label = tk.Label(text = "Choose the function you'd like to use:")

#packing those basic elements
first_label.pack(fill='x', padx=5, pady=(10,5))
first_input.pack(fill='x', padx=5, pady=(5,30))
second_label.pack(fill='x', padx=5, pady=5)
second_input.pack(fill='x', padx=5, pady=(5, 30))
choose_label.pack(fill='x', padx=5, pady=5)

##################################################
#function that displays a message with the answer#
##################################################
def show_answer():

    a = int(first_input.get())
    b = int(second_input.get())

    toShow = "null"

    if(selected_function.get() == "Add"):
        toShow = "The answer is " + str(add(a,b))

    if(selected_function.get() == "Subtract"):
        toShow = "The answer is " + str(subtract(a,b))
    
    if(selected_function.get() == "Multiply"):
        toShow = "The answer is " + str(multiply(a,b))

    if(selected_function.get() == "Divide"):
        toShow = "The answer is " + str(divide(a,b))

    if(selected_function.get() == "Power"):
        toShow = "The answer is " + str(pow(a,b))

    showinfo(
        title = "Result",
        message = toShow
        
    )


functions = ["Add", "Subtract",  "Multiply" , "Divide", "Power"]

selected_function = tk.StringVar()

# radio buttons
for function in functions:
    r = ttk.Radiobutton(
        window,
        text = function,
        value = function,
        variable = selected_function
    )
    r.pack(fill='x', padx=5, pady=5)


# button
button = ttk.Button(
    window,
    text = "Get the answer",
    command = show_answer)

button.pack(fill='x', padx=5, pady=(10,5))


#Equation solving part
equation_label = tk.Label(text = "Put an equation you'd like to solve here:")
equation_input = tk.Entry()

equation_label.pack(fill='x', padx=5, pady=5)
equation_input.pack(fill='x', padx=5, pady=5)

button2 = ttk.Button(
    window,
    text = "Get the answer",
    command = showinfo(
        title = "Equation Result",
        message = "X is " + str(solve_equation(equation_input.get()))
        
    ))

button2.pack(fill='x', padx=5, pady=(10,5))



# set window background color
window.configure(bg='lightgray')
window.mainloop()