from tkinter import*
from PIL import Image,ImageTk,ImageDraw
from datetime import*
import time
from math import*

class Clock():
    def __init__(self,parent):
         self.parent=parent
         self.parent.geometry("1350x700+0+0")
         self.parent.config(bg="#021e2f")
         title=Label(self.parent,text="Webcode Analog Clock",font=("times new roman",50,"bold"),bg="#04444a",fg="white")
         title.place(x=0,y=50,relwidth=1)
         self.lbl=Label(self.parent,bg="white")
         self.lbl.place(x=450,y=150,height=400,width=400)
         self.working()
    def clock_image(self,hr,min_,sec_):
         clock=Image.new("RGB",(400,400),(255,255,255))
         draw=ImageDraw.Draw(clock)
         bg=Image.open("images/cl.jpg")
         bg=bg.resize((300,300),Image.Resampling.LANCZOS)
         clock.paste(bg,(50,50))
         origin=200,200
         
         draw.line((origin,200+50*sin(radians(hr)),200-50*cos(radians(hr))),fill="black",width=3)
         draw.line((origin,200+80*sin(radians(min_)),200-80*cos(radians(min_))),fill="blue",width=3)
         draw.line((origin,200+100*sin(radians(sec_)),200-100*cos(radians(sec_))),fill="green",width=3)
         draw.ellipse((195,195,210,210),fill="black")
         clock.save("images/clock_new.png")
    
    def working(self):
         h=datetime.now().time().hour
         m=datetime.now().time().minute
         s=datetime.now().time().second
         hr=(h%12/12)*360 + (m/60)*30
         min_=(m/60)*360 + (s/60)*6
         sec_=(s/60)*360
         self.clock_image(hr,min_,sec_)
         self.img=ImageTk.PhotoImage(Image.open("images/clock_new.png"))
         self.lbl.config(image=self.img)
         self.lbl.after(1000, self.working)
root=Tk()
obj=Clock(root)
root.mainloop()