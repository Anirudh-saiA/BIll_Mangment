from tkinter import *

root = Tk()
root.geometry("1000x500")
root.title("Bill Mangment")
root.resizable(False,False)


def Reset():
    entry_Dosa.delete(0,END)
    entry_Idly.delete(0,END)
    entry_Vada.delete(0,END)
    entry_Upma.delete(0,END)
    entry_Poori.delete(0,END)
    entry_Coffee.delete(0,END)
    entry_Tea.delete(0,END)

def Total():
    
    try: a1=int(Dosa.get())
    except: a1=0

    try: a2=int(Idly.get())
    except: a2=0

    try: a3=int(Vada.get())
    except: a3=0

    try: a4=int(Upma.get())
    except: a4=0

    try: a5=int(Poori.get())
    except: a5=0

    try: a6=int(Coffee.get())
    except: a6=0

    try: a7=int(Tea.get())
    except: a7=0

    c1=60*a1
    c2=40*a2
    c3=40*a3
    c4=50*a4
    c5=70*a5
    c6=30*a6
    c7=20*a7


    lbl_Total = Label(f2,font=("Arial",20,"bold"),text ="Total",width=17,fg="black",bg="white")
    lbl_Total.place(x=0,y=60)

    entry_Total = Entry(f2,font=("arial",20,"bold"),textvariable= Total_bill,bd=6,width=15,bg="white")
    entry_Total.place(x=20,y=100)

    totalcost = c1+c2+c3+c4+c5+c6+c7
    string_bill = "Rs.",str('%.2f' %totalcost)
    Total_bill.set(string_bill)
    


Label (text="BILL MANAGMENT", bg = "black", fg = "white", font=("calibri", 33),width="300",height="2").pack()

#MENU CARD
f = Frame(root,bg="black",highlightbackground="white",highlightthickness=1,width=300,height=370)
f.place(x=10,y=118)

Label(f,text="Menu",font=("Arial",40,"bold"),fg="white",bg="black").place(x=80,y=0)
Label(f,font=("Verdana",15,),text="Dosa......60/per plate",fg="White",bg="black").place(x=10,y=80)
Label(f,font=("Verdana",15,),text="Idly......40/per plate",fg="White",bg="black").place(x=10,y=110)
Label(f,font=("Verdana",15,),text="Vada......40/per plate",fg="White",bg="black").place(x=10,y=140)
Label(f,font=("Verdana",15,),text="Upma......50/per plate",fg="White",bg="black").place(x=10,y=170)
Label(f,font=("Verdana",15,),text="Poori......70/per plate",fg="White",bg="black").place(x=10,y=230)
Label(f,font=("Verdana",15,),text="Coffee......30/per plate",fg="White",bg="black").place(x=10,y=260)
Label(f,font=("Verdana",15,),text="Tea......20/per plate",fg="White",bg="black").place(x=10,y=290)
Label(f,font=("Verdana",15,),text="Total bill......10/-",fg="White",bg="black").place(x=10,y=320)




f2=Frame(root,bg="white",highlightbackground="black",highlightthickness=1,width=300,height=370)
f2.place(x=690,y=118)

Bill = Label(f2,text="Bill",font=("Arial",40),bg="white")
Bill.place(x=120,y=10)

#ENTRY WORK

f1=Frame(root,bd=5,height=370,width=300,relief=RAISED)
f1.pack()

Dosa = StringVar()
Idly = StringVar()
Vada = StringVar()
Upma = StringVar()
Poori = StringVar()
Coffee = StringVar()
Tea = StringVar()
Total_bill = StringVar()

#LABEL

lb1_Dosa = Label(f1, font = ("Verdana",20),text = "Dosa", width = 12, fg="blue4")
lb1_Idly = Label(f1, font = ("Verdana",20),text = "Idly", width = 12, fg="blue4")
lb1_Vada = Label(f1, font = ("Verdana",20),text = "Vada", width = 12, fg="blue4")
lb1_Upma = Label(f1, font = ("Verdana",20),text = "Upma", width = 12, fg="blue4")
lb1_Poori = Label(f1, font = ("Verdana",20),text = "Poori", width = 12, fg="blue4")
lb1_Coffee = Label(f1, font = ("Verdana",20),text = "Coffee", width = 12, fg="blue4")
lb1_Tea = Label(f1, font = ("Verdana",20),text = "Tea", width = 12, fg="blue4")
lb1_Dosa.grid(row=1,column=0)
lb1_Idly.grid(row=2,column=0)
lb1_Vada.grid(row=3,column=0)
lb1_Upma.grid(row=4,column=0)
lb1_Poori.grid(row=5,column=0)
lb1_Coffee.grid(row=6,column=0)
lb1_Tea.grid(row=7,column=0)


#ENTRY  

entry_Dosa= Entry(f1,font=("Verdana",20),textvariable = Dosa, bd= 6, width=8,bg="white")
entry_Idly= Entry(f1,font=("Verdana",20),textvariable = Idly, bd= 6, width=8,bg="white")
entry_Vada= Entry(f1,font=("Verdana",20),textvariable = Vada, bd= 6, width=8,bg="white")
entry_Upma= Entry(f1,font=("Verdana",20),textvariable = Upma, bd= 6, width=8,bg="white")
entry_Poori= Entry(f1,font=("Verdana",20),textvariable = Poori, bd= 6, width=8,bg="white")
entry_Coffee= Entry(f1,font=("Verdana",20),textvariable = Coffee, bd= 6, width=8,bg="white")
entry_Tea= Entry(f1,font=("Verdana",20),textvariable = Tea, bd= 6, width=8,bg="white")

entry_Dosa.grid(row=1,column=1)
entry_Idly.grid(row=2,column=1)
entry_Vada.grid(row=3,column=1)
entry_Upma.grid(row=4,column=1)
entry_Poori.grid(row=5,column=1)
entry_Coffee.grid(row=6,column=1)
entry_Tea.grid(row=7,column=1)

#BUTTON

Btn_reset = Button(f1,bd=5,fg="black",bg="white",font=("Arial",16),width=10,text="Reset",command= Reset)
Btn_reset.grid(row=8,column=0)


Btn_total = Button(f1,bd=5,fg="black",bg="white",font=("Arial",16),width=10,text="Total",command= Total)
Btn_total.grid(row=8,column=1 )




root.mainloop()

