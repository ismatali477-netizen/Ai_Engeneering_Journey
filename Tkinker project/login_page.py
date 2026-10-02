from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
def login():
    if email_input.get() == "demo@gmail.com" and password_input.get() == "demo@2008":
        messagebox.showinfo("Login Successful")
    else:
        messagebox.showerror("Login Failed")
root=Tk()
root.title("My First GUI")
root.minsize(300,350)
root.maxsize(700,500)
root.geometry("300x350")
root.configure(bg="#0096DC")

logo=Image.open("logo.png")
resized_img=logo.resize((70,70))
logo=ImageTk.PhotoImage(resized_img)

img_label=Label(root,image=logo)
img_label.pack(pady=(10,10))

text_label=Label(root,text="Ismat",fg='white',bg='#0096DC')
text_label.pack()
text_label.config(font=('verdana',20))

email_label=Label(root,text="Enter your email",fg='white',bg='#0096DC')
email_label.pack()
email_label.config(font=('verdana',12))

email_input=Entry(root,width=30)
email_input.pack(ipady=5,pady=(1,15))

password_label=Label(root,text="Enter your password",fg='white',bg='#0096DC')
password_label.pack()
password_label.config(font=('verdana',12))

password_input=Entry(root,width=30)
password_input.pack(ipady=5,pady=(1,15))

login_button=Button(root,text="Login",fg="black",bg="#F8FAFF",command=login)
login_button.pack()

root.mainloop()