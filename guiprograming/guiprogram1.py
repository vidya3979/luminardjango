from tkinter import *

root=Tk()
root.title("Main window")
label1=Label(root,text="username")
label2=Label(root,text="password")
label3=Label(root,text="email_id")
entry1=Entry(root)

entry1.pack()
label1.pack()
label2.pack()
label3.pack()

root.mainloop()