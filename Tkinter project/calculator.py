from tkinter import *
first_num=second_num=operator=None
def digit(num):
    current=result_label["text"]
    result_label.config(text=current+str(num))
def clear():
    result_label.config(text="")
    input_label.config(text="")
def current_operator(op):
    global first_num, operator
    first_num=int(result_label["text"])
    operator=op
    result_label.config(text=result_label["text"]+op)
def result():
    global first_num, second_num, operator
    if operator is not None:
        full_text = result_label["text"]
        second_num_str = full_text.split(operator)[-1]
        if second_num_str != "":
            second_num = int(second_num_str)
            input_label.config(text=full_text)
            if operator == "+":
                result_label.config(text=str(first_num + second_num))
            elif operator == "-":
                result_label.config(text=str(first_num - second_num))
            elif operator == "*":
                result_label.config(text=str(first_num * second_num))
            elif operator == "/":
                if second_num == 0:
                    result_label.config(text="Error")
                else:
                    result_label.config(text=str(round(first_num / second_num, 2)))
root=Tk()
root.title("Calculator")
root.geometry("300x442")
root.resizable(0,0)
root.configure(bg="#ffffff")

input_label=Label(root,text="",bg="#ffffff",fg="black")
input_label.grid(row=0,column=0,columnspan=4,pady=(10,0),sticky="w")
input_label.config(font=("verdana",15))

result_label=Label(root,text="",bg="#ffffff",fg="black")
result_label.grid(row=1,column=0,columnspan=4,pady=(40,51),sticky="w")
result_label.config(font=("verdana",20,"bold"))

btn7=Button(root,text="7",width=5,height=2,bg="#2c6971",fg="white",command=lambda: digit(7))
btn7.grid(row=2,column=0,sticky="nsew")
btn7.config(font=("verdana",15))

btn8=Button(root,text="8",width=5,height=2,bg="#2c6971",fg="white",command=lambda: digit(8))
btn8.grid(row=2,column=1,sticky="nsew")
btn8.config(font=("verdana",15))

btn9=Button(root,text="9",width=5,height=2,bg="#2c6971",fg="white",command=lambda: digit(9))
btn9.grid(row=2,column=2,sticky="nsew")
btn9.config(font=("verdana",15))

btn_clear=Button(root,text="C",width=5,height=2,bg="#f6671a",fg="white",command=clear)
btn_clear.grid(row=2,column=3,sticky="nsew")
btn_clear.config(font=("verdana",15))

btn4=Button(root,text="4",width=5,height=2,bg="#2c6971",fg="white",command=lambda: digit(4))
btn4.grid(row=3,column=0,sticky="nsew")
btn4.config(font=("verdana",15))

btn5=Button(root,text="5",width=5,height=2,bg="#2c6971",fg="white",command=lambda: digit(5))
btn5.grid(row=3,column=1,sticky="nsew")
btn5.config(font=("verdana",15))

btn6=Button(root,text="6",width=5,height=2,bg="#2c6971",fg="white",command=lambda: digit(6))
btn6.grid(row=3,column=2,sticky="nsew")
btn6.config(font=("verdana",15))

btn_subtract=Button(root,text="-",width=5,height=2,bg="#f6671a",fg="white",command=lambda: current_operator("-"))
btn_subtract.grid(row=3,column=3,sticky="nsew")
btn_subtract.config(font=("verdana",15))

btn1=Button(root,text="1",width=5,height=2,bg="#2c6971",fg="white",command=lambda: digit(1))
btn1.grid(row=4,column=0,sticky="nsew")
btn1.config(font=("verdana",15))

btn2=Button(root,text="2",width=5,height=2,bg="#2c6971",fg="white",command=lambda: digit(2))
btn2.grid(row=4,column=1,sticky="nsew")
btn2.config(font=("verdana",15))

btn3=Button(root,text="3",width=5,height=2,bg="#2c6971",fg="white",command=lambda: digit(3))
btn3.grid(row=4,column=2,sticky="nsew")
btn3.config(font=("verdana",15))

btn_multiply=Button(root,text="*",width=5,height=2,bg="#f6671a",fg="white",command=lambda: current_operator("*"))
btn_multiply.grid(row=4,column=3,sticky="nsew")
btn_multiply.config(font=("verdana",15))

btn0=Button(root,text="0",width=5,height=2,bg="#2c6971",fg="white",command=lambda: digit(0))
btn0.grid(row=5,column=0,sticky="nsew")
btn0.config(font=("verdana",15))

btn_add=Button(root,text="+",width=5,height=2,bg="#f6671a",fg="white",command=lambda: current_operator("+"))
btn_add.grid(row=5,column=1,sticky="nsew")
btn_add.config(font=("verdana",15))

btn_equal=Button(root,text="=",width=5,height=2,bg="#f6671a",fg="white",command=result)
btn_equal.grid(row=5,column=2,sticky="nsew")
btn_equal.config(font=("verdana",15))

btn_divide=Button(root,text="/",width=5,height=2,bg="#f6671a",fg="white",command=lambda: current_operator("/"))
btn_divide.grid(row=5,column=3,sticky="nsew")
btn_divide.config(font=("verdana",15))

root.mainloop()