from tkinter import *
root = Tk()
root.title("Calculator")
toptopframe=Frame(root)
toptopframe.pack(side=TOP)
topframe=Frame(root)
topframe.pack(side=TOP)
middleframe=Frame(root)
middleframe.pack()
morebottom=Frame()
morebottom.pack(side=BOTTOM)
bottomframe=Frame(root)
bottomframe.pack(side=BOTTOM)

numberentry= Entry(toptopframe)

def button_click(number):
    current=numberentry.get()
    numberentry.delete(0,END)
    numberentry.insert(0, str(current) + str(number))

def button_clear():
    numberentry.delete(0,END)

def button_add():
    first_number = numberentry.get()
    global f_num
    global math
    math = "addition"
    f_num=int(first_number)
    numberentry.delete(0,END)

def button_subtract():
    first_number = numberentry.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_number)
    numberentry.delete(0, END)

def button_multiply():
    first_number = numberentry.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)
    numberentry.delete(0, END)

def button_divide():
    first_number = numberentry.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    numberentry.delete(0, END)

def button_equal():
    second_number = numberentry.get()
    numberentry.delete(0,END)
    if math == "addition":
        numberentry.insert(0,f_num+int(second_number))
    if math == "subtraction":
        numberentry.insert(0,f_num-int(second_number))
    if math == "multiplication":
        numberentry.insert(0,f_num*int(second_number))
    if math == "division":
        numberentry.insert(0,f_num/int(second_number))

button9 = Button(topframe, text="9", fg="orange",command=lambda: button_click(9))
button8 = Button(topframe, text="8", fg="orange",command=lambda: button_click(8))
button7 = Button(topframe, text="7", fg="orange",command=lambda: button_click(7))
button6 = Button(middleframe, text="6", fg="orange",command=lambda: button_click(6))
button5 = Button(middleframe, text="5", fg="orange",command=lambda: button_click(5))
button4 = Button(middleframe, text="4", fg="orange",command=lambda: button_click(4))
button3 = Button(bottomframe, text="3", fg="orange",command=lambda: button_click(3))
button2 = Button(bottomframe, text="2", fg="orange",command=lambda: button_click(2))
button1 = Button(bottomframe, text="1", fg="orange",command=lambda: button_click(1))
button0 = Button(morebottom, text="0", fg="orange",command=lambda: button_click(0))
buttonadd =Button(topframe, text="+", fg="orange", command=button_add)
buttonminus = Button(middleframe, text="-", fg="orange", command=button_subtract)
buttonmultiply =Button(bottomframe, text="x", fg="orange",command=button_multiply)
buttondivide = Button(morebottom, text="/", fg="orange",command=button_divide)
buttonclear = Button(morebottom, text="Clear", fg="orange",command=button_clear)
buttonequal = Button(morebottom, text="=", fg="orange",command=button_equal)

numberentry.pack()

button9.pack(side=LEFT)
button8.pack(side=LEFT)
button7.pack(side=LEFT)
buttonadd.pack(side=LEFT)
button6.pack(side=LEFT)
button5.pack(side=LEFT)
button4.pack(side=LEFT)
buttonminus.pack(side=LEFT)
button3.pack(side=LEFT)
button2.pack(side=LEFT)
button1.pack(side=LEFT)
buttonmultiply.pack(side=LEFT)
buttonclear.pack(side=LEFT)
button0.pack(side=LEFT)
buttonequal.pack(side=LEFT)
buttondivide.pack(side=LEFT)

root.mainloop()