import tkinter as tk
#import tkinter package.

root = tk.Tk()
#use tkinter as an object. Call its methods

root.geometry("500x500")
#root is the object name. Call tkinter methods on root

root.title("My First Gui")
#a title for the Gui

label = tk.Label(root, text="Hello World!", font=('Arial, 18'))
label.pack(padx=20, pady=20)
#you don't have to padx

textbox = tk.Text(root, height=3, font=('Arial, 16'))
textbox.pack(padx=10)

myentry = tk.Entry(root)
myentry.pack()

button = tk.Button(root, text='Click me!', font=('Arial, 18'))
button.pack(pady=10)

buttonframe = tk.Frame(root)
buttonframe.columnconfigure(0, weight=1)
buttonframe.columnconfigure(1, weight=1)
buttonframe.columnconfigure(2, weight=1)

btn1= tk.Button(buttonframe, text="1", font=('Arial, 18'))
btn1.grid(row=0, column=0, sticky=tk.W+tk.E)

btn2= tk.Button(buttonframe, text="2", font=('Arial, 18'))
btn2.grid(row=0, column=1, sticky=tk.W+tk.E)

btn3= tk.Button(buttonframe, text="3", font=('Arial, 18'))
btn3.grid(row=0, column=2, sticky=tk.W+tk.E)

btn4= tk.Button(buttonframe, text="4", font=('Arial, 18'))
btn4.grid(row=1, column=0, sticky=tk.W+tk.E)

btn5= tk.Button(buttonframe, text="5", font=('Arial, 18'))
btn5.grid(row=1, column=1, sticky=tk.W+tk.E)

btn6= tk.Button(buttonframe, text="6", font=('Arial, 18'))
btn6.grid(row=1, column=2, sticky=tk.W+tk.E)

buttonframe.pack(padx=5)
# or buttonframe.pack(fill='x')

anotherbtn= tk.Button(root, text="TEST", font=('Arial, 18'))
anotherbtn.place(x=200, y=400, height=100, width=100)
#place function

root.mainloop()
#mainloop creates the screen
