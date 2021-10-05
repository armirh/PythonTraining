# Label = an area widget that holds text and/or an image within a window

from tkinter import *

window = Tk()

photo = PhotoImage(file="download.png")

label = Label(window,
              text="Formula 1 season 2021",
              font=("Arial", 40, "bold"),
              fg="#00FF00",
              bg="black",
              relief=RAISED,
              bd=10,
              padx=20,
              pady=20,
              image=photo,
              compound='bottom')  # instantiate the label (container)
label.pack()  # this way places the label in the middle of the window
# label.place(x=110, y=50)  # this way we can give coordinates where to place the label


window.mainloop()
