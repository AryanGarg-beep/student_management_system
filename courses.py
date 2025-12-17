from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import sqlite3

class CourseClass:
    def __init__(self, root):
        self.root=root
        self.root.title("Student Result Manager")
        self.root.config(bg="white")
        #self.root.state('zoomed')
        self.root.geometry("1200x480+80+170")
        self.root.focus_force()

#---------------------------title-----------------------------
        title = Label(self.root, text="Course Management",
                      padx=10,
                      compound=LEFT,
                      font=("times new roman", 30, "bold"),
                      bg="#033054", fg="white").place(x=0, y=0, relwidth=1, height=55)
        
#---------------------------variables--------------------------
        self.var_course_name=StringVar()
        self.var_course_duration=StringVar()
        self.var_course_fees=StringVar()

#---------------------------widgets-----------------------------
        lbl_course_name = Label(self.root, text="Course Name",
                                font=("times new roman", 15),
                                bg="white").place(x=10, y=60)
        
        lbl_course_duration = Label(self.root, text="Duration",
                                font=("times new roman", 15),
                                bg="white").place(x=10, y=100)
        
        lbl_course_fees = Label(self.root, text="Fees",
                                font=("times new roman", 15),
                                bg="white").place(x=10, y=140)
        lbl_course_description = Label(self.root, text="Description",
                                font=("times new roman", 15),
                                bg="white").place(x=10, y=180)
        
        
        self.txt_course_name = Entry(self.root, textvariable=self.var_course_name,
                                font=("times new roman", 15),
                                bg="lightyellow")
        self.txt_course_name.place(x=150, y=60, width=200)
        
        txt_course_duration = Entry(self.root, textvariable=self.var_course_duration,
                                font=("times new roman", 15),
                                bg="lightyellow")
        txt_course_duration.place(x=150, y=100, width=200)
        
        txt_course_fees = Entry(self.root, textvariable = self.var_course_fees,
                                font=("times new roman", 15),
                                bg="lightyellow")
        txt_course_fees.place(x=150, y=140, width=200)
        
        self.txt_course_description = Text(self.root,
                                font=("times new roman", 15),
                                bg="lightyellow")
        self.txt_course_description.place(x=150,y=180, width=500, height=100)
        
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


#-----------------------------search pabel---------------------------
        self.var_search=StringVar()


        lbl_search_courseName = Label(self.root, text="Course Name",
                                     font=("times new roman", 15),
                                     bg="white").place(x=720, y=60)                                                        
        txt_search_courseName = Entry(self.root, textvariable=self.var_search,
                                     font=("times new roman", 15),
                                     bg="lightyellow").place(x=870, y=60, width=190)
        
        btn_search = Button(self.root, text="search",
                               font=("times new roman", 15, "bold"),
                               bg="#03a9f4", fg="white", cursor="hand2", command=self.search).place(x=1070, y=60, width=120, height=26)

#----------------------------content------------------------------

        self.C_Frame = Frame(self.root, bd=2, relief=RIDGE)
        self.C_Frame.place(x=720, y=100, width=470, height=340)

        scrolly = Scrollbar(self.C_Frame, orient=VERTICAL)
        scrollx = Scrollbar(self.C_Frame, orient=HORIZONTAL)
        self.courseTable=ttk.Treeview(self.C_Frame, columns=("cid", "name", "duration", "fees", "description"), xscrollcommand=scrollx.set, yscrollcommand=scrolly.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.courseTable.xview)
        scrolly.config(command=self.courseTable.yview)

        self.courseTable.heading("cid", text="Course ID")
        self.courseTable.heading("name", text="Name")
        self.courseTable.heading("duration", text="Duration")
        self.courseTable.heading("fees", text="Fees")
        self.courseTable.heading("description", text="Description")
        self.courseTable["show"]="headings"
        self.courseTable.pack(fill=BOTH, expand=1)
        self.courseTable.bind("<ButtonRelease-1>", self.get_data)
        

        self.courseTable.column("cid", width=50)
        self.courseTable.column("name", width=100)
        self.courseTable.column("duration", width=100)
        self.courseTable.column("fees", width=100)
        self.courseTable.column("description", width=150)
        self.show()

#----------------------------functions--------------------------
    def get_data(self, ev):
        self.txt_course_name.config(state="readonly")
        r = self.courseTable.focus()
        content = self.courseTable.item(r)
        row = content['values']
        self.var_course_name.set(row[1])
        self.var_course_duration.set(row[2])
        self.var_course_fees.set(row[3])
        self.txt_course_description.delete("1.0", END)
        self.txt_course_description.insert(END, row[4])

    def clear(self):
        self.txt_course_name.config(state=NORMAL)
        self.var_course_name.set("")
        self.var_course_duration.set("")
        self.var_course_fees.set("")
        self.var_search.set("")
        self.txt_course_description.delete("1.0", END)
        self.show()


    def add(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            if self.var_course_name.get()=="":
                messagebox.showerror("Error", "course Name should be required", parent=self.root)
            else:
                cur.execute("select * from course where name=?", (self.var_course_name.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error", "course already assigned, try different", parent=self.root)
                else:
                    cur.execute("insert into course(name, duration, fees, description) values(?,?,?,?)",(
                        self.var_course_name.get(),
                        self.var_course_duration.get(),
                        self.var_course_fees.get(),
                        self.txt_course_description.get("1.0", END)
                    ))
                    con.commit()
                    self.show()
                    messagebox.showinfo("success", "course added successfully", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}")

    def update(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            if self.var_course_name.get()=="":
                messagebox.showerror("Error", "course Name should be required", parent=self.root)
            else:
                cur.execute("select * from course where name=?", (self.var_course_name.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error", "Select course from list", parent=self.root)
                else:
                    cur.execute("update course set duration=?, fees=?, description=? where name=?",(
                        self.var_course_duration.get(),
                        self.var_course_fees.get(),
                        self.txt_course_description.get("1.0", END),
                        self.var_course_name.get()
                    ))
                    con.commit()
                    messagebox.showinfo("success", "course added successfully", parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}")

    def delete(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            if self.var_course_name.get()=="":
                messagebox.showerror("Error", "course Name should be required", parent=self.root)
            else:
                cur.execute("select * from course where name=?", (self.var_course_name.get(),))
                row=cur.fetchone()
                if row!=None:
                    op = messagebox.askyesno("confirm", "do you really want to delete?", parent=self.root)
                    if op==True:
                        cur.execute("delete from course where name=?", (self.var_course_name.get(),))
                        con.commit()
                        messagebox.showinfo("Delete", "course deleted successfully", parent=self.root)
                        self.clear()
                else:
                    messagebox.showerror("Error", "Select course from list", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}")

    
    def show(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            cur.execute("select * from course")
            rows=cur.fetchall()
            self.courseTable.delete(*self.courseTable.get_children())
            for row in rows:
                self.courseTable.insert('', END, values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}")

    def search(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            cur.execute(f"select * from course where name LIKE '%{self.var_search.get()}%'")
            rows=cur.fetchall()
            self.courseTable.delete(*self.courseTable.get_children())
            for row in rows:
                self.courseTable.insert('', END, values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}")


if __name__ == "__main__":
    root=Tk()
    obj=CourseClass(root)
    root.mainloop()