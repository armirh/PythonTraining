# checkboxes
from tkinter import *

def display():
    if(x.get()):
        print("Agree!")
    else:
        print("Disagree")


window = Tk()

x = BooleanVar()

photo = PhotoImage(file="download.png")

check_button = Checkbutton(window,
                           text="F1 is exciting to watch",
                           variable=x,
                           onvalue=True,
                           offvalue=False,
                           command=display,
                           font=("Cosmic Sans", 25),
                           fg="green",
                           bg="black",
                           activeforeground="green",
                           activebackground="black",
                           padx=25,
                           pady=15,
                           image=photo,
                           compound="right")
check_button.pack()

window.mainloop()

