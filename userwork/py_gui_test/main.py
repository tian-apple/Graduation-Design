import tkinter as tk
import son


class main:
    def __init__(self):
        self.master = tk.Tk()
        self.master.title('Main Window')
        tk.Button(self.master, text='Create Child Window',
                  command=self.create_child_window).pack()

    def create_child_window(self):
        son.son(self.master)


if __name__ == '__main__':
    main()
    tk.mainloop()
