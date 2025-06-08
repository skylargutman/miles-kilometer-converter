from tkinter import *

def calc_km():
    km_value_l.config(text= f"{ float(entry.get()) * 1.60934 :.1f}")

window = Tk()
window.config(width=300, height=200, padx=20, pady=20)
window.title("Miles to Kilometers Converter")

#entery field
entry = Entry(width=5)
entry.grid(column=1,row=0)

#miles label
miles_l = Label(text="Miles")
miles_l.grid(column=2,row=0)

#is equal label
is_equal_l = Label(text="is equal to")
is_equal_l.grid(column=0,row=1)

# KM value label
km_value_l = Label(text="0")
km_value_l.grid(column=1, row=1)

#KM label
km_l = Label(text="Km")
km_l.grid(column=2,row=1)

#calculate button
calc_b = Button(text="Calculate", command=calc_km)
calc_b.grid(column=1, row=2)


window.mainloop()