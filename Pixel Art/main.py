from tkinter import *
import tkinter.colorchooser
from PIL import ImageGrab
from datetime import datetime

def PixelApp:

    def __init__(self, root):
        self = self.root
        self.root.title("Pixel Art")

        cell_length = 50
        grid_width = 20
        grid_height = 10

        self.color_chooser = tkinter.colorchooser.Chooser(self.root)
        self.chosen_color = None
        self.is_pen_selected = False
        self.is_eraser_selected = False

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

        new_button = Button(control_frame, text = "New", command=self.press_new_button) #Passes the function as a reference.
        new_button.grid(column=0, row=0, columnspan=2, sticky=(N,S,E,W), padx = 5, pady = 5)

        save_button = Button(control_frame, text="Save", command=self.press_save_button)
        save_button.grid(column=2, row=0, columnspan=2, sticky=(N,S,E,W), padx = 5, pady = 5)

        self.pen_image = PhotoImage(file="pen.png").subsample(2,3)
        pen_button = Button(control_frame, text="Pen", image = self.pen_image, command=self.press_pen_button)
        pen_button.grid(column=8, row=0, columnspan=2, sticky=(N,S,E,W), padx = 5, pady = 5)

        self.erase_image = PhotoImage(file="erase.png").subsample(2,3)
        erase_button = Button(control_frame, text="Erase", image = self.erase_image, command=self.press_erase_button)
        erase_button.grid(column=10, row=0, columnspan=2, sticky=(N,S,E,W), padx = 5, pady = 5)

        self.selected_color_box = Frame(control_frame, borderwidth = 2, relief = "raised", bg="white")
        selected_color_box.grid(column=15, row=0, sticky=(N,E,S,W), padx = 7, pady = 7)

        pick_color_button = Button(control_frame, text = "Pick Color", command=self.press_pick_color_button)
        pick_color_button.grid(column=17, row=0, columnspan=3, sticky=(N,S,E,W), padx = 5, pady = 5)

        cols, rows = control_frame.grid_size()
        for col in range(cols):
            control_frame.columnconfigure(col, minsize=cell_length)
        control_frame.rowconfigure(row, minsize=cell_length)

    def tap_cell(self, event):
        widget = event.widget
        index = self.cells.index(widget)
        selected_cell = self.cells[index]
        if self.is_eraser_selected:
            selected_cell["bg"] = "white"
        if self.is_pen_selected and self.chosen_color != None:
            selected_cell["bg"] = self.chosen_color

    def press_new_button(self):
        for cell in self.cells:
            cell["bg"] = "white"
        self.chosen_color = None
        self.is_pen_selected = False
        self.is_eraser_selected = False
        self.selected_color_bot["bg"] = "white"

    def press_save_button(self):
        x = self.root.winfo_rootx() + self.drawing_grid.winfo_x()
        y = self.root.winfo_rooty() + self.drawing_grid.winfo_y() + 35 # May vary system to system

        _ = ImageGrab.grab(bbox=(x,y, width, height)).save(image_name) # Variable that we don't use(?)

        image_name = datetime.now().strftime("%Y-%m-%d-%H-%M-%S") + ".png"
        width = x + 2000
        height = y + 1000

    def press_pen_button(self):
        self.is_pen_selected = True
        self.is_eraser_selected = False

    def press_erase_button(self):
        self.is_pen_selected = False
        self.is_eraser_selected = True

    def press_pick_color_button(self):
        color_info = self.color_chooser.show()
        chosen = color_info[1]
        if chosen != None:
            self.chosen_color = chosen
            self.selevtec.color_box["bg"] = self.chosen_color

root = Tk()
PixelApp(root)
root.mainloop()
