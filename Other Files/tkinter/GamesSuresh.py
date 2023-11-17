def func_InsertGameData():
    conn = psycopg2.connect(
        host="127.0.0.1",
        database='Project-Test',
        user='postgres',
        password='123qw123'
    )
    try:
        game_date = date_entry.get()
        team_id = int(team_id_entry.get())
        home_team = hometeam_entry.get()
        home_goals = int(home_goals_entry.get())
        away_team = away_entry.get()
        away_goals = int(away_goals_entry.get())
        cursor = conn.cursor()
        QUERY = "INSERT INTO Games (date, Team_ID, Hometeam, HomeGoals, Away, AwayGoals) VALUES (%s, %s, %s, %s, %s, %s);"
        DATA = (game_date, team_id, home_team, home_goals, away_team, away_goals)
        cursor.execute(QUERY, DATA)
        conn.commit()
        MessageBox.showinfo("OK", "Data Successfully Inserted")
    except:
        MessageBox.showerror("OPS", "Something went wrong. Please check the data")
    finally:
        conn.close()

def func_SelectGameData():
    conn = psycopg2.connect(
        host="127.0.0.1",
        database='Project-Test',
        user='postgres',
        password='123qw123'
    )
    try:
        team_id = int(team_id_select.get())
        if team_id == "":
            MessageBox.showerror("Error", "Please enter a Team ID to be selected")
        else:
            cursor = conn.cursor()
            QUERY = "SELECT * FROM Games WHERE Team_ID=%s;"
            cursor.execute(QUERY, (team_id,))
            rows = cursor.fetchall()
            games_listbox.delete(0, END)
            if rows:
                for row in rows:
                    games_listbox.insert(END, row)
                MessageBox.showinfo("Success", "Data Found")
            else:
                MessageBox.showinfo("Info", "Data not found")
    except:
        MessageBox.showinfo("Alert", "Something went wrong.")
    finally:
        conn.close()

def func_UpdateGameData():
    conn = psycopg2.connect(
        host="127.0.0.1",
        database='Project-Test',
        user='postgres',
        password='123qw123'
    )
    try:
        team_id = int(team_id_update.get())
        home_goals = int(home_goals_update.get())
        away_goals = int(away_goals_update.get())
        if team_id == "":
            MessageBox.showerror("Error", "Please enter a Team ID to be updated")
        else:
            cursor = conn.cursor()
            QUERY = "UPDATE Games SET HomeGoals=%s, AwayGoals=%s WHERE Team_ID=%s;"
            DATA = (home_goals, away_goals, team_id)
            cursor.execute(QUERY, DATA)
            conn.commit()
            MessageBox.showinfo("Success", "Data was updated")
    except:
        MessageBox.showinfo("Alert", "Something went wrong.")
    finally:
        conn.close()

def func_DeleteGameData():
    conn = psycopg2.connect(
        host="127.0.0.1",
        database='Project-Test',
        user='postgres',
        password='123qw123'
    )
    try:
        team_id = int(team_id_delete.get())
        if team_id == "":
            MessageBox.showerror("Error", "Please enter a Team ID to be deleted")
        else:
            cursor = conn.cursor()
            QUERY = "DELETE FROM Games WHERE Team_ID=%s;"
            DATA = (team_id,)
            cursor.execute(QUERY, DATA)
            conn.commit()
            MessageBox.showinfo("Success", "Data was deleted")
    except:
        MessageBox.showinfo("Alert", "Something went wrong.")
    finally:
        conn.close()

# Create an Entry widget to accept User Input for Games
Create_l = Label(tabgames, text="Insert Into Games")
Create_l.grid(row=0, column=1, pady=30, padx=30)

L1 = Label(tabgames, text="Date (YYYY-MM-DD)")
L1.grid(row=1, column=0)
date_entry = Entry(tabgames, bd=5)
date_entry.focus_set()
date_entry.grid(row=1, column=1)

L2 = Label(tabgames, text="Team_ID")
L2.grid(row=2, column=0)
team_id_entry = Entry(tabgames, bd=5)
team_id_entry.focus_set()
team_id_entry.grid(row=2, column=1)

L3 = Label(tabgames, text="Home Team")
L3.grid(row=3, column=0)
hometeam_entry = Entry(tabgames, bd=5)
hometeam_entry.focus_set()
hometeam_entry.grid(row=3, column=1)

L4 = Label(tabgames, text="Home Goals")
L4.grid(row=4, column=0)
home_goals_entry = Entry(tabgames, bd=5)
home_goals_entry.focus_set()
home_goals_entry.grid(row=4, column=1)

L5 = Label(tabgames, text="Away Team")
L5.grid(row=5, column=0)
away_entry = Entry(tabgames, bd=5)
away_entry.focus_set()
away_entry.grid(row=5, column=1)

L6 = Label(tabgames, text="Away Goals")
L6.grid(row=6, column=0)
away_goals_entry = Entry(tabgames, bd=5)
away_goals_entry.focus_set()
away_goals_entry.grid(row=6, column=1)

Button(tabgames, text="INSERT", width=20, command=lambda: func_InsertGameData()).grid(row=7, column=1)

# Create widgets for the Select, Update, and Delete sections
Select_l = Label(tabgames, text="Select a Game")
Select_l.grid(row=0, column=2, pady=30, padx=30)

L7 = Label(tabgames, text="Team_ID")
L7.grid(row=1, column=2)
team_id_select = Entry(tabgames, bd=5)
team_id_select.focus_set()
team_id_select.grid(row=1, column=2)

Button(tabgames, text="SELECT", width=20, command=lambda: func_SelectGameData()).grid(row=2, column=2)

Update_l = Label(tabgames, text="Update a Game")
Update_l.grid(row=3, column=2, pady=30, padx=30)

L8 = Label(tabgames, text="Team_ID")
L8.grid(row=4, column=2)
team_id_update = Entry(tabgames, bd=5)
team_id_update.focus_set()
team_id_update.grid(row=4, column=2)

L9 = Label(tabgames, text="Home Goals")
L9.grid(row=5, column=2)
home_goals_update = Entry(tabgames, bd=5)
home_goals_update.focus_set()
home_goals_update.grid(row=5, column=2)

L10 = Label(tabgames, text="Away Goals")
L10.grid(row=6, column=2)
away_goals_update = Entry(tabgames, bd=5)
away_goals_update.focus_set()
away_goals_update.grid(row=6, column=2)

Button(tabgames, text="UPDATE", width=20, command=lambda: func_UpdateGameData()).grid(row=7, column=2)

Delete_l = Label(tabgames, text="Delete a Game")
Delete_l.grid(row=8, column=2, pady=30, padx=30)

L11 = Label(tabgames, text="Team_ID")
L11.grid(row=9, column=2)
team_id_delete = Entry(tabgames, bd=5)
team_id_delete.focus_set()
team_id_delete.grid(row=9, column=2)

Button(tabgames, text="DELETE", width=20, command=lambda: func_DeleteGameData()).grid(row=10, column=2)

# Create a Listbox to display selected game data
games_listbox = Listbox(tabgames, height=6, width=75)
games_listbox.grid(row=11, column=2, rowspan=6, columnspan=2)

root.mainloop()