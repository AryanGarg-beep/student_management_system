import sqlite3

def create_db():
    con=sqlite3.connect('rms.db')
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS course(cid INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, duration TEXT, fees TEXT, description TEXT)")
    con.commit()
    cur.execute("CREATE TABLE IF NOT EXISTS student(roll INTEGER PRIMARY KEY AUTOINCREMENT, name text,email text,gender text, dob text, contact text, admission text, course text, state text, city text, pin text, address text)")
    con.commit()
    cur.execute("CREATE TABLE IF NOT EXISTS result(rid INTEGER PRIMARY KEY AUTOINCREMENT, roll text,name text,course text,marks_ob text, full_marks text,per text)")
    con.commit()
    cur.execute("CREATE TABLE IF NOT EXISTS employee(eid INTEGER PRIMARY KEY AUTOINCREMENT, f_name text,l_name text,contact text,email text, question text,answer text,password text)")
    con.commit()
    con.close()

create_db()