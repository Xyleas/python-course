from tkinter import *
import tkinter as tk # This lets us shorten tkinter to tk in method calls.

class ToDoItem:

    def __init__(self, name, description):
        self.name = name
        self.description = description

class ToDoListApp:

    def __init__(self, root):
        
        root.title("To Do List")
        
        frame = Frame(root,borderwidth=2, relief="sunken")
        frame.grid(column=1,row=1, sticky=(N, E, S, W))
        root.columnconfigure(1, weight=1)
        root.rowconfigure(1, weight=1)

        list_label = Label(frame, text="To Do Items")
        list_label.grid(column=1, row=1, sticky=(S,W))

        self.to_do_items = [
            ToDoItem("Workout", "Push ups, pull ups, squats"),
            ToDoItem("House work", "Clean kitchen, sweep floors, do laundry"),
            ToDoItem("Groceries", "Buy bread, milk, eggs")
        ]
        self.to_do_names = StringVar(value=list(map(lambda x: x.name, self.to_do_items)))
        items_list = Listbox(frame, listvariable=self.to_do_names)
        items_list.bind("<<ListboxSelect>>", lambda s: self.select_item(listbox.curselection()))
        items_list.grid(column=1, row=2, sticky= (E, W))

        self.selected_description = StringVar()
        selected_description_label = Label(frame, textvariable=self.selected_description )
        selected_description_label.grid(column=1, row=3, sticky= (E, W))

        self.label_text = StringVar()
        label = Label(frame, text="Some label text", textvariable=self.label_text)
        # label.pack(side=tk.LEFT, padx=40, pady=20)
        # label.grid(column=1, row=1)
        # label["text"] = "New label text"
        # label["font"] = ("Courier", 40)

        label.configure(text = "New label text", font = ("Courier", 40))

        # entry_text = StringVar()
        self.entry_text = StringVar()
        entry = Entry(frame, textvariable=self.entry_text)
        # entry.pack(side=tk.LEFT) # Is placed below the label
        # entry.place(x=100, y=50)
        # entry.grid(column = 2, row=1)

        # label["textvariable"] = entry_text

        # Create a Button
        button = Button(frame, text="Button text", command=press_button)
        # button.place(x=0,y=0)
        # button.configure(width=10,height=1, font=(Courier, 40))
        # button.pack(side=tk.LEFT)
        # button.grid(column=1, row=2, sticky=(S, E, W))

        
    def press_button(self):
        text = self.entry_text.get()
        self.label_text.set(text)
        listbox.insert(END, text)

    def select_item(self, index):
        # selected_item = self.to_do_names[index[0]]
        # print(selected_item)



root = TK()
ToDoListApp(root)
root.mainloop()