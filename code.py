def Add():
    plot_id = e1.get()
    owner_name = e2.get()
    size = e3.get()
    price = e4.get()

    mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="realestate")
    mycursor = mysqldb.cursor()

    try:
        sql = "INSERT INTO realestatemanagement (plotid, ownername, size, price) VALUES (%s, %s, %s, %s)"
        val = (plot_id, owner_name, size, price)
        mycursor.execute(sql, val)
        mysqldb.commit()
        messagebox.showinfo("", "Plot added!")
        e1.delete(0, tk.END)
        e2.delete(0, tk.END)
        e3.delete(0, tk.END)
        e4.delete(0, tk.END)
        e1.focus_set()
    except Exception as e:
        print(e)
        mysqldb.rollback()
    finally:
        mysqldb.close()

def update():
    plot_id = e1.get()
    owner_name = e2.get()
    size = e3.get()
    price = e4.get()

    mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="realestate")
    mycursor = mysqldb.cursor()

    try:
        sql = "UPDATE realestatemanagement SET ownername=%s, size=%s, price=%s WHERE plotid=%s"
        val = (owner_name, size, price, plot_id)
        mycursor.execute(sql, val)
        mysqldb.commit()
        messagebox.showinfo("", "Plot updated!")
        e1.delete(0, tk.END)
        e2.delete(0, tk.END)
        e3.delete(0, tk.END)
        e4.delete(0, tk.END)
        e1.focus_set()
    except Exception as e:
        print(e)
        mysqldb.rollback()
    finally:
        mysqldb.close()

def search():
    mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="realestate")
    mycursor = mysqldb.cursor()

    try:
        mycursor.execute("SELECT plotid, ownername, size, price FROM realestatemanagement")
        records = mycursor.fetchall()
        for rec in records:
            msg = f"Plot number: {rec[0]}\nOwner name: {rec[1]}\nSize: {rec[2]}\nPrice: {rec[3]}"
            messagebox.showinfo("Plot Details", msg)
    except Exception as e:
        print(e)
    finally:
        mysqldb.close()

def delete():
    plot_id = e1.get()

    mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="realestate")
    mycursor = mysqldb.cursor()

    try:
        sql = "DELETE FROM realestatemanagement WHERE plotid=%s"
        val = (plot_id,)
        mycursor.execute(sql, val)
        mysqldb.commit()
        messagebox.showinfo("", "Plot deleted!")
        e1.delete(0, tk.END)
        e2.delete(0, tk.END)
        e3.delete(0, tk.END)
        e4.delete(0, tk.END)
        e1.focus_set()
    except Exception as e:
        print(e)
        mysqldb.rollback()
    finally:
        mysqldb.close()

def GetValue(event):
    e1.delete(0, tk.END)
    e2.delete(0, tk.END)
    e3.delete(0, tk.END)
    e4.delete(0, tk.END)
    row_id = listBox.selection()[0]
    select = listBox.set(row_id)
    e1.insert(0, select['Plot number'])
    e2.insert(0, select['Owner Name'])
    e3.insert(0, select['Size'])
    e4.insert(0, select['Price'])

def show():
    mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="realestate")
    mycursor = mysqldb.cursor()
    try:
        mycursor.execute("SELECT plotid, ownername, size, price FROM realestatemanagement")
        records = mycursor.fetchall()
        for i, (plot_id, owner_name, size, price) in enumerate(records, start=1):
            listBox.insert("", "end", values=(plot_id, owner_name, size, price))
    except Exception as e:
        print(e)
    finally:
        mysqldb.close()

root = tk.Tk(className=' Real Estate Management System')
root.geometry("800x500")
root.configure(bg='light blue')

tk.Label(root, text="Plot number").place(x=10, y=40)
tk.Label(root, text="Owner Name").place(x=10, y=70)
tk.Label(root, text="Size").place(x=10, y=100)
tk.Label(root, text="Price").place(x=10, y=130)

e1 = tk.Entry(root)
e1.place(x=140, y=40)

e2 = tk.Entry(root)
e2.place(x=140, y=70)

e3 = tk.Entry(root)
e3.place(x=140, y=100)

e4 = tk.Entry(root)
e4.place(x=140, y=130)

tk.Button(root, text="Add", command=Add, height=3, width=13).place(x=30, y=160)
tk.Button(root, text="Update", command=update, height=3, width=13).place(x=140, y=160)
tk.Button(root, text="Delete", command=delete, height=3, width=13).place(x=250, y=160)
tk.Button(root, text="Search", command=search, height=3, width=13).place(x=360, y=160)

cols = ('Plot number', 'Owner Name', 'Size', 'Price')
listBox = ttk.Treeview(root, columns=cols, show='headings')

for col in cols:
    listBox.heading(col, text=col)
    listBox.grid(row=1, column=0, columnspan=2)
    listBox.place(x=1, y=260)

show()
listBox.bind('<Double-Button-1>', GetValue)

root.mainloop()
