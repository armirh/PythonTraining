from tkinter import *

window = Tk()

count = 0
def click():
    global count
    count += 1
    print(count)

photo = PhotoImage(file="901809-200.png")

button = Button(window,
                text="Click on the button!",
                command=click,
                font=("Comic Sans", 30),
                fg="green",
                bg="black",
                activeforeground="green",
                activebackground="black",
                image=photo,
                compound="bottom",
                state=ACTIVE)
button.pack()

window.mainloop()
