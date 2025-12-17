from tkinter import*
from PIL import Image, ImageTk
import sqlite3
from tkinter import ttk, messagebox


class ResultClass:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Result Management System")
        self.root.geometry("1200x480+80+150")
        self.root.config(bg="white")
        self.root.focus_force()

#---------------------------title-----------------------------
        title = Label(self.root, text="Add Student Result",
                      padx=10,
                      compound=LEFT,
                      font=("times new roman", 30, "bold"),
                      bg="#033054", fg="white").place(x=0, y=0, relwidth=1, height=55)

#---------------------------variables--------------------------
        self.var_select=StringVar()
        self.var_name=StringVar()
        self.var_course=StringVar()
        self.var_marks_ob=StringVar()
        self.var_full_marks=StringVar()
        self.roll_list = []
        self.fetch_roll()


#---------------------------widgets----------------------------
        lbl_select = Label(self.root, text="Select Student",
                           font=("times new roman", 15),
                           bg="white").place(x=10, y=100)
        lbl_name = Label(self.root, text="Name",
                           font=("times new roman", 15),
                           bg="white").place(x=10, y=160)
        lbl_course = Label(self.root, text="course",
                           font=("times new roman", 15),
                           bg="white").place(x=10, y=220)
        lbl_marks_ob = Label(self.root, text="Marks Obtained",
                           font=("times new roman", 15),
                            bg="white").place(x=10, y=280)
        lbl_full_marks = Label(self.root, text="Full Marks",
                           font=("times new roman", 15),
                            bg="white").place(x=10, y=340)
        

        self.txt_select = ttk.Combobox(self.root, textvariable=self.var_select,
                                  values=self.roll_list,
                                  font=("times new roman", 15),
                                  state='readonly')
        self.txt_select.place(x=280, y=100, width=200)
        self.txt_select.set("Select")

        self.btn_add = Button(self.root, text="search",
                               font=("times new roman", 15, "bold"),
                               bg="#2196f3", fg="white", cursor="hand2", command=self.search)
        self.btn_add.place(x=500, y=100, width=100, height=30)
        
        txt_name = Entry(self.root, textvariable=self.var_name,
                       font=("times new roman", 15),
                       bg="lightyellow").place(x=280, y=160, width=320)
        
        txt_course = Entry(self.root, textvariable=self.var_course,
                          font=("times new roman", 15),
                          bg="lightyellow").place(x=280, y=220, width=320)
        
        txt_marks_ob = Entry(self.root, textvariable=self.var_marks_ob,
                            font=("times new roman", 15),
                            bg="lightyellow").place(x=280, y=280, width=320)
        
        txt_full_marks = Entry(self.root, textvariable=self.var_full_marks,
                             font=("times new roman", 15),
                             bg="lightyellow").place(x=280, y=340, width=320)
        
#-----------------------------buttons---------------------------
        self.btn_submit = Button(self.root, text="Submit",
                               font=("times new roman", 15, "bold"),
                               bg="#4caf50", fg="white", cursor="hand2", command=self.add)
        self.btn_submit.place(x=300, y=400, width=110, height=40)
        self.btn_clear = Button(self.root, text="Clear",
                                font=("times new roman", 15, "bold"),
                                bg="#607d8b", fg="white", cursor="hand2", command=self.clear)
        self.btn_clear.place(x=420, y=400, width=110, height=40)

#-----------------------------picture----------------------------
        self.bg_img = Image.open("images/result.jpg")
        self.bg_img = self.bg_img.resize((500, 350), Image.Resampling.LANCZOS)
        self.bg_img = ImageTk.PhotoImage(self.bg_img)
        
        self.lbl=Label(self.root, image=self.bg_img).place(x=630, y=100)


    
    def fetch_roll(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            cur.execute("select roll from student")
            rows = cur.fetchall()
            if len(rows) > 0:
                for row in rows:
                    self.roll_list.append(row[0])
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")


    def search(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            cur.execute(f"select name, course from student where roll LIKE '%{self.var_select.get()}%'")
            rows=cur.fetchone()
            if rows!=None:
                self.var_name.set(rows[0])
                self.var_course.set(rows[1])
            else:
                messagebox.showerror("Error", "No record found", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}")

    def clear(self):
        self.var_select.set("Select")
        self.var_name.set("")
        self.var_course.set("")
        self.var_marks_ob.set("")
        self.var_full_marks.set("")

    def add(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            if self.var_name.get()=="":
                messagebox.showerror("Error", "Please select a student", parent=self.root)
            else:
                cur.execute("select * from result where roll=? and course=?", (self.var_select.get(), self.var_course.get()))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error", "result already present", parent=self.root)
                else:
                    per = round((int(self.var_marks_ob.get()) / int(self.var_full_marks.get())) * 100, 3) 

                    cur.execute("insert into result (roll,name ,course ,marks_ob, full_marks ,per) values(?,?,?,?,?,?)",(
                        self.var_select.get(),
                        self.var_name.get(),
                        self.var_course.get(),
                        self.var_marks_ob.get(),
                        self.var_full_marks.get(),
                        str(per)
                    ))
                    con.commit()
                    self.clear()
                    messagebox.showinfo("success", "results added successfully", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}")


if __name__ == "__main__":
    root = Tk()
    obj = ResultClass(root)
    root.mainloop()