import tkinter

# button click
def calculate():
    num=int(input.get())
    label3.config(text=int(num*1.609344))

# window
window = tkinter.Tk()
window.title("Mile to Km converter")
window.minsize(width=200, height=100)
window.config(padx=10, pady=10)

# entry
input=tkinter.Entry(width=5)
input.grid(row=0,column=5)

# label

label1=tkinter.Label(text=" Miles")
label1.grid(row=0,column=7)
label2=tkinter.Label(text="is equal to ")
label2.grid(row=2,column=3)
label3=tkinter.Label(text="0")
label3.grid(row=2,column=5)
label4=tkinter.Label(text="km")
label4.grid(row=2,column=7)

#Button

button = tkinter.Button(text="calculate",command=calculate)
button.grid(row=4,column=5)



window.mainloop()
