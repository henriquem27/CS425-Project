def func_InsertTeamData():
    conn = psycopg2.connect(
        host="127.0.0.1",
        database='Project-Test',
        user='postgres',
        password='123qw123'
    )
    try:
        player_id = int(player_id_entry.get())
        games = int(games_entry.get())
        shots_for = int(shots_for_entry.get())
        shots_against = int(shots_against_entry.get())
        goals_for = int(goals_for_entry.get())
        goals_against = int(goals_against_entry.get())
        cursor = conn.cursor()
        QUERY = "INSERT INTO Teams (Player_Id, Games, ShotsFor, ShotsAgainst, GoalsFor, GoalsAgainst) VALUES (%s, %s, %s, %s, %s, %s);"
        DATA = (player_id, games, shots_for, shots_against, goals_for, goals_against)
        cursor.execute(QUERY, DATA)
        conn.commit()
        MessageBox.showinfo("OK", "Data Successfully Inserted")
    except:
        MessageBox.showerror("OPS", "Something went wrong. Please check the data")
    finally:
        conn.close()

def func_SelectTeamData():
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
            QUERY = "SELECT * FROM Teams WHERE Player_Id=%s;"
            cursor.execute(QUERY, (player_id,))
            row = cursor.fetchone()
            if row is not None:
                player_id_label.config(text="Player ID: " + str(row[0]))
                games_label.config(text="Games: " + str(row[1]))
                shots_for_label.config(text="Shots For: " + str(row[2]))
                shots_against_label.config(text="Shots Against: " + str(row[3]))
                goals_for_label.config(text="Goals For: " + str(row[4]))
                goals_against_label.config(text="Goals Against: " + str(row[5]))
                MessageBox.showinfo("Success", "Data Found")
            else:
                MessageBox.showinfo("Info", "Data not found")

    except:
        MessageBox.showinfo("Alert", "Something went wrong.")
    finally:
        conn.close()

def func_UpdateTeamData():
    conn = psycopg2.connect(
        host="127.0.0.1",
        database='Project-Test',
        user='postgres',
        password='123qw123'
    )
    try:
        player_id = int(player_id_update.get())
        games = int(games_update.get())
        shots_for = int(shots_for_update.get())
        shots_against = int(shots_against_update.get())
        goals_for = int(goals_for_update.get())
        goals_against = int(goals_against_update.get())
        if player_id == "":
            MessageBox.showerror("Error", "Please enter a Player ID to be updated")
        else:
            cursor = conn.cursor()
            QUERY = "UPDATE Teams SET Games=%s, ShotsFor=%s, ShotsAgainst=%s, GoalsFor=%s, GoalsAgainst=%s WHERE Player_Id=%s;"
            DATA = (games, shots_for, shots_against, goals_for, goals_against, player_id)
            cursor.execute(QUERY, DATA)
            conn.commit()
            MessageBox.showinfo("Success", "Data was updated")

    except:
        MessageBox.showinfo("Alert", "Something went wrong.")
    finally:
        conn.close()

def func_DeleteTeamData():
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
            QUERY = "DELETE FROM Teams WHERE Player_Id=%s;"
            DATA = (player_id,)
            cursor.execute(QUERY, DATA)
            conn.commit()
            MessageBox.showinfo("Success", "Data was deleted")

    except:
        MessageBox.showinfo("Alert", "Something went wrong.")
    finally:
        conn.close()

# Create an Entry widget to accept User Input for Teams
Create_l = Label(tabteams, text="Insert Into Teams")
Create_l.grid(row=0, column=1, pady=30, padx=30)

L1 = Label(tabteams, text="Player_ID")
L1.grid(row=1, column=0)
player_id_entry = Entry(tabteams, bd=5)
player_id_entry.focus_set()
player_id_entry.grid(row=1, column=1)

L2 = Label(tabteams, text="Games")
L2.grid(row=2, column=0)
games_entry = Entry(tabteams, bd=5)
games_entry.focus_set()
games_entry.grid(row=2, column=1)

L3 = Label(tabteams, text="Shots For")
L3.grid(row=3, column=0)
shots_for_entry = Entry(tabteams, bd=5)
shots_for_entry.focus_set()
shots_for_entry.grid(row=3, column=1)

L4 = Label(tabteams, text="Shots Against")
L4.grid(row=4, column=0)
shots_against_entry = Entry(tabteams, bd=5)
shots_against_entry.focus_set()
shots_against_entry.grid(row=4, column=1)

L5 = Label(tabteams, text="Goals For")
L5.grid(row=5, column=0)
goals_for_entry = Entry(tabteams, bd=5)
goals_for_entry.focus_set()
goals_for_entry.grid(row=5, column=1)

L6 = Label(tabteams, text="Goals Against")
L6.grid(row=6, column=0)
goals_against_entry = Entry(tabteams, bd=5)
goals_against_entry.focus_set()
goals_against_entry.grid(row=6, column=1)

Button(tabteams, text="INSERT", width=20, command=lambda: func_InsertTeamData()).grid(row=7, column=1)

# Create widgets for the Select, Update, and Delete sections
Select_l = Label(tabteams, text="Select a Team")
Select_l.grid(row=0, column=2, pady=30, padx=30)

L7 = Label(tabteams, text="Player_ID")
L7.grid(row=1, column=2)
player_id_select = Entry(tabteams, bd=5)
player_id_select.focus_set()
player_id_select.grid(row=1, column=2)
Button(tabteams, text="SELECT", width=20, command=lambda: func_SelectTeamData()).grid(row=2, column=2)

Update_l = Label(tabteams, text="Update a Team")
Update_l.grid(row=3, column=2, pady=30, padx=30)

L8 = Label(tabteams, text="Player_ID")
L8.grid(row=4, column=2)
player_id_update = Entry(tabteams, bd=5)
player_id_update.focus_set()
player_id_update.grid(row=4, column=2)

L9 = Label(tabteams, text="Games")
L9.grid(row=5, column=2)
games_update = Entry(tabteams, bd=5)
games_update.focus_set()
games_update.grid(row=5, column=2)

L10 = Label(tabteams, text="Shots For")
L10.grid(row=6, column=2)
shots_for_update = Entry(tabteams, bd=5)
shots_for_update.focus_set()
shots_for_update.grid(row=6, column=2)

L11 = Label(tabteams, text="Shots Against")
L11.grid(row=7, column=2)
shots_against_update = Entry(tabteams, bd=5)
shots_against_update.focus_set()
shots_against_update.grid(row=7, column=2)

L12 = Label(tabteams, text="Goals For")
L12.grid(row=8, column=2)
goals_for_update = Entry(tabteams, bd=5)
goals_for_update.focus_set()
goals_for_update.grid(row=8, column=2)

L13 = Label(tabteams, text="Goals Against")
L13.grid(row=9, column=2)
goals_against_update = Entry(tabteams, bd=5)
goals_against_update.focus_set()
goals_against_update.grid(row=9, column=2)

Button(tabteams, text="UPDATE", width=20, command=lambda: func_UpdateTeamData()).grid(row=10, column=2)

Delete_l = Label(tabteams, text="Delete a Team")
Delete_l.grid(row=11, column=2, pady=30, padx=30)

L14 = Label(tabteams, text="Player_ID")
L14.grid(row=12, column=2)
player_id_delete = Entry(tabteams, bd=5)
player_id_delete.focus_set()
player_id_delete.grid(row=12, column=2)

Button(tabteams, text="DELETE", width=20, command=lambda: func_DeleteTeamData()).grid(row=13, column=2)

player_id_label = Label(tabteams, text="")
player_id_label.grid(row=14, column=2)
games_label = Label(tabteams, text="")
games_label.grid(row=15, column=2)
shots_for_label = Label(tabteams, text="")
shots_for_label.grid(row=16, column=2)
shots_against_label = Label(tabteams, text="")
shots_against_label.grid(row=17, column=2)
goals_for_label = Label(tabteams, text="")
goals_for_label.grid(row=18, column=2)
goals_against_label = Label(tabteams, text="")
goals_against_label.grid(row=19, column=2)

root.mainloop()