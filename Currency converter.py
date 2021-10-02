from tkinter import *

root = Tk()
root.geometry("400x400+250+250")
root.title("Currency Converter")

heading = Label(root, text="WELCOME TO CURRENCY CONVERTER", font=('arial 13 bold'), fg="blue").pack()

entr_amt = Label(root, text="Enter Amount In Dollar", font=('arial 20 bold')).place(x=10, y=50)

my_num = IntVar()
ent_box = Entry(root, width=58, textvariable=my_num).place(x=10, y=90)

def converter():
	here = my_num.get()
	final = here * 74.15
	lab = Label(root, text=("Rs. "+ str(final)), font=('arial, 25 bold'), fg="red").place(x=10, y=200)

def reverse():
	here = my_num.get() 
	final = here / 74.15
	lab = Label(root, text=("$"+ str(final)), font=('arial, 25 bold'), fg="green").place(x=10, y=240) 

btn1 = Button(root, text="Convert", width=12, height=2, bg="lightgreen", command=converter).place(x=10, y=130) 

btn2 = Button(root, text="Reverse", width=12, height=2, bg="lightgreen", command=reverse).place (x=180, y=130)

root.mainloop()