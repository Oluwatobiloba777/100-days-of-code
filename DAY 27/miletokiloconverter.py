from tkinter import *


def milesToKm():
    miles = float(milesInput.get())
    km = miles * 1.609
    kilometerResultLabel.config(text=f"{km}")



window = Tk()
window.title("Miles to Kilometer Converter")
window.config(padx=20, pady=20)

milesInput = Entry(width=7)
milesInput.grid(column=1, row=0)

milesLabel = Label(text="Miles")
milesLabel.grid(column=2, row=0)

isEqualLabel = Label(text="is equal to")
isEqualLabel.grid(column=0, row=1)

kilometerLabel = Label(text="Km")
kilometerLabel.grid(column=2, row=1)

kilometerResultLabel = Label(text="0")
kilometerResultLabel.grid(column=1, row=1)

calculateButton = Button(text="Calculate", command=milesToKm)
calculateButton.grid(column=1, row=2)



window.mainloop()