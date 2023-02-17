
import tkinter as tk
import mysql.connector

class Half_yearly_result:
    def __init__(self,root):
        # Connect to MySQL database
        conn = mysql.connector.connect(
          host="localhost",
          user="root",
          password="Mjstar@143",
          database="ankit"
        )

        # Create a cursor to interact with the database
        cursor = conn.cursor()

        self.root = root
        self.root.title("Half_yearly_exam")
        
        # Create a button to fetch data from the table
        fetch_button = tk.Button(self.root, text="Show-Result", command=self.fetch_data)
        fetch_button.grid(row=0, column=3, pady=10)
  
       # create a button and entry for asking roll_no and exam_name  where exam name is pre-defined  and roll_no is user_input
        total_button = tk.Button(self.root, text="Total", command=self.total)
        total_button.grid(row=0, column=4, pady=10)
       #create a percentage button to get % of marks
        percentage_button = tk.Button(self.root, text="Percentage", command=self.percentage)
        percentage_button.grid(row=0, column=5, pady=20)    
        
       #percentage grid for percetage sign
        percentage_label= tk.Label(self.root,text="%")

        percentage_label.grid(row=2, column=6)
       #create a roll_no label and entry thorugh which user can get a specific result according to his/her need 
        roll_no_button = tk.Label(self.root, text="Roll_no")
        roll_no_button.grid(row=0, column=0, pady=10)

        # Create a label for each column
        roll_no_label = tk.Label(self.root, text="Roll No.")
        roll_no_label.grid(row=1, column=0)

        #roll number entry
        self.roll_no_entry = tk.Entry(self.root)
        self.roll_no_entry.grid(row=0, column=1, pady=10)

        roll_no_label = tk.Label(self.root, text="Roll No.")
        roll_no_label.grid(row=1, column=0)

  
        exam_name_label = tk.Label(self.root, text="Tatal-Marks")
        exam_name_label.grid(row=1, column=4)

        exam_name_label = tk.Label(self.root, text="Exam Name")
        exam_name_label.grid(row=1, column=1)

        sub_name_label = tk.Label(self.root, text="Subject Name")
        sub_name_label.grid(row=1, column=2)

        marks_label = tk.Label(self.root, text="Marks")
        marks_label.grid(row=1, column=3)

        exam_name_label = tk.Label(self.root, text="Percentage")
        exam_name_label.grid(row=1, column=5) 
        
        self.conn = conn
        self.cursor = cursor


    def fetch_data(self):

        # Execute the SQL query to fetch data from the table
        roll_no=self.roll_no_entry.get()

        self.cursor.execute(f"SELECT * FROM student_exam_details where(roll_no={roll_no} and exam_name='half_yearly_exam')")

        # Fetch all the data from the table
        results = self.cursor.fetchall()     
        # Loop through the results and display the data in the window
        for index, row in enumerate(results):
            roll_no = tk.Label(self.root, text=row[0])

            roll_no.grid(row=index + 2, column=0)

            exam_name = tk.Label(self.root, text=row[1])
            exam_name.grid(row=index + 2, column=1)

            sub_name = tk.Label(self.root, text=row[2])
            sub_name.grid(row=index + 2, column=2)

            marks = tk.Label(self.root, text=row[3])
            marks.grid(row=index + 2, column=3)
            
    def total(self):
        # Execute the SQL query to fetch data from the table
        roll_no=self.roll_no_entry.get()

        self.cursor.execute(f"SELECT sum(marks) FROM student_exam_details where(roll_no={roll_no} and exam_name='half_yearly_exam')")

        # Fetch all the data from the table
        result = self.cursor.fetchall()
        
        marks_label= tk.Label(self.root, text=result[0])

        marks_label.grid(row=2, column=4)  
    def percentage(self):
        # Execute the SQL query to fetch data from the table
        roll_no=self.roll_no_entry.get()

        self.cursor.execute(f"SELECT sum(marks)/5 FROM student_exam_details where(roll_no={roll_no} and exam_name='half_yearly_exam')")

        # Fetch all the data from the table
        result1= self.cursor.fetchall()
        
        percentage_label= tk.Label(self.root, text=result1[0])

        percentage_label.grid(row=2, column=5)     
        
