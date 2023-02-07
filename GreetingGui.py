
import tkinter as tk

root= tk.Tk()
root.title("GreetingGui")
root.geometry("500x500")
#creating the actual box

def click():
    label = tk.Label(root, text = "Hello " +textbox.get()).pack()

label=tk.Label(root, text="Enter Your Name").pack()

textbox= tk.Entry(root, bg="White", fg="black")
textbox.pack()
textbox.insert(0, "Enter your name:")
#the second thing (.pack) must be on a second line. IDK why yet

btn= tk.Button(root, text="Click Me!", fg ="red", command=click).pack()











root.mainloop()
