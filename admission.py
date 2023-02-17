from tkinter import *
from datetime import *
from tkinter import messagebox as msg
from pymysql import *
class myadmission(Frame):
    def __init__(self,master):
        super().__init__(master)

        self.l1=Label(self,text="Admission-no")
        self.l2=Label(self,text="Student-Name")
        self.l3=Label(self,text="Father's-Name")
        self.l4=Label(self,text="Mother's-Name")
        self.l5=Label(self,text="Mobile-No")
        self.l6=Label(self,text="Roll-No")
        self.l7=Label(self,text="Class of Admin..")
        self.l8=Label(self,text="Address")
        self.l9=Label(self,text="City")
        self.t1=Entry(self)
        self.t2=Entry(self)
        self.t3=Entry(self)
        self.t4=Entry(self)
        self.t5=Entry(self)
        self.t6=Entry(self)
        self.t7=Entry(self)
        self.t8=Entry(self)
        self.t9=Entry(self)
        self.b1=Button(self,text="Resiger",command=self.savedata)

        self.rowconfigure(index=0,pad=10)
        self.rowconfigure(index=1,pad=10)
        self.rowconfigure(index=2,pad=10)
        self.rowconfigure(index=3,pad=10)
        self.rowconfigure(index=4,pad=10)
        self.rowconfigure(index=5,pad=10)
        self.rowconfigure(index=6,pad=10)
        self.rowconfigure(index=7,pad=10)
        self.rowconfigure(index=8,pad=10)
        self.rowconfigure(index=9,pad=10)
        self.rowconfigure(index=10,pad=10)
        self.rowconfigure(index=11,pad=10)
        self.rowconfigure(index=12,pad=10)
        self.rowconfigure(index=13,pad=10)
        self.columnconfigure(index=0,pad=10)
        self.columnconfigure(index=1,pad=10)

        self.l1.grid(row=0,column=0)
        self.t1.grid(row=0,column=1)

        self.l2.grid(row=1,column=0)
        self.t2.grid(row=1,column=1)

        self.l3.grid(row=2,column=0)
        self.t3.grid(row=2,column=1)

        self.l4.grid(row=3,column=0)
        self.t4.grid(row=3,column=1)

        self.l5.grid(row=4,column=0)
        self.t5.grid(row=4,column=1)

        self.l6.grid(row=5,column=0)
        self.t6.grid(row=5,column=1)

        self.l7.grid(row=6,column=0)
        self.t7.grid(row=6,column=1)

        self.l8.grid(row=7,column=0)
        self.t8.grid(row=7,column=1)

        self.l9.grid(row=8,column=0)
        self.t9.grid(row=8,column=1)

        self.b1.grid(columnspan=2)
        self.pack()

    def savedata(self):
        con=connect(db='ankit',user='root',password='Mjstar@143',host='localhost')
        cur=con.cursor()

        dt=datetime.now()
        ndate=str(dt.year)+"-"+str(dt.month)+"-"+str(dt.day)
        admin_no=int(self.t1.get())
        sname=self.t2.get()
        fname=self.t3.get()
        mname=self.t4.get()
        phn_No=self.t5.get()
        roll_no=int(self.t6.get())
        class_admin=self.t7.get()
        address=self.t8.get()
        city=self.t9.get()

        i=cur.execute("insert into student_personal values(%d,'%s','%s','%s','%s',%d,'%s','%s','%s','%s')"%(admin_no,sname,fname,mname,phn_No,roll_no,class_admin,address,city,ndate))
        con.commit()
        if(i==1):
            msg.showinfo('Confiramtion','Admission success') 
            self.t1.delete(0,'end')
            self.t2.delete(0,'end')
            self.t3.delete(0,'end')
            self.t4.delete(0,'end')
            self.t5.delete(0,'end')
            self.t6.delete(0,'end')
            self.t7.delete(0,'end')
            self.t8.delete(0,'end')
            self.t9.delete(0,'end')
            self.t1.focus()
            con.close()

    def admission(self):
        room=Tk()
        ob=myadmission(room)
        room.title('Open admission')
        room.geometry('450x750')
        room.mainloop()
        
room=Tk()
ob=myadmission(room)
room.mainloop()