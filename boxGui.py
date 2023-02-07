import tkinter as tk



print("Enter Height:")
height = int(input())
print('Enter Width:')
width = int(input())


text_1=""
x=1
for i in range(height):
    if x==1:
        text_1 += (width*'*')
        x += 1
    elif x==height:
        text_1 += ('\n'+width*'*')
    else:
        text_1 += ('\n'+'*' + (width-2)*' '+ '*')
        x += 1


root = tk.Tk()
root.geometry('500x500')
root.title("My First Gui")

box=tk.Button(root, text=text_1, font=('Arial, 18'))
box.place(x=200, y=200, height=100, width=100)

root.mainloop()
