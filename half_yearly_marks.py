from tkinter import *
from tkinter import messagebox as msg
from pymysql import *

import tkinter as tk
import mysql.connector


class Half_yearly_marks(Frame): 
    def __init__(self,master):
        super().__init__(master)
        l1=Label(self,text="Roll-No:")
        l2=Label(self,text="Sub Name:")
        l3=Label(self,text="Marks  :")
    
        self.t1=Entry(self)
        self.t2=Entry(self)
        self.t3=Entry(self)
        self.b1=Button(self,text="Submit",command=self.half_exam)
        self.rowconfigure(index=0,pad=10)
        self.rowconfigure(index=1,pad=10)
        self.rowconfigure(index=2,pad=10)
        self.columnconfigure(index=0,pad=10)
        self.columnconfigure(index=1,pad=10)
        l1.grid(row=0,column=0)
        l2.grid(row=1,column=0)
        l3.grid(row=2,column=0)
        self.t1.grid(row=0,column=1)
        self.t2.grid(row=1,column=1)
        self.t3.grid(row=2,column=1)
        self.b1.grid(columnspan=2)
        self.pack()

    def half_exam(self):
        con=connect(db='ankit',user='root',password='Mjstar@143',host='localhost')
        cur=con.cursor()
        roll_no=int(self.t1.get())
        sub_na=self.t2.get()
        marks=int(self.t3.get())
        i=cur.execute("insert into student_exam_details values(%d,'%s','%s',%d)"%(roll_no,'half_yearly_exam',sub_na,marks))
        con.commit()
        con.close()
        if(i==1):
            msg.showinfo('submitted','Anual exam marks submitted',)
            # self.t1.delete(0,'end')
            self.t2.delete(0,'end')
            self.t3.delete(0,'end')
            self.t2.focus()
            
        
        