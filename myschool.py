from tkinter import *
from tkinter import messagebox as msg
from pymysql import *
from schoolmain import *
class Login(Frame): 
    def __init__(self,master):
        super().__init__(master)

        l1=Label(self,text="User Name")
        l2=Label(self,text="Password")
        self.t1=Entry(self,fg='black')
        self.t2=Entry(self,fg='black',show="*")
        self.b1=Button(self,text="Login",command=self.check)
        self.rowconfigure(index=0,pad=10)
        self.rowconfigure(index=1,pad=10)
        self.rowconfigure(index=2,pad=10)
        self.columnconfigure(index=0,pad=10) 
        
        self.columnconfigure(index=1,pad=10)
        l1.grid(row=0,column=0)
        self.t1.grid(row=0,column=1)
        l2.grid(row=1,column=0)
        self.t2.grid(row=1,column=1)
        self.b1.grid(columnspan=2)
        self.pack()

    def check(self):
        con=connect(db='ankit',user='root',password='Mjstar@143',host='localhost')
        cur=con.cursor()
        uid=self.t1.get()
        pwd=self.t2.get()
        cur.execute("select*from login_master where user_name='%s' and password='%s'"%(uid,pwd))
        result=cur.fetchall()
        if(len(result)==1):
            if(result[0][0]=='lokesh'):
                msg.showinfo('Greeting','Welcome sir/madam')
                root=Tk()
                ob=MainMenu(root)
                root.title("School Menu")
                root.state('zoomed')
                root.config(menu=ob.menubar)
                root.mainloop()

            else:
                msg.showinfo('Greeting','Good Morning student')
        self.t1.delete(0,'end')
        self.t2.delete(0,'end')
        self.t1.focus()
        con.close()


room=Tk()
ob=Login(room)
room.title('Login Page')
room.geometry('450x200')
room.mainloop()