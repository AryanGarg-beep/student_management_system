import os
import sqlite3
from tkinter import *
from PIL import Image, ImageTk
from courses import CourseClass
from student import StudentClass
from result import ResultClass
from view_results import viewResultClass
from login import LoginClass
from tkinter import messagebox


class RMS:
    def __init__(self, root):
        self.root=root
        self.root.title("Student Result Manager")
        self.root.config(bg="white")
        self.root.state('zoomed')
        #self.root.geometry("1350x700+0+0")
        self.root.grid_rowconfigure(0, weight=0)  
        self.root.grid_rowconfigure(1, weight=0)  
        self.root.grid_rowconfigure(2, weight=1)  
        self.root.grid_rowconfigure(3, weight=0)  
        self.root.grid_columnconfigure(0, weight=1)

#---------------------------icons-----------------------------

        self.logo_dash = ImageTk.PhotoImage(file="images/logo_p.png")

#---------------------------title-----------------------------
        title = Label(self.root, text="Student Result Management System",
                      compound=LEFT,
                      padx=10,
                      image=self.logo_dash,
                      font=("times new roman", 30, "bold"),
                      bg="#033054", fg="white")
        title.grid(row=0, column=0, sticky='ew')

#---------------------------menu------------------------------
        M_frame = LabelFrame(self.root, text="Menu",
                            font=("times new roman", 15), bg="white")
        M_frame.grid(row=1, column=0, sticky='ew', padx=10, pady=10)
        for i in range(6):
            M_frame.grid_columnconfigure(i, weight=1)
        M_frame.grid_rowconfigure(0, weight=1)

        btn_course = Button(M_frame, text = "Courses",
                             font=("times new roman", 15, "bold"),
                             bg = "#0b5377", fg="white", cursor="hand2", command=self.add_course, height=2)
        btn_course.grid(row=0, column=0, sticky='ew', padx=5, pady=10)
        
        btn_student = Button(M_frame, text = "Students",
                             font=("times new roman", 15, "bold"),
                             bg = "#0b5377", fg="white", cursor="hand2", command=self.add_student, height=2)
        btn_student.grid(row=0, column=1, sticky='ew', padx=5, pady=10)
        
        btn_result = Button(M_frame, text = "Results",
                             font=("times new roman", 15, "bold"),
                             bg = "#0b5377", fg="white", cursor="hand2", command=self.add_result, height=2)
        btn_result.grid(row=0, column=2, sticky='ew', padx=5, pady=10)
        
        btn_view = Button(M_frame, text = "View results",
                             font=("times new roman", 15, "bold"),
                             bg = "#0b5377", fg="white", cursor="hand2", command=self.view_result, height=2)
        btn_view.grid(row=0, column=3, sticky='ew', padx=5, pady=10)
        
        btn_logout = Button(M_frame, text = "Logout",
                             font=("times new roman", 15, "bold"),
                             bg = "#0b5377", fg="white", cursor="hand2", command=self.logout, height=2)
        btn_logout.grid(row=0, column=4, sticky='ew', padx=5, pady=10)
        
        btn_exit = Button(M_frame, text = "Exit",
                             font=("times new roman", 15, "bold"),
                             bg = "#0b5377", fg="white", cursor="hand2", command=self.exit_, height=2)
        btn_exit.grid(row=0, column=5, sticky='ew', padx=5, pady=10)
        

#---------------------------content---------------------------
        Content_frame = Frame(self.root, bg="white")
        Content_frame.grid(row=2, column=0, sticky='nsew')
        Content_frame.grid_rowconfigure(0, weight=1)
        Content_frame.grid_rowconfigure(1, weight=0)
        Content_frame.grid_columnconfigure(0, weight=1)

        self.bg_img = Image.open("images/bg.png")
        self.bg_img = self.bg_img.resize((920, 350), Image.Resampling.LANCZOS)
        self.bg_img = ImageTk.PhotoImage(self.bg_img)
        
        self.lbl=Label(Content_frame, image=self.bg_img, bg="white")
        self.lbl.place(relx=0.5, rely=0.4, anchor='center')  

        Labels_frame = Frame(Content_frame, bg="white")
        Labels_frame.grid(row=1, column=0, sticky='ew', pady=20)
        Labels_frame.grid_columnconfigure(0, weight=1)
        Labels_frame.grid_columnconfigure(1, weight=1)
        Labels_frame.grid_columnconfigure(2, weight=1)


#----------------------------updates--------------------------

        self.lbl_course = Label(Labels_frame, text = "Total courses\n[ 0 ]",
                                font=("times new roman", 20),
                                bg="#e43b06", fg="white", bd=10, relief=RIDGE)
        self.lbl_course.grid(row=0, column=0, sticky='ew', padx=10)
     
        self.lbl_student = Label(Labels_frame, text = "Total Students\n[ 0 ]",
                                font=("times new roman", 20),
                                bg="#0676ad", fg="white", bd=10, relief=RIDGE)
        self.lbl_student.grid(row=0, column=1, sticky='ew', padx=10)

        self.lbl_result = Label(Labels_frame, text = "Total Results\n[ 0 ]",
                                font=("times new roman", 20),
                                bg="#03874d", fg="white", bd=10, relief=RIDGE)
        self.lbl_result.grid(row=0, column=2, sticky='ew', padx=10)


#---------------------------footer-----------------------------
        footer = Label(self.root, text="Student Result Management System | Developed by Aryan",
                       font=("times new roman", 15),
                       bg="#033054", fg="white")
        footer.grid(row=3, column=0, sticky='ew', ipady=10)
        
        self.update_details()


        self.btn_refresh = Button(self.root, text="↻",
                               font=("times new roman", 15, "bold"),
                               bg="#4caf50", fg="white", cursor="hand2", command=self.update_details)
        self.btn_refresh.place(x=20, y=15, width=20, height=20)

#----------------------------functions--------------------------


    def update_details(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            cur.execute("select * from course")
            cr = cur.fetchall()
            self.lbl_course.config(text=f"Total Courses\n[{str(len(cr))}]")
            cur.execute("select * from student")
            cr = cur.fetchall()
            self.lbl_student.config(text=f"Total Students\n[{str(len(cr))}]")
            cur.execute("select * from result")
            cr = cur.fetchall()
            self.lbl_result.config(text=f"Total Results\n[{str(len(cr))}]")
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")

    def add_course(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = CourseClass(self.new_win)

    def add_student(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = StudentClass(self.new_win)

    def add_result(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = ResultClass(self.new_win)
    
    def view_result(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = viewResultClass(self.new_win)
    
    def exit_(self):
        op = messagebox.askyesno("Confirm", "You want to really exit?", parent=self.root)
        if op == True:
            self.root.destroy()
    
    def logout(self):
        op = messagebox.askyesno("Confirm", "You want to really logout?", parent=self.root)
        if op == True:
            self.root.destroy()
            os.system("python login.py")

if __name__ == "__main__":
    root=Tk()
    obj=RMS(root)
    root.mainloop()