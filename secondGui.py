import tkinter as tk
from tkinter import messagebox

class MyGui:

    def __init__(self):

        self.root = tk.Tk()
        
        self.menubar = tk.Menu(self.root)

        self.filemenu = tk.Menu(self.menubar, tearoff = 0)
        self.filemenu.add_command(label="Close", command=exit)

        self.menubar.add_cascade(menu = self.filemenu, label="File")
        self.menu= tk.Menu(self.menubar, tearoff = 0)

        self.root.config(menu=self.menubar)

        

        self.label = tk.Label(self.root, text="Your Message", font = ('Arial', 18))
        self.label.pack(padx=10, pady=10)

        self.textbox = tk.Text(self.root, height = 5, font = ('Arial', 18))
        self.textbox.bind("<KeyPress>", self.shortcut)
        self.textbox.pack(padx=10, pady=10)

        self.check_state= tk.IntVar()

        self.check = tk.Checkbutton(self.root, text = 'Show Messagebox', font = ('Arial', 18), variable = self.check_state)
        self.check.pack(padx=10, pady=10)

        self.button= tk.Button(self.root, text = 'Show Message', font= ('Arial', 18), command = self.show_message)
        self.button.pack(padx=10, pady=10)

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.mainloop()

    def show_message(self):
        if self.check_state.get() == 0:
            print(self.textbox.get('1.0', tk.END))
        else:
            messagebox.showinfo(title= 'Message', message=self.textbox.get('1.0', tk.END))
#print(self.check_state.get())- to see the true false value of the checkbox


    def shortcut(self, event):
        if event.state == 4 and event.keysym == 'Return':
            print('Hello')
#print(event) to see all the information about keys
#print(event.keysym)
#print(event.state) to get the values you need for key combination

    def on_closing(self):
        if messagebox.askyesno(title = 'Quit', message = 'Do you really want to quit?'):
            self.root.destroy()




MyGui()

#on you own- make it so you can press ESC button to escape
#implement function- outputs textmessage in console when you press control enter
#34:35
