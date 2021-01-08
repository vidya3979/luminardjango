from tkinter import*

root=Tk()
root.title("Log In Window")

def click_btn():
    print("btn clicked")

ulabel=Label(root,text="username")
plabel=Label(root,text="password")

uentry=Entry(root)
pentry=Entry(root)

btn1=Button(root,text="Log In",command=click_btn,fg="blue")
btn2=Button(root,text="Create New Account",command=click_btn,fg="green")

ulabel.grid(row=0,column=0)
plabel.grid(row=1,column=0)

uentry.grid(row=0,column=1)
pentry.grid(row=1,column=1)

btn1.grid(columnspan=2)
btn2.grid(columnspan=4)

root.mainloop()