from tkinter import *
root=Tk()
root.title("Calculator")
root.geometry("300x400")
root.resizable(0,0)
root.configure(bg="#25fb97")

result_label=Label(root,text="0",bg="#25fb97",fg="white")
result_label.grid(row=0,column=0,pady=(40,30))
result_label.config(font=("verdana",30,"bold"))

btn7=Button(root,text="7",width=5,height=2,bg="#2c6971",fg="white")
btn7.grid(row=1,column=0,sticky="nsew")
btn7.config(font=("verdana",15))

btn8=Button(root,text="8",width=5,height=2,bg="#2c6971",fg="white")
btn8.grid(row=1,column=1,sticky="nsew")
btn8.config(font=("verdana",15))

btn9=Button(root,text="9",width=5,height=2,bg="#2c6971",fg="white")
btn9.grid(row=1,column=2,sticky="nsew")
btn9.config(font=("verdana",15))

btn_add=Button(root,text="+",width=5,height=2,bg="#2c6971",fg="white")
btn_add.grid(row=1,column=3,sticky="nsew")
btn_add.config(font=("verdana",15))

btn4=Button(root,text="4",width=5,height=2,bg="#2c6971",fg="white")
btn4.grid(row=2,column=0,sticky="nsew")
btn4.config(font=("verdana",15))

btn5=Button(root,text="5",width=5,height=2,bg="#2c6971",fg="white")
btn5.grid(row=2,column=1,sticky="nsew")
btn5.config(font=("verdana",15))

btn6=Button(root,text="6",width=5,height=2,bg="#2c6971",fg="white")
btn6.grid(row=2,column=2,sticky="nsew")
btn6.config(font=("verdana",15))

btn_subtract=Button(root,text="-",width=5,height=2,bg="#2c6971",fg="white")
btn_subtract.grid(row=2,column=3,sticky="nsew")
btn_subtract.config(font=("verdana",15))

btn1=Button(root,text="1",width=5,height=2,bg="#2c6971",fg="white")
btn1.grid(row=3,column=0,sticky="nsew")
btn1.config(font=("verdana",15))

btn2=Button(root,text="2",width=5,height=2,bg="#2c6971",fg="white")
btn2.grid(row=3,column=1,sticky="nsew")
btn2.config(font=("verdana",15))

btn3=Button(root,text="3",width=5,height=2,bg="#2c6971",fg="white")
btn3.grid(row=3,column=2,sticky="nsew")
btn3.config(font=("verdana",15))

btn_multiply=Button(root,text="*",width=5,height=2,bg="#2c6971",fg="white")
btn_multiply.grid(row=3,column=3,sticky="nsew")
btn_multiply.config(font=("verdana",15))

btn0=Button(root,text="0",width=5,height=2,bg="#2c6971",fg="white")
btn0.grid(row=4,column=0,sticky="nsew")
btn0.config(font=("verdana",15))

btn_clear=Button(root,text="C",width=5,height=2,bg="#2c6971",fg="white")
btn_clear.grid(row=4,column=1,sticky="nsew")
btn_clear.config(font=("verdana",15))

btn_equal=Button(root,text="=",width=5,height=2,bg="#2c6971",fg="white")
btn_equal.grid(row=4,column=2,sticky="nsew")
btn_equal.config(font=("verdana",15))

btn_divide=Button(root,text="/",width=5,height=2,bg="#2c6971",fg="white")
btn_divide.grid(row=4,column=3,sticky="nsew")
btn_divide.config(font=("verdana",15))

root.mainloop()