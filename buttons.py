import random
from tkinter import *
import json



class Buttons:
    def __init__(self, master):
        self.master = master
        self.cross_image = PhotoImage(file="images/wrong.png")
        self.tick_image = PhotoImage(file="images/right.png")





    def wrong_button(self, command):
        unknown_button = Button(image=self.cross_image, command=command)
        unknown_button.grid(row=3, column=1)
        unknown_button.config(highlightthickness=0)
        return unknown_button


    def right_button(self, command):
        unknown_button = Button(image=self.tick_image, command=command)
        unknown_button.grid(row=3, column=2)
        unknown_button.config(highlightthickness=0)


