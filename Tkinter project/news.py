import io
import os
import webbrowser
import requests
from tkinter import *
from urllib.request import urlopen,Request
from PIL import ImageTk,Image
base_dir = os.path.dirname(os.path.abspath(__file__)) 
key_path = os.path.join(base_dir,"secret_api") 
with open(key_path, "r") as file:
    API_KEY = file.read().strip()
class news:
    def __init__(self):
        #fetch data from news api
        self.data=requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={API_KEY}").json()
        self.load_gui()
        self.load_news(0)

    def load_gui(self):
        self.root=Tk()
        self.root.title("News App")
        self.root.geometry("350x600")
        self.root.resizable(0,0)
        self.root.configure(bg="#7ce1f0")


    def clear(self):
        for i in self.root.pack_slaves():
            i.destroy()
    def load_news(self, index):
        self.clear()

        img_url=self.data['articles'][index]['urlToImage']


        if img_url:
            try:
                headers = {'User-Agent': 'Mozilla/5.0'}
                raw_data = requests.get(img_url, headers=headers).content

                im = Image.open(io.BytesIO(raw_data)).resize((350, 250))
                self.photo = ImageTk.PhotoImage(im)  # Save reference on self

                label = Label(self.root, image=self.photo)
                label.pack()
            except Exception as e:
                label = Label(self.root, text="[Image Load Failed]", bg="#7ce1f0", height=10)
                label.pack()
        else:
            label = Label(self.root, text="[No Image Available]", bg="#7ce1f0", height=10)
            label.pack()


        heading=Label(self.root,text=self.data['articles'][index]['title'],bg="#7ce1f0",fg="black",font=("bold",10),wraplength=300,justify="center")
        heading.pack(pady=(10,20))
        heading.config(font=("verdana",10))


        detail=Label(self.root,text=self.data['articles'][index]['description'],bg="#7ce1f0",fg="black",font=("bold",10),wraplength=300,justify="center")
        detail.pack(pady=(2,20))
        detail.config(font=("verdana",10))


        frame=Frame(self.root,bg="#7ce1f0")
        frame.pack(expand=True,fill=BOTH)

        if index!=0:
            prev=Button(frame,text="Prev",width=16,height=3,command=lambda:self.load_news(index-1))
            prev.pack(side=LEFT)

        read=Button(frame,text="Read More",width=16,height=3,command=lambda:self.open_link(self.data['articles'][index]['url']))
        read.pack(side=LEFT)

        if index!=len(self.data['articles'])-1:
            next=Button(frame,text="Next",width=16,height=3,command=lambda:self.load_news(index+1))
            next.pack(side=LEFT)

        self.root.mainloop()
    def open_link(self,url):
        webbrowser.open(url)
object=news()
