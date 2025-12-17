from tkinter import*
from PIL import Image, ImageTk
import sqlite3
from tkinter import ttk, messagebox
import os


class viewResultClass:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Result Management System")
        self.root.geometry("1200x480+80+170")
        self.root.config(bg="white")
        self.root.focus_force()

#---------------------------title-----------------------------
        title = Label(self.root, text="View Student Results",
                      padx=10,
                      compound=LEFT,
                      font=("times new roman", 30, "bold"),
                      bg="#033054", fg="white").place(x=0, y=0, relwidth=1, height=55)
        
#---------------------------variables--------------------------
        self.var_search = StringVar()
        self.var_id = ""

#----------------------------search------------------------------
        lbl_search = Label(self.root, text="Search By Roll No.", font=(
                        "times new roman", 15, "bold"), bg="white").place(x=350, y=100)
        txt_serach = Entry(self.root, textvariable=self.var_search, font=(
                        "times new roman", 20, "bold"), bg="lightyellow").place(x=520, y=100, width=150)

        btn_search = Button(self.root, text='Search', font=("times new roman", 15, "bold"),
                    bg="#03a9f4", fg="white", cursor="hand2", command=self.search).place(x=680, y=100, width=100, height=35)
        btn_clear = Button(self.root, text='Clear', font=("times new roman", 15, "bold"),
                   bg="gray", fg="white", cursor="hand2", command=self.clear).place(x=800, y=100, width=100, height=35)

        lbl_roll = Label(self.root, text="Roll No.", font=(
                        "times new roman", 15, "bold"), bg="white", bd=2, relief=GROOVE).place(x=150, y=230, width=150, height=50)
        lbl_name = Label(self.root, text="Name", font=(
                        "times new roman", 15, "bold"), bg="white", bd=2, relief=GROOVE).place(x=300, y=230, width=150, height=50)
        lbl_course = Label(self.root, text="Course", font=(
                        "times new roman", 15, "bold"), bg="white", bd=2, relief=GROOVE).place(x=450, y=230, width=150, height=50)
        lbl_marks = Label(self.root, text="Marks Obtained", font=(
                        "times new roman", 15, "bold"), bg="white", bd=2, relief=GROOVE).place(x=600, y=230, width=150, height=50)
        lbl_full_marks = Label(self.root, text="Full Marks", font=(
                        "times new roman", 15, "bold"), bg="white", bd=2, relief=GROOVE).place(x=750, y=230, width=150, height=50)
        lbl_per = Label(self.root, text="Percentage", font=(
                        "times new roman", 15, "bold"), bg="white", bd=2, relief=GROOVE).place(x=900, y=230, width=150, height=50)

        self.roll = Label(self.root,  font=(
                        "times new roman", 15, "bold"), bg="white", bd=2, relief=GROOVE)
        self.roll.place(x=150, y=280, width=150, height=50)
        self.name = Label(self.root,  font=(
                        "times new roman", 15, "bold"), bg="white", bd=2, relief=GROOVE)
        self.name.place(x=300, y=280, width=150, height=50)
        self.course = Label(self.root, font=(
                        "times new roman", 15, "bold"), bg="white", bd=2, relief=GROOVE)
        self.course.place(x=450, y=280, width=150, height=50)
        self.marks = Label(self.root,  font=(
                        "times new roman", 15, "bold"), bg="white", bd=2, relief=GROOVE)
        self.marks.place(x=600, y=280, width=150, height=50)
        self.full_marks = Label(self.root,  font=(
                        "times new roman", 15, "bold"), bg="white", bd=2, relief=GROOVE)
        self.full_marks.place(x=750, y=280, width=150, height=50)
        self.per = Label(self.root,  font=(
                        "times new roman", 15, "bold"), bg="white", bd=2, relief=GROOVE)
        self.per.place(x=900, y=280, width=150, height=50)


        btn_delete = Button(self.root, text="Delete", font = ("times new roman", 15, "bold"),
                            bg="#f44336", fg="white", cursor="hand2", command=self.delete).place(x=500, y=350, width=150, height=35)
        
#------------------------------------functions------------------------------------

    def search(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            if self.var_search.get()=="":
                messagebox.showerror("Error", "Roll no. should be required", parent=self.root)
            else:
                cur.execute(f"select * from result where roll LIKE '%{self.var_search.get()}%'")
                rows=cur.fetchone()
                if rows!=None:
                    self.var_id = rows[0]
                    self.roll.config(text=rows[1])
                    self.name.config(text=rows[2])
                    self.course.config(text=rows[3])
                    self.marks.config(text=rows[4])
                    self.full_marks.config(text=rows[5])
                    self.per.config(text=rows[6])
                else:
                    messagebox.showerror("Error", "No record found", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}")

    def clear(self):
        self.var_id = ""
        self.roll.config(text="")
        self.name.config(text="")
        self.course.config(text="")
        self.marks.config(text="")
        self.full_marks.config(text="")
        self.per.config(text="")
        self.var_search.set("")

    def delete(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            if self.var_id == "":
                messagebox.showerror("Error", "Search student result first", parent=self.root)
            else:
                cur.execute("select * from result where rid=?",(self.var_id,))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Invalid student result", parent=self.root)
                else:
                    op = messagebox.askyesno("Confirm", "Do you realy want to delete?", parent=self.root)
                    if op == True:
                        cur.execute("delete from result where rid =?",(self.var_id,))
                        con.commit()
                        messagebox.showinfo("Delete", "Result deleted successfully", parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")


if __name__ == "__main__":
    root = Tk()
    obj = viewResultClass(root)
    root.mainloop()
