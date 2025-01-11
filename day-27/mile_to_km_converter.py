
from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20,pady=20)



my_label = Label(text="is equal to",font="Arial")
my_label.grid(column=0,row=1)

mile_label = Label(text="Miles",font="Arial")
mile_label.grid(column=2,row=0)

km_label = Label(text="Km",font="Arial")
km_label.grid(column=2,row=1)

result_label = Label(text="0",font="Arial")
result_label.grid(column=1,row=1)



def button_clicked():
    label_text = float(input.get())
    calculated_km = round(label_text * 1.609)
    result_label.config(text=f"{calculated_km}")


button = Button(text="Calculate",command=button_clicked)
button.grid(column=1,row=2)


input = Entry(width=7)
input.grid(column=1,row=0)




window.mainloop()


