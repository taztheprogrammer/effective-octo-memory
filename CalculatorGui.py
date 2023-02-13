//Calculator Gui

import tkinter as tk

root = tk.Tk()
root.title("Calculator")

e = tk.Entry(root)
e.grid(row=0, column=0, padx=10, pady=5, columnspan=3)
#e.insert(0, "Enter Your Name:")

def click(number):
    #e.delete(0, 10)
    t = e.get()
    t += str(number)
    e.delete(0, 100)
    e.insert(0, t)

def add():
    global t
    t = str(e.get())+" + "
    e.delete(0, 25)


def equals():
    answer = eval(t + str(e.get()))
    e.delete(0, 25)
    e.insert(0, answer)

def clear():
    e.delete(0, 100)

b1= tk.Button(root, text="1", padx=40, pady=20, command=lambda: click(1))
b2= tk.Button(root, text="2", padx=40, pady=20, command=lambda: click(2))
b3= tk.Button(root, text="3", padx=40, pady=20, command=lambda: click(3))
b4= tk.Button(root, text="4", padx=40, pady=20, command=lambda: click(4))
b5= tk.Button(root, text="5", padx=40, pady=20, command=lambda: click(5))
b6= tk.Button(root, text="6", padx=40, pady=20, command=lambda: click(6))
b7= tk.Button(root, text="7", padx=40, pady=20, command=lambda: click(7))
b8= tk.Button(root, text="8", padx=40, pady=20, command=lambda: click(8))
b9= tk.Button(root, text="9", padx=40, pady=20, command=lambda: click(9))
b0= tk.Button(root, text="0", padx=40, pady=20, command=lambda: click(0))
b_add= tk.Button(root, text="+", padx=40, pady=20, command=click)
b_clear= tk.Button(root, text="c", padx=40, pady=20, command=click)
b_equal= tk.Button(root, text="=", padx=40, pady=20, command=click)

b1.grid(row=4, column=0)
b2.grid(row=4, column=1)
b3.grid(row=4, column=2)

b4.grid(row=3, column=0)
b5.grid(row=3, column=1)
b6.grid(row=3, column=2)

b7.grid(row=2, column=0)
b8.grid(row=2, column=1)
b9.grid(row=2, column=2)

b0.grid(row=5, column=0)
b_add.grid(row=5, column=1)
b_clear.grid(row=5, column=2)

b_equal.grid(row=6, column=0)



root.mainloop()
