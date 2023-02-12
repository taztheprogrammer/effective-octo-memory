import tkinter as tk

root = tk.Tk()
root.title("Calculator")

e = tk.Entry(root)
e.grid(row=0, column=0, padx=10, pady=5, columnspan=3)
#e.insert(0, "Enter Your Name:")

def click():
    pass

b1= tk.Button(root, text="1", padx=40, pady=20, command=click)
b2= tk.Button(root, text="2", padx=40, pady=20, command=click)
b3= tk.Button(root, text="3", padx=40, pady=20, command=click)
b4= tk.Button(root, text="4", padx=40, pady=20, command=click)
b5= tk.Button(root, text="5", padx=40, pady=20, command=click)
b6= tk.Button(root, text="6", padx=40, pady=20, command=click)
b7= tk.Button(root, text="7", padx=40, pady=20, command=click)
b8= tk.Button(root, text="8", padx=40, pady=20, command=click)
b9= tk.Button(root, text="9", padx=40, pady=20, command=click)
b0= tk.Button(root, text="0", padx=40, pady=20, command=click)

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



root.mainloop()
