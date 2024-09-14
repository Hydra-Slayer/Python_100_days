from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width = 200, height= 100)
window.config(padx=20, pady=20)



#Entries
entry = Entry(width=30)
#Add some text to begin with
entry.insert(END, string="0")
entry.config(width=10)

def convert():
    distance = entry.get()
    dist_km = float(distance)*1.609
    label_output.config(text=f"{dist_km}")
    
    


entry.grid(row=0,column=1)
#Label
label_miles = Label(text="Miles")
label_miles.grid(row=0, column=2)

label_text = Label(text="is equal to")
label_text.grid(row=1, column=0)

label_output = Label(text="0")
label_output.grid(row=1, column=1)


label_km = Label(text="Km")
label_km.grid(row=1, column=2)

button = Button(text="Calculate", command=convert)
button.grid(row=2, column=1)
window.mainloop()