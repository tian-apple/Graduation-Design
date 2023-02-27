import tkinter as tk

class son:
    def __init__(self, master):
        self.master = master
        self.child_window = tk.Toplevel(self.master)
        self.child_window.geometry('200x200+400+300')
        self.child_window.title('Child Window')
        tk.Label(self.child_window, text='Child Window Content').pack()
    
