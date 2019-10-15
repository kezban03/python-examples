from tkinter import *
from tkinter import ttk
import mysql.connector


def register(*args):
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="159357i",
        database = "example-app"
    )
    cursor = connection.cursor()
    sql = "INSERT INTO users(email,password,firstname,lastname) VALUES (%s,%s,%s,%s)"
    values = (email.get(), password.get(), firstname.get(), lastname.get())
    cursor.execute(sql,values)
    try:
        connection.commit()
    except mysql.connection.Error as err:
        print("hata:", err)
    finally:
        connection.close()

root = Tk()
root.geometry('300x300')
root.title("Authentication APP")
mainframe = ttk.Frame(root, padding="12 12 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
firstname = StringVar()
lastname = StringVar()
email = StringVar()
password = StringVar()

firstname_entry = ttk.Entry(mainframe, width=12, textvariable=firstname).grid(column=2, row=1, sticky=(W, E))
lastname_entry = ttk.Entry(mainframe, width=12, textvariable=lastname).grid(column=2, row=2, sticky=(W, E))
email_entry = ttk.Entry(mainframe, width=12, textvariable=email).grid(column=2, row=3, sticky=(W, E))
password_entry = ttk.Entry(mainframe, width=12, textvariable=password).grid(column=2, row=4, sticky=(W, E))
ttk.Label(mainframe, text="firstname:").grid(column=1, row=1, sticky=W)
ttk.Label(mainframe, text="lastname:").grid(column=1, row=2, sticky=W)
ttk.Label(mainframe, text="email:").grid(column=1, row=3, sticky=W)
ttk.Label(mainframe, text="password:").grid(column=1, row=4, sticky=W)
ttk.Button(mainframe, text="Kayıt Ol", command=register).grid(column=2, row=5, sticky=W)
root.mainloop()


