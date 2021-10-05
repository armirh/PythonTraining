# radio button = similar to checkbox, but can select only one from a group
from tkinter import *

food = ["pizza", "hamburger", "hot-dog"]

window = Tk()

x = IntVar()

for index in range(len(food)):
    radiobutton = Radiobutton(window,
                              text=food[index],  # add text to radio buttons
                              variable=x,  # groups radiobuttons together
                              value=index,  # assigns each radiobutton a diff value
                              padx=25,
                              font=("Cosmic Sans", 35))
    radiobutton.pack(anchor=W)

window.mainloop()

