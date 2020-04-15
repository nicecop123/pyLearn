from tkinter import *
root = Tk()
topframe=Frame(root)
topframe.pack(side=TOP)
middleframe=Frame(root)
middleframe.pack()
bottomframe=Frame(root)
bottomframe.pack(side=BOTTOM)

button9 = Button(topframe, text="9", fg="orange")
button8 = Button(topframe, text="8", fg="orange")
button7 = Button(topframe, text="7", fg="orange")
button6 = Button(middleframe, text="6", fg="orange")
button5 = Button(middleframe, text="5", fg="orange")
button4 = Button(middleframe, text="4", fg="orange")
button3 = Button(bottomframe, text="3", fg="orange")
button2 = Button(bottomframe, text="2", fg="orange")
button1 = Button(bottomframe, text="1", fg="orange")


button9.pack(side=LEFT)
button8.pack(side=LEFT)
button7.pack(side=LEFT)
button6.pack(side=LEFT)
button5.pack(side=LEFT)
button4.pack(side=LEFT)
button3.pack(side=LEFT)
button2.pack(side=LEFT)
button1.pack(side=LEFT)

root.mainloop()

