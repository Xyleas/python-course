from tkinter import *
import tkinter as tk # This lets us shorten tkinter to tk in method calls.

class MyApp:

    def __init__(self, root):
        
        root.title("My app")
        # root.geometry("500x400")
        # root.maxsize(1000,800)

        self.label_text = StringVar()
        label = Label(root, text="Some label text", textvariable=self.label_text)
        # label.pack(side=tk.LEFT, padx=40, pady=20)
        label.grid(column=1, row=1)
        # label["text"] = "New label text"
        # label["font"] = ("Courier", 40)

        label.configure(text = "New label text", font = ("Courier", 40))

        # entry_text = StringVar()
        self.entry_text = StringVar()
        entry = Entry(root, textvariable=self.entry_text)
        # entry.pack(side=tk.LEFT) # Is placed below the label
        # entry.place(x=100, y=50)
        entry.grid(column = 2, row=1)

        # label["textvariable"] = entry_text

        # Create a Button
        button = Button(root, text="Button text", command=press_button)
        # button.pack(side=tk.LEFT)
        button.grid(column=1, row=2)

        # Create Listbox
        self.list_item_strings = ["Hey", "Hi", "Hello", "Howdy", "Greetings"]
        list_items = StringVar(value=self.list_item_strings)
        self.listbox = Listbox(root, listvariable=list_items)
        # listbox.pack(side=tk.BOTTOM)
        listbox.grid(column=2,row=2)
        listbox["height"] = 3
        listbox.bind("<<ListboxSelect>>", lambda s: self.select_item(listbox.curselection()))

    def press_button(self):
        text = self.entry_text.get()
        self.label_text.set(text)
        listbox.insert(END, text)

    def select_item(self, index):
        selected_item = self.list_item_strings[index[0]]
        print(selected_item)

root = TK()
MyApp(root)
root.mainloop()