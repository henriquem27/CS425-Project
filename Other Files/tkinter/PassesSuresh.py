def func_InsertPassData():
    conn = psycopg2.connect(
        host="127.0.0.1",
        database='Project-Test',
        user='postgres',
        password='123qw123'
    )
    try:
        player_id = int(player_id_entry.get())
        minute = int(minute_entry.get())
        passes = int(passes_entry.get())
        distance = float(distance_entry.get())
        vertical = float(vertical_entry.get())
        cursor = conn.cursor()
        QUERY = "INSERT INTO Passes (Player_ID, Minute, Passes, Distance, Vertical) VALUES (%s, %s, %s, %s, %s);"
        DATA = (player_id, minute, passes, distance, vertical)
        cursor.execute(QUERY, DATA)
        conn.commit()
        MessageBox.showinfo("OK", "Data Successfully Inserted")
    except:
        MessageBox.showerror("OPS", "Something went wrong. Please check the data")
    finally:
        conn.close()

def func_SelectPassData():
    conn = psycopg2.connect(
        host="127.0.0.1",
        database='Project-Test',
        user='postgres',
        password='123qw123'
    )
    try:
        player_id = int(player_id_select.get())
        if player_id == "":
            MessageBox.showerror("Error", "Please enter a Player ID to be selected")
        else:
            cursor = conn.cursor()
            QUERY = "SELECT * FROM Passes WHERE Player_ID=%s;"
            cursor.execute(QUERY, (player_id,))
            rows = cursor.fetchall()
            passes_listbox.delete(0, END)
            if rows:
                for row in rows:
                    passes_listbox.insert(END, row)
                MessageBox.showinfo("Success", "Data Found")
            else:
                MessageBox.showinfo("Info", "Data not found")
    except:
        MessageBox.showinfo("Alert", "Something went wrong.")
    finally:
        conn.close()

def func_UpdatePassData():
    conn = psycopg2.connect(
        host="127.0.0.1",
        database='Project-Test',
        user='postgres',
        password='123qw123'
    )
    try:
        player_id = int(player_id_update.get())
        minute = int(minute_update.get())
        passes = int(passes_update.get())
        distance = float(distance_update.get())
        vertical = float(vertical_update.get())
        if player_id == "":
            MessageBox.showerror("Error", "Please enter a Player ID to be updated")
        else:
            cursor = conn.cursor()
            QUERY = "UPDATE Passes SET Minute=%s, Passes=%s, Distance=%s, Vertical=%s WHERE Player_ID=%s;"
            DATA = (minute, passes, distance, vertical, player_id)
            cursor.execute(QUERY, DATA)
            conn.commit()
            MessageBox.showinfo("Success", "Data was updated")
    except:
        MessageBox.showinfo("Alert", "Something went wrong.")
    finally:
        conn.close()

def func_DeletePassData():
    conn = psycopg2.connect(
        host="127.0.0.1",
        database='Project-Test',
        user='postgres',
        password='123qw123'
    )
    try:
        player_id = int(player_id_delete.get())
        if player_id == "":
            MessageBox.showerror("Error", "Please enter a Player ID to be deleted")
        else:
            cursor = conn.cursor()
            QUERY = "DELETE FROM Passes WHERE Player_ID=%s;"
            DATA = (player_id,)
            cursor.execute(QUERY, DATA)
            conn.commit()
            MessageBox.showinfo("Success", "Data was deleted")
    except:
        MessageBox.showinfo("Alert", "Something went wrong.")
    finally:
        conn.close()

# Create an Entry widget to accept User Input for Passes
Create_l = Label(tabpasses, text="Insert Into Passes")
Create_l.grid(row=0, column=1, pady=30, padx=30)

L1 = Label(tabpasses, text="Player ID")
L1.grid(row=1, column=0)
player_id_entry = Entry(tabpasses, bd=5)
player_id_entry.focus_set()
player_id_entry.grid(row=1, column=1)

L2 = Label(tabpasses, text="Minute")
L2.grid(row=2, column=0)
minute_entry = Entry(tabpasses, bd=5)
minute_entry.focus_set()
minute_entry.grid(row=2, column=1)

L3 = Label(tabpasses, text="Passes")
L3.grid(row=3, column=0)
passes_entry = Entry(tabpasses, bd=5)
passes_entry.focus_set()
passes_entry.grid(row=3, column=1)

L4 = Label(tabpasses, text="Distance")
L4.grid(row=4, column=0)
distance_entry = Entry(tabpasses, bd=5)
distance_entry.focus_set()
distance_entry.grid(row=4, column=1)

L5 = Label(tabpasses, text="Vertical")
L5.grid(row=5, column=0)
vertical_entry = Entry(tabpasses, bd=5)
vertical_entry.focus_set()
vertical_entry.grid(row=5, column=1)

Button(tabpasses, text="INSERT", width=20, command=lambda: func_InsertPassData()).grid(row=6, column=1)

# Create widgets for the Select, Update, and Delete sections
Select_l = Label(tabpasses, text="Select a Pass")
Select_l.grid(row=0, column=2, pady=30, padx=30)

L6 = Label(tabpasses, text="Player ID")
L6.grid(row=1, column=2)
player_id_select = Entry(tabpasses, bd=5)
player_id_select.focus_set()
player_id_select.grid(row=1, column=2)

Button(tabpasses, text="SELECT", width=20, command=lambda: func_SelectPassData()).grid(row=2, column=2)

Update_l = Label(tabpasses, text="Update a Pass")
Update_l.grid(row=3, column=2, pady=30, padx=30)

L7 = Label(tabpasses, text="Player ID")
L7.grid(row=4, column=2)
player_id_update = Entry(tabpasses, bd=5)
player_id_update.focus_set()
player_id_update.grid(row=4, column=2)

L8 = Label(tabpasses, text="Minute")
L8.grid(row=5, column=2)
minute_update = Entry(tabpasses, bd=5)
minute_update.focus_set()
minute_update.grid(row=5, column=2)

L9 = Label(tabpasses, text="Passes")
L9.grid(row=6, column=2)
passes_update = Entry(tabpasses, bd=5)
passes_update.focus_set()
passes_update.grid(row=6, column=2)

L10 = Label(tabpasses, text="Distance")
L10.grid(row=7, column=2)
distance_update = Entry(tabpasses, bd=5)
distance_update.focus_set()
distance_update.grid(row=7, column=2)

L11 = Label(tabpasses, text="Vertical")
L11.grid(row=8, column=2)
vertical_update = Entry(tabpasses, bd=5)
vertical_update.focus_set()
vertical_update.grid(row=8, column=2)

Button(tabpasses, text="UPDATE", width=20, command=lambda: func_UpdatePassData()).grid(row=9, column=2)

Delete_l = Label(tabpasses, text="Delete a Pass")
Delete_l.grid(row=10, column=2, pady=30, padx=30)

L12 = Label(tabpasses, text="Player ID")
L12.grid(row=11, column=2)
player_id_delete = Entry(tabpasses, bd=5)
player_id_delete.focus_set()
player_id_delete.grid(row=11, column=2)

Button(tabpasses, text="DELETE", width=20, command=lambda: func_DeletePassData()).grid(row=12, column=2)

# Create a Listbox to display selected pass data
passes_listbox = Listbox(tabpasses, height=6, width=75)
passes_listbox.grid(row=13, column=2, rowspan=6, columnspan=2)

root.mainloop()