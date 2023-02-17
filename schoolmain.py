from tkinter import *
from admission import *
from schoolfee import *
from half_yearly_marks import *
from annual_marks import *
from half_result import *
from annual_result import *
class MainMenu(Frame):
    def __init__(self,m):
        super().__init__(m)

        self.menubar=Menu(self)

        self.file=Menu(self.menubar,tearoff=0)
        self.edit=Menu(self.menubar,tearoff=0)

        self.file.add_command(label='Admission Open',command=self.admission)
        self.file.add_separator()
        self.file.add_command(label='School fee',command=self.fees)
        self.file.add_separator()
        self.file.add_command(label='Exit',command=self.exitprg)

        self.edit.add_command(label='Half-Yearly-marks ',command=self.half_marks)
        self.edit.add_separator()
        self.edit.add_command(label='Anual-Exam-marks',command=self.annual_marks)
        self.edit.add_separator()
        self.edit.add_command(label='Half-yearly-result',command=self.half_result)
        self.edit.add_separator()
        self.edit.add_command(label='Annual-result',command=self.annual_result)

        self.menubar.add_cascade(label='File',underline=0,menu=self.file)
        self.menubar.add_cascade(label='Edit',underline=0,menu=self.edit)

    def exitprg(self):
        quit()  

    def admission(self):
        room=Tk()
        ob=myadmission(room)
        room.title('Open admission')
        room.geometry('450x750')
        room.mainloop()

    def fees(self):
        room=Tk()
        ob=schoolfee(room)
        room.title('School fees')
        room.geometry('450x200')
        room.mainloop()

    def half_marks(self):
        room=Tk()
        ob=Half_yearly_marks(room)
        room.title('Half yearly exam')
        room.geometry('450x750')
        room.mainloop()

    def annual_marks(self):
        room=Tk()
        ob=Annual_marks(room)
        room.title('Annual exam')
        room.geometry('450x7500')
        room.mainloop()

    def half_result(self):
        root = tk.Tk()
        ob = Half_yearly_result(root)
        root.mainloop()
        
    def annual_result(self):
        root = tk.Tk()
        ob = Annual_result(root)
        root.mainloop()