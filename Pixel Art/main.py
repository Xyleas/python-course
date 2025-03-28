from tkinter import *

def PixelApp:

    def __init__(self, root):
        self = self.root
        self.root.title("Pixel Art")

        cell_length = 50
        grid_width = 20
        grid_height = 10

        self.drawing_grid = Canvas(self.root)
        self.drawing_grid.grid(column=0, row=0, sticky=(N,S,E,W))

        self.cells = []

        for i in range(grid_width):
            for j in range(grid_height):
                cell = Frame(self.drawing_grid, width = cell_length, height = cell_length, bg = "white", highlightbackground="black", highlightcolor="black", highlightthickness=1)
                cell.grid(column=i, row=j)
                cell.bind('<Button-1>', self.tap_cell)
                self.cells.append(cell)

        control_frame = Frame(self.root, height = cell_length)
        control_frame.grid(column=0, row=1, sticky=(N,S,E,W))

        new_button = Button(control_frame, text = "New")
        new_button.grid(column=0, row=0, columnspan=2)

        save_button = Button(control_frame, text="Save")
        save_button.grid(column=2, row=0, columnspan=2)

        pen_button = Button(control_frame, text="Pen")
        pen_button.grid(column=8, row=0, columnspan=2)

        erase_button = Button(control_frame, text="Erase")
        erase_button.grid(column=10, row=0, columnspan=2)

        selected_color_box = Frame(control_frame, borderwidth = 2, relief = "raised", bg="white")
        selected_color_box.grid(column=15, row=0, sticky=(N,E,S,W))

        pick_color_button = Button(control_frame, text = "Pick Color")
        pick_color_button.grid(column=17, row=0, columnspan=3)

        cols, rows = control_frame.grid_size()
        for col in range(cols):
            control_frame.columnconfigure(col, minsize=cell_length)
        control_frame.rowconfigure(row, minsize=cell_length)

    def tap_cell(self, event):
        print("Cell tapped")

root = Tk()
PixelApp(root)
root.mainloop()
