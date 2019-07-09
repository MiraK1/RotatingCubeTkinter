from tkinter import *
import time
import math

class coords():
    def __init__(self, x,y,z):
        self.x = x
        self.y = y
        self.z = z

        self.rxy = (self.x**2+self.y**2)**(1/2)
        self.rxz = (self.x**2+self.z**2)**(1/2)
        self.ryz = (self.y**2+self.z**2)**(1/2)
        self.arg()

    def arg(self):
        if self.x > 0 and self.y > 0 :
            self.txy = math.atan(self.y/self.x)
        elif self.x > 0 and self.y < 0 :
            self.txy = 2*math.pi + math.atan(self.y/self.x)
        elif self.x < 0 and self.y > 0 :
            self.txy = math.pi + math.atan(self.y/self.x)
        elif self.x < 0 and self.y < 0 :
            self.txy = math.pi + math.atan(self.y/self.x)

        if self.z > 0 and self.x > 0 :
            self.txz = math.atan(self.x/self.z )
        elif self.z > 0 and self.x < 0 :
            self.txz = 2*math.pi + math.atan(self.x/self.z )
        elif self.z < 0 and self.x > 0 :
            self.txz = math.pi + math.atan(self.x/self.z )
        elif self.z < 0 and self.x < 0 :
            self.txz = math.pi + math.atan(self.x/self.z )

        if self.y > 0 and self.z > 0 :
            self.tyz = math.atan(self.z/self.y)
        elif self.y > 0 and self.z < 0 :
            self.tyz = 2*math.pi + math.atan(self.z/self.y)
        elif self.y < 0 and self.z > 0 :
            self.tyz = math.pi + math.atan(self.z/self.y)
        elif self.y < 0 and self.z < 0 :
            self.tyz = math.pi + math.atan(self.z/self.y)


    def rotZ(self,t):
        self.txy = self.txy + t if self.txy + t >= 0 else self.txy + t  + 2*math.pi

        self.x = math.cos(self.txy)*self.rxy
        self.y = math.sin(self.txy)*self.rxy

        self.rxz = (self.x**2+self.z**2)**(1/2)
        self.ryz = (self.y**2+self.z**2)**(1/2)
        self.arg()

    def rotY(self,t):
        self.txz = self.txz + t if self.txz + t >= 0 else self.txz + t  + 2*math.pi
        self.z = math.cos(self.txz)*self.rxz
        self.x = math.sin(self.txz)*self.rxz
        self.rxy = (self.x**2+self.y**2)**(1/2)
        self.ryz = (self.y**2+self.z**2)**(1/2)
        self.arg()
    def rotX(self,t):
        self.tyz = self.tyz + t if self.tyz + t >= 0 else self.tyz + t  + 2*math.pi

        self.y = math.cos(self.tyz)*self.ryz
        self.z = math.sin(self.tyz)*self.ryz

        self.rxy = (self.x**2+self.y**2)**(1/2)
        self.rxz = (self.x**2+self.z**2)**(1/2)
        self.arg()
class Win():
    def __init__(self,master):
        self.master = master
        self.master.geometry("1200x600+{}+{}".format(int((WIDTH-1200)/2),int((HEIGHT-600)/2)))
        self.C = Canvas(self.master,width = 1200,height = 600)

        self.M1 = self.C.create_oval(M[0].x+600,M[0].z+300,M[0].x+600+1,M[0].z+300+1)
        self.M2 = self.C.create_oval(M[1].x+600,M[1].z+300,M[1].x+600+1,M[1].z+300+1)
        self.M3 = self.C.create_oval(M[2].x+600,M[2].z+300,M[2].x+600+1,M[2].z+300+1)
        self.M4 = self.C.create_oval(M[3].x+600,M[3].z+300,M[3].x+600+1,M[3].z+300+1)
        self.M5 = self.C.create_oval(M[4].x+600,M[4].z+300,M[4].x+600+1,M[4].z+300+1)
        self.M6 = self.C.create_oval(M[5].x+600,M[5].z+300,M[5].x+600+1,M[5].z+300+1)
        self.M7 = self.C.create_oval(M[6].x+600,M[6].z+300,M[6].x+600+1,M[6].z+300+1)
        self.M8 = self.C.create_oval(M[7].x+600,M[7].z+300,M[7].x+600+1,M[7].z+300+1)

        self.L1 = self.C.create_line(M[0].x+600,M[0].z+300,M[1].x+600,M[1].z+300)
        self.L2 = self.C.create_line(M[1].x+600,M[1].z+300,M[2].x+600,M[2].z+300)
        self.L3 = self.C.create_line(M[2].x+600,M[2].z+300,M[3].x+600,M[3].z+300)
        self.L4 = self.C.create_line(M[3].x+600,M[3].z+300,M[0].x+600,M[0].z+300)

        self.L5 = self.C.create_line(M[4].x+600,M[4].z+300,M[5].x+600,M[5].z+300)
        self.L6 = self.C.create_line(M[5].x+600,M[5].z+300,M[6].x+600,M[6].z+300)
        self.L7 = self.C.create_line(M[6].x+600,M[6].z+300,M[7].x+600,M[7].z+300)
        self.L8 = self.C.create_line(M[7].x+600,M[7].z+300,M[4].x+600,M[4].z+300)

        self.L9 = self.C.create_line(M[4].x+600,M[4].z+300,M[0].x+600,M[0].z+300)
        self.L10 = self.C.create_line(M[5].x+600,M[5].z+300,M[1].x+600,M[1].z+300)
        self.L11 = self.C.create_line(M[6].x+600,M[6].z+300,M[2].x+600,M[2].z+300)
        self.L12 = self.C.create_line(M[7].x+600,M[7].z+300,M[3].x+600,M[3].z+300)



        self.master.bind("<Key-a>", lambda event: self.Rot(event,"Zp"))
        self.master.bind("<Key-z>", lambda event: self.Rot(event,"Zm"))
        self.master.bind("<Key-q>", lambda event: self.Rot(event,"Xp"))
        self.master.bind("<Key-s>", lambda event: self.Rot(event,"Xm"))
        self.master.bind("<Key-w>", lambda event: self.Rot(event,"Yp"))
        self.master.bind("<Key-x>", lambda event: self.Rot(event,"Ym"))

        self.C.pack()
    def Rot(self,event,axe) :
        if axe =="Zp":
            for i in range(8):
                M[i].rotZ(0.03)
        elif axe =="Zm":
            for i in range(8):
                M[i].rotZ(-0.03)
        elif axe =="Xp":
            for i in range(8):
                M[i].rotX(0.03)
        elif axe =="Xm":
            for i in range(8):
                M[i].rotX(-0.03)
        elif axe =="Yp":
            for i in range(8):
                M[i].rotY(0.03)
        elif axe =="Ym":
            for i in range(8):
                M[i].rotY(-0.03)

        self.C.coords(self.M1,M[0].x+600,M[0].z+300,M[0].x+600+1,M[0].z+300+1)
        self.C.coords(self.M2,M[1].x+600,M[1].z+300,M[1].x+600+1,M[1].z+300+1)
        self.C.coords(self.M3,M[2].x+600,M[2].z+300,M[2].x+600+1,M[2].z+300+1)
        self.C.coords(self.M4,M[3].x+600,M[3].z+300,M[3].x+600+1,M[3].z+300+1)
        self.C.coords(self.M5,M[4].x+600,M[4].z+300,M[4].x+600+1,M[4].z+300+1)
        self.C.coords(self.M6,M[5].x+600,M[5].z+300,M[5].x+600+1,M[5].z+300+1)
        self.C.coords(self.M7,M[6].x+600,M[6].z+300,M[6].x+600+1,M[6].z+300+1)
        self.C.coords(self.M8,M[7].x+600,M[7].z+300,M[7].x+600+1,M[7].z+300+1)

        self.C.coords(self.L1,M[0].x+600,M[0].z+300,M[1].x+600,M[1].z+300)
        self.C.coords(self.L2,M[1].x+600,M[1].z+300,M[2].x+600,M[2].z+300)
        self.C.coords(self.L3,M[2].x+600,M[2].z+300,M[3].x+600,M[3].z+300)
        self.C.coords(self.L4,M[3].x+600,M[3].z+300,M[0].x+600,M[0].z+300)

        self.C.coords(self.L5,M[4].x+600,M[4].z+300,M[5].x+600,M[5].z+300)
        self.C.coords(self.L6,M[5].x+600,M[5].z+300,M[6].x+600,M[6].z+300)
        self.C.coords(self.L7,M[6].x+600,M[6].z+300,M[7].x+600,M[7].z+300)
        self.C.coords(self.L8,M[7].x+600,M[7].z+300,M[4].x+600,M[4].z+300)

        self.C.coords(self.L9,M[4].x+600,M[4].z+300,M[0].x+600,M[0].z+300)
        self.C.coords(self.L10,M[5].x+600,M[5].z+300,M[1].x+600,M[1].z+300)
        self.C.coords(self.L11,M[6].x+600,M[6].z+300,M[2].x+600,M[2].z+300)
        self.C.coords(self.L12,M[7].x+600,M[7].z+300,M[3].x+600,M[3].z+300)



M = [coords(50,50,-50), coords(-50,50,-50), coords(-50,50,50), coords(50,50,50), coords(50,-50,-50), coords(-50,-50,-50), coords(-50,-50,50), coords(50,-50,50)]


win = Tk()
win.title("3D cube   -   MiraK")
WIDTH = win.winfo_screenwidth()
HEIGHT = win.winfo_screenheight()
app = Win(win)


win.mainloop()
