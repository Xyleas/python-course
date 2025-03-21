from tkinter import *

class MyApp:

    def __init__(self, root):
        
        root.title("My app")
        root.geometry("500x400")
        root.maxsize(1000,800)

        self.label_text = StringVar()
        label = Label(root, text="Some label text", textvariable=self.label_text)
        label.pack()

        # label["text"] = "New label text"
        # label["font"] = ("Courier", 40)

        label.configure(text = "New label text", font = ("Courier", 40))

        # entry_text = StringVar()
        self.entry_text = StringVar()
        entry = Entry(root, textvariable=self.entry_text)
        entry.pack() # Is placed below the label

        # label["textvariable"] = entry_text

        # Create a Button
        button = Button(root, text="Button text", command=press_button)
        button.pack()

        # Create Listbox
        self.list_item_strings = ["Hey", "Hi", "Hello", "Howdy", "Greetings"]
        list_items = StringVar(value=self.list_item_strings)
        self.listbox = Listbox(root, listvariable=list_items)
        listbox.pack()
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