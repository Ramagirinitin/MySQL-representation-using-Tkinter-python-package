from tkinter import *
import tkinter.messagebox as MessageBox
import mysql.connector as mysql


def insert():
    id = e_id.get()
    name = e_name.get()
    project_name = e_project_name.get()
    status = e_status.get()

    if id == "" or name == "" or project_name == "" or status == "":
        MessageBox.showinfo("Insert Status", "All fields are required")
    else:
        con = mysql.connect(
            host="localhost",
            user="root",
            password="Import@nt1",
            database="project_mysql",
        )
        query = "insert into interns values(%s,%s,%s,%s)"
        cursor = con.cursor()
        cursor.execute(query, (id, name, project_name, status))
        cursor.execute("commit")

        e_id.delete(0, "end")
        e_name.delete(0, "end")
        e_project_name.delete(0, "end")
        e_status.delete(0, "end")
        show()
        MessageBox.showinfo("Insert Status", "Inserted successfully")
        con.close()


def delete():
    id = e_id.get()
    if e_id.get() == "":
        MessageBox.showinfo("Delete Status", "ID is required")
    else:
        con = mysql.connect(
            host="localhost",
            user="root",
            password="Import@nt1",
            database="project_mysql",
        )
        query = "delete from interns where id = '" + id + "'"
        cursor = con.cursor()
        cursor.execute(query)
        cursor.execute("commit")

        e_id.delete(0, "end")
        e_name.delete(0, "end")
        e_project_name.delete(0, "end")
        e_status.delete(0, "end")
        show()
        MessageBox.showinfo("Delete Status", "Deleted successfully")
        con.close()


def get():
    id = e_id.get()
    if e_id.get() == "":
        MessageBox.showinfo("Fetch Status", "ID is required")
    else:
        con = mysql.connect(
            host="localhost",
            user="root",
            password="Import@nt1",
            database="project_mysql",
        )
        query = "select * from interns where id = '" + id + "'"
        cursor = con.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        for row in rows:
            e_name.insert(0, row[1])
            e_project_name.insert(0, row[2])
            e_status.insert(0, row[3])

        con.close()


def show():
    con = mysql.connect(
        host="localhost", user="root", password="Import@nt1", database="project_mysql"
    )
    cursor = con.cursor()
    cursor.execute("select * from interns")
    rows = cursor.fetchall()
    list.delete(0, list.size())

    for row in rows:
        insertData = str(row[0]) + "   " + row[1] + "   " + row[2] + "   " + row[3]
        list.insert(list.size() + 1, insertData)
    con.close()


box = Tk()
box.geometry("600x300")
box.title("MySQL project")

id = Label(box, text="Enter ID", font=("bold", 10))
id.place(x=20, y=30)

name = Label(box, text="Enter Name", font=("bold", 10))
name.place(x=20, y=60)

project_name = Label(box, text="Enter Project_Title", font=("bold", 10))
project_name.place(x=20, y=90)

status = Label(box, text="Enter Status", font=("bold", 10))
status.place(x=20, y=120)

e_id = Entry()
e_id.place(x=150, y=30)

e_name = Entry()
e_name.place(x=150, y=60)

e_project_name = Entry()
e_project_name.place(x=150, y=90)

e_status = Entry()
e_status.place(x=150, y=120)

insert = Button(box, text="insert", font=("italic", 10), bg="white", command=insert)
insert.place(x=20, y=170)

delete = Button(box, text="delete", font=("italic", 10), bg="white", command=delete)
delete.place(x=70, y=170)

get = Button(box, text="get", font=("italic", 10), bg="white", command=get)
get.place(x=130, y=170)

list = Listbox(box, height=10, width=35)
list.place(x=300, y=30)

show()

box.mainloop()
