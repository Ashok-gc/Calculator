from _ast import Lambda
from tkinter import *
from PIL import ImageTk, Image

root = Tk()

#defining title of the project
root.title("Calculator")

e = Entry(root, text= " " ,relief=SUNKEN, width=20, borderwidth=12,font=("Verdana", 15), bg="gray70", insertwidth=4, justify=CENTER)
e.grid(row=0, column=0,columnspan=5, ipady=13)
# icon images
root.iconbitmap('D:/emoji.ico')


def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def button_clear():
    e.delete(0,END)

def button_add():
    first_number = e.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    e.delete(0, END)

def button_subtract():
    first_number = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_number)
    e.delete(0,END)

def button_multiply():
    first_number = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)
    e.delete(0,END)

def button_divide():
    first_number = e.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    e.delete(0,END)

def button_total():
    second_number = e.get()
    e.delete(0, END)
    if math == "addition":
        e.insert(0, f_num + int(second_number))
    if math == "subtraction":
        e.insert(0, f_num - int(second_number))
    if math == "multiplication":
        e.insert(0, f_num * int(second_number))
    if math == "division":
        e.insert(0, f_num / int(second_number))




# Defining the buttons
button_1 = Button(root, text="1", padx=20, pady=13, bd=5, fg="black", bg="gainsboro", font=("Helvetica", 14,"bold"), command=lambda : button_click(1))
button_2 = Button(root, text="2", padx=20, pady=13, bd=5, fg="black", bg="gainsboro", font=("Helvetica", 14,"bold"), command=lambda : button_click(2))
button_3 = Button(root, text="3", padx=20, pady=13, bd=5, fg="black", bg="gainsboro", font=("Helvetica", 14,"bold"), command=lambda : button_click(3))
button_4 = Button(root, text="4", padx=20, pady=13, bd=5, fg="black", bg="gainsboro", font=("Helvetica", 14,"bold"), command=lambda : button_click(4))
button_5 = Button(root, text="5", padx=20, pady=13, bd=5, fg="black", bg="gainsboro", font=("Helvetica", 14,"bold"), command=lambda : button_click(5))
button_6 = Button(root, text="6", padx=20, pady=13, bd=5, fg="black", bg="gainsboro", font=("Helvetica", 14,"bold"), command=lambda : button_click(6))
button_7 = Button(root, text="7", padx=20, pady=13, bd=5, fg="black", bg="gainsboro", font=("Helvetica", 14,"bold"), command=lambda : button_click(7))
button_8 = Button(root, text="8", padx=20, pady=13, bd=5, fg="black", bg="gainsboro", font=("Helvetica", 14,"bold"), command=lambda : button_click(8))
button_9 = Button(root, text="9", padx=20, pady=13, bd=5,fg="black", bg="gainsboro", font=("Helvetica", 14,"bold"), command=lambda : button_click(9))
button_0 = Button(root, text="0", padx=20, pady=13, bd=6, fg="black", bg="gainsboro", font=("Helvetica", 14,"bold"), command=lambda : button_click(0))
button_add =  Button(root, text="+", padx=20, pady=13, bd=6, fg="black", bg="snow4", font=("Verdana", 14,"bold"), command=button_add)
button_total =  Button(root, text="=", padx=20, pady=13, bd=6, fg="black", bg="orange", font=("Verdana", 14,"bold"), command=button_total)
button_clear =  Button(root, text="C", padx=20, pady=13, bd=6,fg="white", bg="slate gray4", font=("Verdana", 14,"bold"), command=button_clear)


button_subtract =  Button(root, text="-", padx=20, pady=13, bd=6, fg="black", bg="snow4", font=("Verdana", 14,"bold"), command=button_subtract)
button_multiply =  Button(root, text="*", padx=20, pady=13, bd=6, fg="black", bg="snow4", font=("Verdana", 14,"bold"), command=button_multiply)
button_divide =  Button(root, text="/", padx=20, pady=13, bd=6, fg="black", bg="snow4", font=("Verdana", 14,"bold"), command=button_divide)




#Putting buttons on the screen
button_1.grid(row=1, column=0)
button_2.grid(row=1, column=1)
button_3.grid(row=1, column=2)
button_add.grid(row=1, column=3)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_subtract.grid(row=2, column=3)

button_7.grid(row=3, column=0)
button_8.grid(row=3, column=1)
button_9.grid(row=3, column=2)
button_multiply.grid(row=3, column=3)

button_clear.grid(row=4, column=0)
button_0.grid(row=4, column=1)
button_total.grid(row=4, column=2)
button_divide.grid(row=4, column=3)




root.mainloop()