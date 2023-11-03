def func_InsertGoalData():
    conn = psycopg2.connect(
        host="127.0.0.1",
        database='Project-Test',
        user='postgres',
        password='123qw123'
    )
    try:
        player_id = int(player_id_entry.get())
        assisting_player = assisting_player_entry.get()
        scorer_name = scorer_name_entry.get()
        goalkeeper_name = goalkeeper_name_entry.get()
        cursor = conn.cursor()
        QUERY = "INSERT INTO Goals (Player_ID, AssistingPlayerName, Scorer_Name, GoalKeeper_Name) VALUES (%s, %s, %s, %s);"
        DATA = (player_id, assisting_player, scorer_name, goalkeeper_name)
        cursor.execute(QUERY, DATA)
        conn.commit()
        MessageBox.showinfo("OK", "Data Successfully Inserted")
    except:
        MessageBox.showerror("OPS", "Something went wrong. Please check the data")
    finally:
        conn.close()

def func_SelectGoalData():
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
            QUERY = "SELECT * FROM Goals WHERE Player_ID=%s;"
            cursor.execute(QUERY, (player_id,))
            rows = cursor.fetchall()
            goals_listbox.delete(0, END)
            if rows:
                for row in rows:
                    goals_listbox.insert(END, row)
                MessageBox.showinfo("Success", "Data Found")
            else:
                MessageBox.showinfo("Info", "Data not found")
    except:
        MessageBox.showinfo("Alert", "Something went wrong.")
    finally:
        conn.close()

def func_UpdateGoalData():
    conn = psycopg2.connect(
        host="127.0.0.1",
        database='Project-Test',
        user='postgres',
        password='123qw123'
    )
    try:
        player_id = int(player_id_update.get())
        assisting_player = assisting_player_update.get()
        scorer_name = scorer_name_update.get()
        goalkeeper_name = goalkeeper_name_update.get()
        if player_id == "":
            MessageBox.showerror("Error", "Please enter a Player ID to be updated")
        else:
            cursor = conn.cursor()
            QUERY = "UPDATE Goals SET AssistingPlayerName=%s, Scorer_Name=%s, GoalKeeper_Name=%s WHERE Player_ID=%s;"
            DATA = (assisting_player, scorer_name, goalkeeper_name, player_id)
            cursor.execute(QUERY, DATA)
            conn.commit()
            MessageBox.showinfo("Success", "Data was updated")
    except:
        MessageBox.showinfo("Alert", "Something went wrong.")
    finally:
        conn.close()

def func_DeleteGoalData():
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
            QUERY = "DELETE FROM Goals WHERE Player_ID=%s;"
            DATA = (player_id,)
            cursor.execute(QUERY, DATA)
            conn.commit()
            MessageBox.showinfo("Success", "Data was deleted")
    except:
        MessageBox.showinfo("Alert", "Something went wrong.")
    finally:
        conn.close()

# Create an Entry widget to accept User Input for Goals
Create_l = Label(tabgoals, text="Insert Into Goals")
Create_l.grid(row=0, column=1, pady=30, padx=30)

L1 = Label(tabgoals, text="Player ID")
L1.grid(row=1, column=0)
player_id_entry = Entry(tabgoals, bd=5)
player_id_entry.focus_set()
player_id_entry.grid(row=1, column=1)

L2 = Label(tabgoals, text="Assisting Player Name")
L2.grid(row=2, column=0)
assisting_player_entry = Entry(tabgoals, bd=5)
assisting_player_entry.focus_set()
assisting_player_entry.grid(row=2, column=1)

L3 = Label(tabgoals, text="Scorer Name")
L3.grid(row=3, column=0)
scorer_name_entry = Entry(tabgoals, bd=5)
scorer_name_entry.focus_set()
scorer_name_entry.grid(row=3, column=1)

L4 = Label(tabgoals, text="Goalkeeper Name")
L4.grid(row=4, column=0)
goalkeeper_name_entry = Entry(tabgoals, bd=5)
goalkeeper_name_entry.focus_set()
goalkeeper_name_entry.grid(row=4, column=1)

Button(tabgoals, text="INSERT", width=20, command=lambda: func_InsertGoalData()).grid(row=5, column=1)

# Create widgets for the Select, Update, and Delete sections
Select_l = Label(tabgoals, text="Select a Goal")
Select_l.grid(row=0, column=2, pady=30, padx=30)

L5 = Label(tabgoals, text="Player ID")
L5.grid(row=1, column=2)
player_id_select = Entry(tabgoals, bd=5)
player_id_select.focus_set()
player_id_select.grid(row=1, column=2)

Button(tabgoals, text="SELECT", width=20, command=lambda: func_SelectGoalData()).grid(row=2, column=2)

Update_l = Label(tabgoals, text="Update a Goal")
Update_l.grid(row=3, column=2, pady=30, padx=30)

L6 = Label(tabgoals, text="Player ID")
L6.grid(row=4, column=2)
player_id_update = Entry(tabgoals, bd=5)
player_id_update.focus_set()
player_id_update.grid(row=4, column=2)

L7 = Label(tabgoals, text="Assisting Player Name")
L7.grid(row=5, column=2)
assisting_player_update = Entry(tabgoals, bd=5)
assisting_player_update.focus_set()
assisting_player_update.grid(row=5, column=2)

L8 = Label(tabgoals, text="Scorer Name")
L8.grid(row=6, column=2)
scorer_name_update = Entry(tabgoals, bd=5)
scorer_name_update.focus_set()
scorer_name_update.grid(row=6, column=2)

L9 = Label(tabgoals, text="Goalkeeper Name")
L9.grid(row=7, column=2)
goalkeeper_name_update = Entry(tabgoals, bd=5)
goalkeeper_name_update.focus_set()
goalkeeper_name_update.grid(row=7, column=2)

Button(tabgoals, text="UPDATE", width=20, command=lambda: func_UpdateGoalData()).grid(row=8, column=2)

Delete_l = Label(tabgoals, text="Delete a Goal")
Delete_l.grid(row=9, column=2, pady=30, padx=30)

L10 = Label(tabgoals, text="Player ID")
L10.grid(row=10, column=2)
player_id_delete = Entry(tabgoals, bd=5)
player_id_delete.focus_set()
player_id_delete.grid(row=10, column=2)

Button(tabgoals, text="DELETE", width=20, command=lambda: func_DeleteGoalData()).grid(row=11, column=2)

# Create a Listbox to display selected goal data
goals_listbox = Listbox(tabgoals, height=6, width=75)
goals_listbox.grid(row=12, column=2, rowspan=6, columnspan=2)

root.mainloop()