from tkinter import*
from tkinter import ttk
import tkinter
from PIL import Image,ImageTk
from avatar_generator import AvatarGenerator
import os
from time import strftime
from datetime import datetime
from tkinter import messagebox

class nft_generator:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1580x790+0+0")
        self.root.title("NFT Generator")

        #Background image
        img2 = Image.open(r"resource\bg1.jpg")
        img2 = img2.resize((1580,900) , Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        bg_img = Label(self.root,image =self.photoimg2)
        bg_img.place(x = 0,y = 0,width=1536,height=900)


        #clock
        def time():
            string=strftime("%H:%M:%S %p")
            lbl.config(text=string)
            lbl.after(1000, time)


        lbl= Label(self.root,font=("Comic Sans MS",15,"bold"),background="crimson",foreground="white")
        lbl.place(x=0,y=2,width=200,height=50)
        time()

        #geneate nft button button
        img3 = Image.open(r"resource\generate_avatar_btn.jpg")
        img3 = img3.resize((220,220) , Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        b1 = Button(bg_img,image = self.photoimg3,command=self.generate_avatar,cursor="hand2")
        b1.place(x=200,y=300,width=220,height=220)
        
        b1_1 = Button(bg_img,text="Generate NFT",command=self.generate_avatar,cursor="hand2",font=("Comic Sans MS",15,"bold"),bg="white",fg="darkblue")
        b1_1.place(x=200,y=510,width=220,height=30)


        #photos button
        img8 = Image.open(r"resource\show_nft_btn.jpg")
        img8 = img8.resize((220,220) , Image.ANTIALIAS)
        self.photoimg8 = ImageTk.PhotoImage(img8)
        b1 = Button(bg_img,image = self.photoimg8,command=self.open_image,cursor="hand2")
        b1.place(x=700,y=300,width=220,height=220)
        b1_1 = Button(bg_img,text="NFT",cursor="hand2",command=self.open_image,font=("Comic Sans MS",15,"bold"),bg="white",fg="green")
        b1_1.place(x=700,y=510,width=220,height=30)



        #Exit button
        img10 = Image.open(r"resource\Exit_image.jpg")
        img10 = img10.resize((220,220) , Image.ANTIALIAS)
        self.photoimg10 = ImageTk.PhotoImage(img10)
        b1 = Button(bg_img,image = self.photoimg10,cursor="hand2",command=self.exit)
        b1.place(x=1200,y=300,width=220,height=220)
        b1_1 = Button(bg_img,text="Exit",cursor="hand2",command=self.exit,font=("Comic Sans MS",15,"bold"),bg="white",fg="red")
        b1_1.place(x=1200,y=510,width=220,height=30)


    def generate_avatar(self):
        generator = AvatarGenerator("./images")
        generator.generate_avatar(100)
        messagebox.showinfo("Output","NFT Generated!!!")


        #image directory
    def open_image(self):
        os.startfile("output")


         #Exit
    def exit(self):
        self.exit=tkinter.messagebox.askyesno("NFT Generator","Exit this project??",parent=self.root)
        if self.exit>0:
            self.root.destroy()
        else:
            return


if __name__=='__main__':
    root = Tk()
    obj = nft_generator(root)
    root.mainloop()
