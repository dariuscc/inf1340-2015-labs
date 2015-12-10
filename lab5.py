#!/usr/bin/env python3

""" GUI for Name that Shape """

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"

from name_that_shape import *
import Tkinter
import tkMessageBox

"""
   Create a GUI for the Name That Shape program
   See name_shape_gui.png for specification
   Use the name_that_shape.py to perform computations
   For inputs that raise an error, pop up a modal dialog box
   For inputs that produce a shape name, display the string in the window
"""

triangle = "3"
square = "4"
pentagon = "5"
hexagon = "6"
heptagon = "7"
octagon = "8"
nonagon = "9"
decagon = "10"

def name_that_shape(shape_edges):
    shape_text = ""  # Initialize variable
    if shape_edges == triangle:  # match the number of sides to the shape
        shape_text = "triangle"  # store the name of the shape
    elif shape_edges == square:
        shape_text = "quadrilateral"
    elif shape_edges == pentagon:
        shape_text = "pentagon"
    elif shape_edges == hexagon:
        shape_text = "hexagon"
    elif shape_edges == heptagon:
        shape_text = "heptagon"
    elif shape_edges == octagon:
        shape_text = "octagon"
    elif shape_edges == nonagon:
        shape_text = "nonagon"
    elif shape_edges == decagon:
        shape_text = "decagon"
    else:
        raise ValueError
    return shape_text

class NameThatShapeGUI:
    def __init__(self):
        # Create the main window widget
        self.main_window = Tkinter.Tk()
        self.main_window.geometry('500x100')

        # Create two frames to group widgets
        self.top_frame = Tkinter.Frame(self.main_window)
        self.middle_frame = Tkinter.Frame(self.main_window)
        self.bottom_frame = Tkinter.Frame(self.main_window)

        # Create widgets for the top frame
        self.prompt_label = Tkinter.Label(self.top_frame,
                                          text="Enter the number of sides in the shape:")
        self.side_entry = Tkinter.Entry(self.top_frame, width=10)

        # Pack the top frame's widgets
        self.prompt_label.pack(side="left")
        self.side_entry.pack(side="left")

        # Create widgets for the middle frame
        self.descr_label = Tkinter.Label(self.middle_frame, text="Name of shape:")
        self.value = Tkinter.StringVar()
        self.value.set("")
        self.shape_name = Tkinter.Label(self.middle_frame, textvariable=self.value)

        # Pack the middle frame's widgets
        self.descr_label.pack(side="left")
        self.shape_name.pack(side="left")


        # Create widgets for bottom frame
        self.conv_button = Tkinter.Button(self.bottom_frame,
                                          text="Name",
                                          command=self.convert)

        self.quit_button = Tkinter.Button(self.bottom_frame,
                                          text="Quit",
                                          command=self.main_window.destroy)

        # Pack the bottom buttons
        self.conv_button.pack(side="left")
        self.quit_button.pack(side="left")

        # Pack the frames
        self.top_frame.pack()
        self.middle_frame.pack()
        self.bottom_frame.pack()


        # Enter the Tkinter main loop
        Tkinter.mainloop()

    def convert(self):
        # Display and info dialog box
        try:
            self.value.set(name_that_shape(self.side_entry.get()))
        except ValueError:
            self.value.set("Error")
            tkMessageBox.showinfo("Error", "Please input a valid number (3-10)")


# Create an instance of the MainWindow class
ntsg = NameThatShapeGUI()