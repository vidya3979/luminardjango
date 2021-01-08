from tkinter import*
root=Tk()
tFrmae=Frame(root)
bFrame=Frame(root)
tFrmae.pack()
bFrame.pack(side=BOTTOM)
btn1=Button(tFrmae,text="first button",fg="green")
btn2=Button(tFrmae,text="secon button",fg="blue")
btn3=Button(tFrmae,text="third button",fg="red")
btn4=Button(bFrame,text="forth button",fg="yellow")

btn1.pack(side=LEFT)
btn2.pack(side=LEFT)
btn3.pack()
btn4.pack()

root.mainloop()
