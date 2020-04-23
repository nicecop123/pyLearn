from tkinter import *
root=Tk()
root.geometry("675x750+0+0")
root.title("Tic tac toe")
root.configure(background="Cadet Blue")

top=Frame(root, bg="Cadet Blue", pady=2, width=675,height=50,relief=RIDGE)
top.grid(row=0,column=0)

lblTitle=Label(top,font=('arial',50,'bold'), text="Tic Tac Toe Game",bd=21,bg='Cadet Blue',fg='Cornsilk',justify=CENTER)
lblTitle.grid(row=0,column=0)

main=Frame(root, bg="Powder Blue", pady=2, width=675,height=300,relief=RIDGE,bd=10)
main.grid(row=1,column=0)

left=Frame(main, bg="Cadet Blue", pady=2, width=375,height=250,padx=10,relief=RIDGE,bd=10)
left.pack(side=LEFT)

right=Frame(main, bg="Cadet Blue", pady=2, width=280,height=250,padx=10,relief=RIDGE,bd=10)
right.pack(side=RIGHT)

right1=Frame(right, bg="Cadet Blue", pady=2, width=280,height=250,padx=10,relief=RIDGE,bd=10)
right1.grid(row=0,column=0)

right2=Frame(right, bg="Cadet Blue", pady=2, width=280,height=250,padx=10,relief= RIDGE,bd=10)
right2.grid(row=1,column=0)

playerX=IntVar()
playerO=IntVar()
playerX.set(0)
playerO.set(0)

button1=Button(left,text='',font='Times 26 bold',height=1.5,width=4,bg='gainboro')
button1.grid(row=1,column=0,sticky=S+N+E+W)

root.mainloop()