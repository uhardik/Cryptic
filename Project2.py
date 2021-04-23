from tkinter import *
from tkinter import messagebox
import pygame


pygame.init()
root=Tk()
root.title("CRYPTIC CURRENCY")
root.geometry('1352x652+0+0')
root.configure(background='black')
ABC=Frame(root,bg='black')
ABC.grid()
ABC1=Frame(root,bg='black',bd=20,width=900,height=600)
ABC1.grid(row=0,column=0)
ABC2=Frame(root,bg='black',bd=20,width=452,height=600)
ABC2.grid(row=0,column=1)

ABC1a=Frame(ABC1,bg='green',bd=20,padx=110,width=900,height=200)
ABC1a.grid(row=0,column=0)
T=Label(ABC1a,text="CRYPTIC CURRENCY",font=('arial',20,'bold'),bg='black',fg='white',bd=5,justify=CENTER)
T.grid(row=0,column=0)

ABC1b=Frame(ABC1,bg='light blue',bd=20,width=900,height=200)
ABC1b.grid(row=1,column=0)

ABC1c=Frame(ABC1,bg='gray',bd=20,width=10000,height=200)
ABC1c.grid(row=2,column=0)
def MillionPicture1():
    canvas=Canvas(ABC2,bg='black',width=670,height=270)
    canvas.grid(row=0,column=0)
    canvas.delete("all")
    image1=PhotoImage(file='1.png')
    canvas.create_image(335,135,image=image1)
    canvas.image=image1
def MillionPicture2():
    canvas=Canvas(ABC2,bg='black',width=670,height=270)
    canvas.grid(row=0,column=0)
    canvas.delete("all")
    image1=PhotoImage(file='2.png')
    canvas.create_image(335,135,image=image1)
    canvas.image=image1
def MillionPicture3():
    canvas=Canvas(ABC2,bg='black',width=670,height=270)
    canvas.grid(row=0,column=0)
    canvas.delete("all")
    image1=PhotoImage(file='3.png')
    canvas.create_image(335,135,image=image1)
    canvas.image=image1
def MillionPicture4():
    canvas=Canvas(ABC2,bg='black',width=670,height=270)
    canvas.grid(row=0,column=0)
    canvas.delete("all")
    image1=PhotoImage(file='4.png')
    canvas.create_image(335,135,image=image1)
    canvas.image=image1



CentreImage=PhotoImage(file='download.png')
LogoCentre=Button(ABC1b,image=CentreImage,bg='black',width=300,height=200)
LogoCentre.grid()

MillionImage=PhotoImage(file='Picture.png')
MillionImg=Button(ABC2,image=MillionImage,bg='black',width=670,height=270)
MillionImg.grid(row=0,column=0)
#================================================
Question1=StringVar()
Question2=StringVar()
Question3=StringVar()
Question4=StringVar()


Answer1=StringVar()
Answer2=StringVar()
Answer3=StringVar()
Answer4=StringVar()

Question1.set("Q1:Time constant of RL circuit is")
Answer1.set("RL")
Answer2.set("L/R")
Answer3.set("R/L")
Answer4.set("L")


def Question2():
    Question1.set("Q2:SOURCE FREE CIRCUIT TRANSIENTS RESPONSE IS CALLED")
    Answer1.set("FORCED")
    Answer2.set("NATURAL")
    Answer3.set("TRANSIENT")
    Answer4.set("NONE")

    MillionPicture1()

def Question3():
    Question1.set("Q3:THE RELATION BETWEEN CURRENT AND VOLTAGE IN CASE OF INDUCTOR IS")
    Answer1.set("V=Ldt/di")
    Answer2.set("V=Ldi/dt")
    Answer3.set("V=dt/di")
    Answer4.set("V=di/dt")
    MillionPicture2()
def Question4():
    Question1.set("Q4:THE VOLTAGE AND CURRENT IN A CAPACITOR ARE RELATED AS")
    Answer1.set("i=Cdt/dv")
    Answer2.set("v=Cdv/dt")
    Answer3.set("i=Cdv/dt")
    Answer4.set("v=Cdt/dv")
    MillionPicture3()
def Question5():
    Question1.set("Q5:THE TRANSFORM IMPEDENCE OF THE INDUCTOR IS")
    Answer1.set("L")
    Answer2.set("1/L")
    Answer3.set("sL")
    Answer4.set("1/sL")
    MillionPicture4()


#==============================================
txtQuestion=Entry(ABC1c,font=('arial',14,'bold'),bg='black',fg='white',bd=3,width=70,justify=CENTER,textvariable=Question1)
txtQuestion.grid(row=0,column=0,columnspan=4,pady=4)
lblQuestionA=Label(ABC1c,font=('arial',14,'bold'),text="A: ",bg='black',fg='white',bd=5,justify=CENTER)
lblQuestionA.grid(row=1,column=0,pady=4,sticky=W)
txtQuestion1=Button(ABC1c,font=('arial',14,'bold'),bg='black',fg='white',bd=1,width=10,height=1,justify=CENTER,textvariable=Answer1,command=Question2)
txtQuestion1.grid(row=1,column=0,pady=4)

lblQuestionB=Label(ABC1c,font=('arial',14,'bold'),text="B: ",bg='black',fg='white',bd=5,justify=CENTER)
lblQuestionB.grid(row=1,column=1,pady=4,sticky=W)
txtQuestion2=Button(ABC1c,font=('arial',14,'bold'),bg='black',fg='white',bd=1,width=10,height=1,justify=CENTER,textvariable=Answer2,command=Question3)
txtQuestion2.grid(row=1,column=1,pady=4)

lblQuestionC=Label(ABC1c,font=('arial',14,'bold'),text="C: ",bg='black',fg='white',bd=5,justify=CENTER)
lblQuestionC.grid(row=2,column=0,pady=4,sticky=W)
txtQuestion3=Button(ABC1c,font=('arial',14,'bold'),bg='black',fg='white',bd=1,width=10,height=1,justify=CENTER,textvariable=Answer3,command=Question4)
txtQuestion3.grid(row=2,column=0,pady=4)

lblQuestionD=Label(ABC1c,font=('arial',14,'bold'),text="D: ",bg='black',fg='white',bd=5,justify=CENTER)
lblQuestionD.grid(row=2,column=1,pady=4,sticky=W)
txtQuestion4=Button(ABC1c,font=('arial',14,'bold'),bg='black',fg='white',bd=1,width=10,height=1,justify=CENTER,textvariable=Answer4,command=Question5)
txtQuestion4.grid(row=2,column=1,pady=4)

root.mainloop()
