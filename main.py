
from tkinter import *
import img
import clip
import cv2
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
from tkinter.ttk import *
import tkinter.ttk as ttk
from tkinter import messagebox


class mywindow:

    def __init__(self,win):
        self.mycv = ""
        win.title("Photo Designer ")
        win.geometry("550x500+400+40")
        self.win=win
        self.st = Style()
        self.st.configure('W.TButton', background='black', foreground='black', font=('Segoe Print', 16))
        self.bv=Button(win,text="Presentation 🎬",command=self.clipp,style='W.TButton')
        self.b=Button(win,text="Take a picture📸",command=self.picture,style='W.TButton')
        self.b1=Button(win,text="Choose image📂",style='W.TButton')
        self.b2=Button(win,text="Filters🛠",style='W.TButton')
        self.b3=Button(win,text= "Cut ✂",style='W.TButton',command=self.cut)
        self.b4=Button(win,text="Add text 🖊",style='W.TButton')
        self.b5=Button(win,text="Draw shape ◻0l",style='W.TButton',command=self.listShapes)
        self.b6=Button(win,text="Save as📥",style='W.TButton',command=self.save)
        self.b7=Button(win,text= "Exit❌",command=self.closeWin)
        self.lbl1=Label(win,text=" © All rights reserved to Efrat Indig and Shira Vinograd",foreground='orange',font=('Arial',12))
        self.h1=Label(win,text='Photo Designer ~',foreground='orange',font=('Forte', 32))
        self.flagButton=False
        self.position()
        self.events()

#------מיקומים-----
    def position(self):
        self.bv.place(x=500, y=100)
        self.h1.place(x=50,y=50)
        self.bv.place(x=50, y=130)
        self.b.place(x=300,y=130)
        self.b1.place(x=50,y=200)
        self.b2.place(x=50,y=280)
        self.b3.place(x=50,y=360)
        self.b4.place(x=300,y=200)
        self.b5.place(x=300,y=280)
        self.b6.place(x=300,y=360)
        self.b7.place(x=470,y=7)
        self.lbl1.place(x=85,y=450)
#------אירועים------
    def events(self):
        self.b1.bind('<Button-1>', self.addImg)
        self.b2.bind('<Button-1>', self.filters)
        self.b4.bind('<Button-1>', self.addtext)
#---הצגת וידיאו----
    def clipp(self):
        movie = clip.Movie_MP4("הסרט שלי.mp4")
        movie.play()
#----צילום תמונה----
    def picture(self):
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            raise IOError("Cannot open webcam")
        for i in range(1):
            ret, frame = cap.read()
            frame = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
            return_value, image = cap.read()
            cv2.imwrite('opencv.jpg', image)
        cap.release()
        cv2.destroyAllWindows()
        newImg=img.image("opencv.jpg", "Photo Designer")
        self.mycv=newImg
        self.flagButton=True

#-----הוספת תמונה---
    def addImg(self, event):
        self.flagButton=True
        file_name = askopenfilename()
        newImg=img.image(file_name, "Photo Designer")
        self.mycv=newImg

#---חלונית פילטרים---
    def filters(self,event):
        if self.flagButton == False:
            messagebox.showwarning("Photo Designer", "Image selection required!")
        else:
            top=Tk()
            top.title("Filters")
            top.geometry("580x200+200+300")
            style = ttk.Style(top)
            style.configure("TButton", font=('Segoe Print', 16))
            lbl=Label(top,text='Choose what you love and love what you choose (;',font=("Forte",19),foreground='orange').place(x=10,y=10)
            ttk.Button(top, text='frames', command=self.getFrame).place(x=10,y=50)
            ttk.Button(top,text='black&white',command=self.black,style="TButton").place(x=10,y=100)
            ttk.Button(top,text='sharp',command=self.sharp,style="TButton").place(x=10,y=150)
            ttk.Button(top,text='invert',command=self.invert,style="TButton").place(x=200,y=50)
            ttk.Button(top,text='original',command=self.original,style="TButton").place(x=200,y=100)
            ttk.Button(top, text='sepia', command=self.sepia, style="TButton").place(x=200, y=150)
            ttk.Button(top,text='blur'  ,command=self.blur).place(x=390, y=50)
            ttk.Button(top,text='emboss', command=self.emboss).place(x=390, y=100)
            ttk.Button(top,text='rotate', command=self.rotate).place(x=390, y=150)

#-----הוספת טקסט לתמונה---
    def addtext(self,event):
        if self.flagButton==False:
            messagebox.showwarning("Photo Designer","Image selection required!")
        else:
            top=Tk()
            top.title("Photo Designer")
            top.geometry("250x200+200+300")
            lbl1 = Label(top, text="Enter text " ,font=("Forte",19),foreground='orange')
            global entry1
            entry1=Entry(top)
            lbl1.pack()
            entry1.place(x=50,y=60)
            entry1.pack()
            style = ttk.Style(top)
            style.configure("TButton", font=('Segoe Print', 8))
            b = Button(top, text="ok",command=self.addText,style='TButton').place(x=75,y=60)
            lbl2 = Label(top, text="* Click on the image to place the text").place(x=30,y=150)
        #הכפתור OK שולח לפונקציה זו
        #הפונקציה הזאת מעבירה את הטקסט לתמונה
    def addText(self):
        cv2.setMouseCallback(self.mycv.nameWindow, self.mycv.putText,entry1.get())

# -------חיתוך-------
    def cut(self):
        if self.flagButton==False:
            messagebox.showwarning("Photo Designer","Image selection required!")
        else:
            self.mycv.getType('cut')

#-----רשימת צורות----
    def listShapes(self):
        if self.flagButton==False:
            messagebox.showwarning("Photo Designer","Image selection required!")
        else:
            top = Tk()
            top.title("Shapes list")
            listbox = Listbox(top, height=10,
                      width=10,
                      bg='light grey',
                      activestyle='dotbox',
                      font=("Segoe Print",14),
                      fg="black")
            top.geometry("200x200")
            label = Label(top, text=" SHAPES ITEMS",font=("Forte",19),foreground='orange')
            listbox.insert(1, "rectangle")
            listbox.insert(2, "circle")
            listbox.insert(3, "line")
            listbox.insert(4, "triangular")
            label.pack()
            listbox.pack()
            def getList(event):
                index = listbox.curselection()[0]
                seltext = listbox.get(index)
                if seltext == 'rectangle':
                    self.drawR()
                elif seltext == 'circle':
                    self.drawC()
                elif seltext == 'line':
                    self.drawl()
                elif seltext == 'triangular':
                    self.drawT()

        listbox.bind('<ButtonRelease-1>',getList)
        #top.mainloop()

#-----------ציור צורות---------
    #ציור רבוע
    def drawR(self):
        self.mycv.getType('rectangle')
    #ציור עיגול
    def drawC(self):
        self.mycv.getType('circle')
    #ציור קו
    def drawl(self):
        self.mycv.getType('line')
    #ציור משולש
    def drawT(self):
        self.mycv.getType('triangular')

#---------------פילטרים----------
    #פילטר שחור לבן
    def black(self):
        self.mycv.filterBlack()
    #פילטר שארפ
    def sharp(self):
       self.mycv.filterSharpen()
    #פילטר אינברט
    def invert(self):
        self.mycv.filterInvert()
    #רקע מעושן
    def sepia(self):
        self.mycv.filterSepia()
    #מטושטש
    def blur(self):
        self.mycv.filterBlur()
    #בהיר
    def emboss(self):
        self.mycv.filterEmboss()
    #סיבוב עדין לצד ימין
    def rotate(self):
        self.mycv.filterRotate()
    #מקור
    def original(self):
        self.mycv.noneFilter()
    #מסגרות
    def getFrame(self):
        self.mycv.frame()
#------------------------------------

#--------שמירה------
    def save(self):
        path=asksaveasfilename(defaultextension='.json',filetypes=[("json files",'*.json'),("jpg files",'*.jpg'),("PNG files",'*.png')],
                title="Choose fileName")
        cv2.imwrite(path,self.mycv.img)

#--------יציאה------
    def closeWin(self):
        ans=messagebox.askokcancel("Photo Designer", "Are you sure you want to exit?")
        if ans:
            window.quit()


#מופע מסוג המחלקה
window=Tk()
p1 = PhotoImage(file='icon.PNG')
window.iconphoto(False, p1)
mywin=mywindow(window)
window.mainloop()









