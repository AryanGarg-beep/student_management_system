from tkinter import*
from PIL import Image, ImageTk
import sqlite3
from tkinter import ttk, messagebox



class StudentClass:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Result Management System")
        self.root.geometry("1200x480+80+150")
        self.root.config(bg="white")
        self.root.focus_force()

#---------------------------title-----------------------------
        title = Label(self.root, text="Student Management",
                      padx=10,
                      compound=LEFT,
                      font=("times new roman", 30, "bold"),
                      bg="#033054", fg="white").place(x=0, y=0, relwidth=1, height=55)

#---------------------------variables--------------------------
        self.var_roll=StringVar()
        self.var_name=StringVar()
        self.var_email=StringVar()
        self.var_gender=StringVar()
        self.var_state=StringVar()
        self.var_city=StringVar()
        self.var_pin=StringVar()
        self.var_contact=StringVar()
        self.var_dob=StringVar()
        self.var_course=StringVar()
        self.var_admission=StringVar()



#---------------------------widgets-----------------------------
#---------------------------left side-----------------------------
        lbl_roll = Label(self.root, text="Roll No",
                                font=("times new roman", 15),
                                bg="white").place(x=10, y=60)
        lbl_name = Label(self.root, text="Name",
                                font=("times new roman", 15),
                                bg="white").place(x=10, y=100)
        lbl_email = Label(self.root, text="Email",
                                font=("times new roman", 15),
                                bg="white").place(x=10, y=140)
        lbl_gender = Label(self.root, text="Gender",
                                font=("times new roman", 15),
                                bg="white").place(x=10, y=180)
        lbl_state = Label(self.root, text="State",
                                font=("times new roman", 15),
                                bg="white").place(x=10, y=220)
        lbl_city = Label(self.root, text="City",
                                font=("times new roman", 15),
                                bg="white").place(x=310, y=220)
        lbl_address = Label(self.root, text="Address",
                                font=("times new roman", 15),
                                bg="white").place(x=10, y=260)
#---------------------------right side-----------------------------
        lbl_dob = Label(self.root, text="DOB",
                                font=("times new roman", 15),
                                bg="white").place(x=360, y=60)
        lbl_contact = Label(self.root, text="Contact",
                                font=("times new roman", 15),
                                bg="white").place(x=360, y=100)
        lbl_admission = Label(self.root, text="Admission",
                                font=("times new roman", 15),
                                bg="white").place(x=360, y=140)
        lbl_course = Label(self.root, text="Course",
                                font=("times new roman", 15),
                                bg="white").place(x=360, y=180)
        lbl_pin = Label(self.root, text="Pin Code",
                                font=("times new roman", 15),
                                bg="white").place(x=480, y=220)
        
#---------------------------left side entries-----------------------------
        
        self.txt_roll = Entry(self.root, textvariable=self.var_roll,
                                font=("times new roman", 15),
                                bg="lightyellow")
        self.txt_roll.place(x=150, y=60, width=200)
        self.txt_name = Entry(self.root, textvariable=self.var_name,
                                font=("times new roman", 15),
                                bg="lightyellow")
        self.txt_name.place(x=150, y=100, width=200)
        self.txt_email = Entry(self.root, textvariable=self.var_email,
                                font=("times new roman", 15),
                                bg="lightyellow")
        self.txt_email.place(x=150, y=140, width=200)
        self.txt_gender = ttk.Combobox(self.root, textvariable=self.var_gender, values=("Select","Male","Female","Other"),
                                font=("times new roman", 15),
                                state='readonly', justify=CENTER)
        self.txt_gender.place(x=150, y=180, width=200)
        self.txt_gender.current(0)

        self.txt_state = Entry(self.root, textvariable=self.var_state,
                                font=("times new roman", 15),
                                bg="lightyellow")
        self.txt_state.place(x=150, y=220, width=150)
        self.txt_city = Entry(self.root, textvariable=self.var_city,
                                font=("times new roman", 15),
                                bg="lightyellow")
        self.txt_city.place(x=360, y=220, width=110)

#---------------------------right side entries-----------------------------

        self.course_list = ["select"]
        self.fetch_course()


        self.txt_dob = Entry(self.root, textvariable=self.var_dob,
                                font=("times new roman", 15),
                                bg="lightyellow")
        self.txt_dob.place(x=480, y=60, width=200)
        self.txt_contact = Entry(self.root, textvariable=self.var_contact,
                                font=("times new roman", 15),
                                bg="lightyellow")
        self.txt_contact.place(x=480, y=100, width=200)
        self.txt_admission = Entry(self.root, textvariable=self.var_admission,
                                font=("times new roman", 15),
                                bg="lightyellow")
        self.txt_admission.place(x=480, y=140, width=200)
        self.txt_course = ttk.Combobox(self.root, textvariable=self.var_course, values=self.course_list,
                                font=("times new roman", 15),
                                state='readonly', justify=CENTER)
        self.txt_course.place(x=480, y=180, width=200)
        self.txt_course.current(0)

        self.txt_pin = Entry(self.root, textvariable=self.var_pin,
                                font=("times new roman", 15),
                                bg="lightyellow")
        self.txt_pin.place(x=580, y=220, width=100)
        
        self.txt_address = Text(self.root,
                                font=("times new roman", 15),
                                bg="lightyellow")
        self.txt_address.place(x=150,y=260, width=530, height=80)
        
#---------------------------buttons-----------------------------
        self.btn_add = Button(self.root, text="save",
                               font=("times new roman", 15, "bold"),
                               bg="#2196f3", fg="white", cursor="hand2", command=self.add)
        self.btn_add.place(x=150, y=400, width=110, height=40)
        self.btn_update = Button(self.root, text="update",
                               font=("times new roman", 15, "bold"),
                               bg="#4caf50", fg="white", cursor="hand2", command=self.update)
        self.btn_update.place(x=270, y=400, width=110, height=40)
        self.btn_delete = Button(self.root, text="delete",
                               font=("times new roman", 15, "bold"),
                               bg="#f44336", fg="white", cursor="hand2", command=self.delete)
        self.btn_delete .place(x=390, y=400, width=110, height=40)
        self.btn_clear = Button(self.root, text="clear",
                               font=("times new roman", 15, "bold"),
                               bg="#607d8b", fg="white", cursor="hand2", command=self.clear)
        self.btn_clear .place(x=510, y=400, width=110, height=40)

#-----------------------------search panel---------------------------
        self.var_search=StringVar()


        lbl_search_courseName = Label(self.root, text="Roll No or Name",
                                     font=("times new roman", 15),
                                     bg="white").place(x=720, y=60)                                                        
        txt_search_courseName = Entry(self.root, textvariable=self.var_search,
                                     font=("times new roman", 15),
                                     bg="lightyellow").place(x=870, y=60, width=190)
        
        btn_search = Button(self.root, text="search",
                               font=("times new roman", 15, "bold"),
                               bg="#03a9f4", fg="white", cursor="hand2", command=self.search)
        btn_search.place(x=1070, y=60, width=120, height=26)

#------------------------------content--------------------------------
        self.C_Frame = Frame(self.root, bd=2, relief=RIDGE)
        self.C_Frame.place(x=720, y=100, width=470, height=340)

        scrolly = Scrollbar(self.C_Frame, orient=VERTICAL)
        scrollx = Scrollbar(self.C_Frame, orient=HORIZONTAL)
        self.courseTable=ttk.Treeview(self.C_Frame, columns=("roll", "name", "email", "gender", "dob", "contact", "admission", "course", "state", "city", "pin", "address"), xscrollcommand=scrollx.set, yscrollcommand=scrolly.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.courseTable.xview)
        scrolly.config(command=self.courseTable.yview)

        self.courseTable.heading("roll", text="Roll No.")
        self.courseTable.heading("name", text="Name")
        self.courseTable.heading("email", text="Email")
        self.courseTable.heading("gender", text="Gender")
        self.courseTable.heading("dob", text="D.O.B")
        self.courseTable.heading("contact", text="Contact")
        self.courseTable.heading("admission", text="Admission")
        self.courseTable.heading("course", text="Course")
        self.courseTable.heading("state", text="State")
        self.courseTable.heading("city", text="City")
        self.courseTable.heading("pin", text="PIN")
        self.courseTable.heading("address", text="Address")
        self.courseTable["show"]="headings"
        self.courseTable.pack(fill=BOTH, expand=1)
        self.courseTable.bind("<ButtonRelease-1>", self.get_data)

        self.courseTable.column("roll", width=100)
        self.courseTable.column("name", width=100)
        self.courseTable.column("email", width=100)
        self.courseTable.column("gender", width=100)
        self.courseTable.column("dob", width=100)
        self.courseTable.column("contact", width=100)
        self.courseTable.column("admission", width=100)
        self.courseTable.column("course", width=100)
        self.courseTable.column("state", width=100)
        self.courseTable.column("city", width=100)
        self.courseTable.column("pin", width=100)
        self.courseTable.column("address", width=200)
        self.show()
        
#----------------------------functions--------------------------

    def get_data(self, ev):
        self.txt_roll.config(state='readonly')
        r = self.courseTable.focus()
        content = self.courseTable.item(r)
        row = content["values"]
        self.var_roll.set(row[0]),
        self.var_name.set(row[1]),
        self.var_email.set(row[2]),
        self.var_gender.set(row[3]),
        self.var_dob.set(row[4]),
        self.var_contact.set(row[5]),
        self.var_admission.set(row[6]),
        self.var_course.set(row[7]),
        self.var_state.set(row[8]),
        self.var_city.set(row[9]),
        self.var_pin.set(row[10]),
        self.txt_address.delete("1.0", END)
        self.txt_address.insert(END, row[11])

    def clear(self):
        self.show()
        self.var_roll.set(""),
        self.var_name.set(""),
        self.var_email.set(""),
        self.var_gender.set("Select"),
        self.var_dob.set(""),
        self.var_contact.set(""),
        self.var_admission.set(""),
        self.var_course.set("Select"),
        self.var_state.set(""),
        self.var_city.set(""),
        self.var_pin.set(""),
        self.txt_address.delete("1.0", END)
        self.txt_roll.config(state=NORMAL)
        self.var_search.set("")



    def add(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            if self.var_roll.get()=="":
                messagebox.showerror("Error", "Roll Number should be required", parent=self.root)
            elif "@" not in self.var_email.get() or "." not in self.var_email.get():
                messagebox.showerror("Error", "Invalid Email Address", parent=self.root)
            elif self.var_contact.get().isnumeric()==False or len(self.var_contact.get())!=10:
                messagebox.showerror("Error", "Invalid Contact Number", parent=self.root)
            elif self.var_pin.get().isnumeric()==False or len(self.var_pin.get())!=6:
                messagebox.showerror("Error", "Invalid Pin Code", parent=self.root)
            elif self.var_name.get().isalpha()==False:
                messagebox.showerror("Error", "Invalid Name", parent=self.root)
            else:
                cur.execute("select * from student where roll=?", (self.var_roll.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error", "Roll Number already present", parent=self.root)
                else:
                    cur.execute("insert into student(roll, name, email, gender, dob, contact, admission, course, state, city, pin, address) values(?,?,?,?,?,?,?,?,?,?,?,?)",(
                        self.var_roll.get(),
                        self.var_name.get(),
                        self.var_email.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_contact.get(),
                        self.var_admission.get(),
                        self.var_course.get(),
                        self.var_state.get(),
                        self.var_city.get(),
                        self.var_pin.get(),
                        self.txt_address.get("1.0", END)
                    ))
                    con.commit()
                    self.show()
                    messagebox.showinfo("success", "student added successfully", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}")

    def update(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            if self.var_roll.get()=="":
                messagebox.showerror("Error", "Roll Number should be required", parent=self.root)
            elif "@" not in self.var_email.get() or "." not in self.var_email.get():
                messagebox.showerror("Error", "Invalid Email Address", parent=self.root)
            elif self.var_contact.get().isnumeric()==False or len(self.var_contact.get())!=10:
                messagebox.showerror("Error", "Invalid Contact Number", parent=self.root)
            elif self.var_pin.get().isnumeric()==False or len(self.var_pin.get())!=6:
                messagebox.showerror("Error", "Invalid Pin Code", parent=self.root)
            elif self.var_name.get().isalpha()==False:
                messagebox.showerror("Error", "Invalid Name", parent=self.root)
            else:
                cur.execute("select * from student where roll=?", (self.var_roll.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error", "Select student from list", parent=self.root)
                else:
                    cur.execute("update student set name=?, email=?, gender=?, dob=?, contact=?, admission=?, course=?, state=?, city=?, pin=?, address=? where roll=?",(
                        self.var_name.get(),
                        self.var_email.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_contact.get(),
                        self.var_admission.get(),
                        self.var_course.get(),
                        self.var_state.get(),
                        self.var_city.get(),
                        self.var_pin.get(),
                        self.txt_address.get("1.0", END),
                        self.var_roll.get()
                    ))
                    con.commit()
                    messagebox.showinfo("success", "student updated successfully", parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}")

    def delete(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            if self.var_roll.get()=="":
                messagebox.showerror("Error", "student Name should be required", parent=self.root)
            else:
                cur.execute("select * from student where roll=?", (self.var_roll.get(),))
                row=cur.fetchone()
                if row!=None:
                    op = messagebox.askyesno("confirm", "do you really want to delete?", parent=self.root)
                    if op==True:
                        cur.execute("delete from student where roll=?", (self.var_roll.get(),))
                        con.commit()
                        messagebox.showinfo("Delete", "student deleted successfully", parent=self.root)
                        self.clear()
                else:
                    messagebox.showerror("Error", "Select student from list", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}")

    
    def show(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            cur.execute("select * from student")
            rows = cur.fetchall()
            self.courseTable.delete(*self.courseTable.get_children())
            for row in rows:
                self.courseTable.insert('', END, values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")

    def search(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            cur.execute(f"select * from student where roll LIKE '%{self.var_search.get()}%' OR name LIKE '%{self.var_search.get()}%'")
            rows=cur.fetchall()
            self.courseTable.delete(*self.courseTable.get_children())
            for row in rows:
                self.courseTable.insert('', END, values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}")
    
    def fetch_course(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            cur.execute("select name from course")
            rows = cur.fetchall()
            if len(rows) > 0:
                for row in rows:
                    self.course_list.append(row[0])
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")
        

if __name__ == "__main__":
    root=Tk()
    obj=StudentClass(root)
    root.mainloop()