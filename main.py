from tkinter import *

def button_clicked():
    # my_label["text"] = "Button got clicked"
    my_label["text"] = my_entry.get()

window = Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=300)

#label
my_label = Label(text="I am a label", font=('arial', 24, 'bold'))
my_label["text"] = "new text"
my_label.config(text="text")
my_label.grid(column=0,row=0)

#button
button = Button(text="Click Me", command=button_clicked)
button.grid(column=1,row=1)
button2 = Button(text="New Button")
button2.grid(column=2, row=0)

#entry
my_entry = Entry(width=10)
my_entry.grid(column=3,row=3)







window.mainloop()