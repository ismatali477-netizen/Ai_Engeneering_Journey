from tkinter import *
from PIL import ImageTk, Image
import os
def next_img():
    global counter
    img_label.config(image=img_array[counter%len(img_array)])
    counter += 1
counter=1
root=Tk()
root.title("Wallpaper Viewer")
root.geometry("300x400")
root.configure(bg="#3ccacc")

files= os.listdir("Tkinter project/Wallpapers")
img_array=[]
for file in files:
    img=Image.open(os.path.join("Tkinter project/Wallpapers", file))
    resized_img=img.resize((200, 300))
    img_array.append(ImageTk.PhotoImage(resized_img))
img_label=Label(root,image=img_array[0])
img_label.pack(pady=(10,10))

nxt_btn=Button(root,text="Next",bg="white",fg="#5183b4",command=next_img)
nxt_btn.pack()
root.mainloop()