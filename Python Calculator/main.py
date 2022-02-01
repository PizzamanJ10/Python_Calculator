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


#function that displays a message with the answer
def show_answer():

    a = 100
    b = 20

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

button.pack(fill='x', padx=5, pady=5)

# set window background color
window.configure(bg='lightgray')
window.mainloop()