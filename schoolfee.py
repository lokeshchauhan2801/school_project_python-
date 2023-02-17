from tkinter import *
from tkinter import messagebox as msg
from pymysql import *
from datetime import *
class schoolfee(Frame):
    def __init__(self,master):
        super().__init__(master)

        l1=Label(self,text="Roll-No")
        l2=Label(self,text="Amount")
        l3=Label(self,text="Class")
        self.t1=Entry(self)
        self.t2=Entry(self)
        self.t3=Entry(self)
        self.b1=Button(self,text="Deposit",command=self.fees)
        self.rowconfigure(index=0,pad=10)
        self.rowconfigure(index=1,pad=10)
        self.rowconfigure(index=2,pad=10)
        self.rowconfigure(index=3,pad=10)
        self.columnconfigure(index=0,pad=10)
        self.columnconfigure(index=1,pad=10)
        l1.grid(row=0,column=0)
        self.t1.grid(row=0,column=1)
        l2.grid(row=1,column=0)
        self.t2.grid(row=1,column=1)
        l3.grid(row=2,column=0)
        self.t3.grid(row=2,column=1)
        self.b1.grid(columnspan=2)
        self.pack()  

    def fees(self):
        con=connect(db='ankit',user='root',password='Mjstar@143',host='localhost')
        cur=con.cursor()
        roll_no=int(self.t1.get())
        dt=datetime.now()
        ndate=str(dt.year)+"-"+str(dt.month)+"-"+str(dt.day)
        amount=float(self.t2.get())
        cls=self.t3.get()
        i=cur.execute("insert into student_fee  values(%d,'%s',%f,'%s')"%(roll_no,ndate,amount,cls))
        if(i==1):
            con.commit()
            msg.showinfo('Confirmation','Fee Submitted')
            self.t1.delete(0,'end')
            self.t2.delete(0,'end')
            self.t3.delete(0,'end')
        else:
            msg.showerror('Error','Fee not submitted')
        con.close()