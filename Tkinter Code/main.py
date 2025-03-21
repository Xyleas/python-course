from tkinter import *

class MyApp:

    def __init__(self, root):
        
        root.title("My app")
        root.geometry("500x400")
        root.maxsize(1000,800)

        label = Label(root, text="Some label text")
        label.pack()


root = TK()
MyApp(root)
root.mainloop()