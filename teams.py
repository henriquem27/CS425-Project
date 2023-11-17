# ------------------------------------------------------Teams--------------------------------------------------------------|

from tkinter import *
import psycopg2
import datetime
from tkinter import ttk
import tkinter.messagebox as MessageBox
import traceback
from connection import *
# Team insert data function

def generate_teams(tabteams):

    def func_InsertTeamData():
        conn = get_conn()
        try:
            team = team_id_entry.get()
            games = int(games_entry.get())
            shots_for = int(shots_for_entry.get())
            shots_against = int(shots_against_entry.get())
            goals_for = int(goals_for_entry.get())
            goals_against = int(goals_against_entry.get())
            season = season_entry_t.get()
            team_id = team+season
            cursor = conn.cursor()
            QUERY = "INSERT INTO Teams (team_id,season_id ,team,gamesplayed, ShotsFor, ShotsAgainst, GoalsFor, GoalsAgainst) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);"
            DATA = (team_id, int(season), team, games, shots_for,
                    shots_against, goals_for, goals_against)
            cursor.execute(QUERY, DATA)
            conn.commit()
            MessageBox.showinfo("OK", "Data Successfully Inserted")
        except Exception:
            traceback.print_exc()
            MessageBox.showerror(
                "OPS", "Something went wrong. Please check the data")
        finally:
            conn.close()
    # Team Select data function


    def func_SelectTeamData():
        conn = get_conn()
        try:
            team_id = team_id_select.get()
            if team_id == "":
                MessageBox.showerror(
                    "Error", "Please enter a Team name to be selected")
            else:
                cursor = conn.cursor()
                QUERY = "SELECT * FROM Teams WHERE team=%s;"
                cursor.execute(QUERY, (team_id,))
                records = cursor.fetchall()
                for label in tabteams.grid_slaves():
                    if int(label.grid_info()["row"]) > 14:
                        label.grid_forget()
                Label(tabteams, text="team_id").grid(row=15, column=0)
                Label(tabteams, text="Season_ID").grid(row=15, column=1)
                Label(tabteams, text="Team").grid(row=15, column=2)
                Label(tabteams, text="Games Played").grid(row=15, column=3)
                Label(tabteams, text="Shots For").grid(row=15, column=4)
                Label(tabteams, text="Shots Faced").grid(row=15, column=5, padx=5)
                Label(tabteams, text="Goals For").grid(row=15, column=6, padx=5)
                Label(tabteams, text="Goals Against").grid(
                    row=15, column=7, padx=5)
                Label(tabteams, text="Points").grid(row=15, column=8, padx=5)
                for x in range(len(records)):
                    Label(tabteams, text=records[x][0]).grid(row=x+16, column=0)
                    Label(tabteams, text=records[x][1]).grid(row=x+16, column=1)
                    Label(tabteams, text=records[x][2]).grid(row=x+16, column=2)
                    Label(tabteams, text=records[x][3]).grid(row=x+16, column=3)
                    Label(tabteams, text=records[x][4]).grid(row=x+16, column=4)
                    Label(tabteams, text=records[x][5]).grid(row=x+16, column=5)
                    Label(tabteams, text=records[x][6]).grid(row=x+16, column=6)
                    Label(tabteams, text=records[x][7]).grid(row=x+16, column=7)
                    Label(tabteams, text=records[x][8]).grid(row=x+16, column=8)
                conn.commit()

        except Exception:
            traceback.print_exc()
            MessageBox.showinfo("Alert", "Something went wrong.")
        finally:
            conn.close()
    # Team Update data function


    def func_UpdateTeamData():
        conn = get_conn()
        try:
            team_id = team_id_update.get()
            games = int(games_update.get())
            shots_for = int(shots_for_update.get())
            shots_against = int(shots_against_update.get())
            goals_for = int(goals_for_update.get())
            goals_against = int(goals_against_update.get())
            points = points_update.get()
            if team_id == "":
                MessageBox.showerror(
                    "Error", "Please enter a Player ID to be updated")
            else:
                cursor = conn.cursor()
                QUERY = "UPDATE Teams SET gamesplayed=%s, ShotsFor=%s, ShotsAgainst=%s, GoalsFor=%s, GoalsAgainst=%s, points=%s WHERE team_id=%s;"
                DATA = (games, shots_for, shots_against,
                        goals_for, goals_against, points, team_id)
                cursor.execute(QUERY, DATA)
                conn.commit()
                MessageBox.showinfo("Success", "Data was updated")

        except Exception:
            traceback.print_exc()
            MessageBox.showinfo("Alert", "Something went wrong.")
        finally:
            conn.close()
    # Team Delete data function


    def func_DeleteTeamData():
        conn = get_conn()
        try:
            team_id = team_id_delete.get()
            if team_id == "":
                MessageBox.showerror(
                    "Error", "Please enter a Team ID to be deleted")
            else:
                cursor = conn.cursor()
                QUERY = "DELETE FROM Teams WHERE team_id=%s;"
                DATA = (team_id,)
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

    L1 = Label(tabteams, text="Team")
    L1.grid(row=1, column=0)
    team_id_entry = Entry(tabteams, bd=5)
    team_id_entry.focus_set()
    team_id_entry.grid(row=1, column=1)

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

    L6 = Label(tabteams, text="Season")
    L6.grid(row=7, column=0)
    season_entry_t = Entry(tabteams, bd=5)
    season_entry_t.focus_set()
    season_entry_t.grid(row=7, column=1)

    Button(tabteams, text="INSERT", width=20,
        command=lambda: func_InsertTeamData()).grid(row=8, column=1)

    # Create widgets for the Select, Update, and Delete sections
    Select_l = Label(tabteams, text="Select a Team")
    Select_l.grid(row=11, column=0, pady=30, padx=30)

    L7 = Label(tabteams, text="Team")
    L7.grid(row=12, column=0)
    team_id_select = Entry(tabteams, bd=5)
    team_id_select.focus_set()
    team_id_select.grid(row=13, column=0)
    Button(tabteams, text="SELECT", width=20,
        command=lambda: func_SelectTeamData()).grid(row=14, column=0)

    Update_l = Label(tabteams, text="Update a Team")
    Update_l.grid(row=0, column=2, pady=30, padx=30)

    L8 = Label(tabteams, text="TEAM_ID")
    L8.grid(row=1, column=2)
    team_id_update = Entry(tabteams, bd=5)
    team_id_update.focus_set()
    team_id_update.grid(row=1, column=3)

    L9 = Label(tabteams, text="Games")
    L9.grid(row=2, column=2)
    games_update = Entry(tabteams, bd=5)
    games_update.focus_set()
    games_update.grid(row=2, column=3)

    L10 = Label(tabteams, text="Shots For")
    L10.grid(row=3, column=2)
    shots_for_update = Entry(tabteams, bd=5)
    shots_for_update.focus_set()
    shots_for_update.grid(row=3, column=3)

    L11 = Label(tabteams, text="Shots Against")
    L11.grid(row=4, column=2)
    shots_against_update = Entry(tabteams, bd=5)
    shots_against_update.focus_set()
    shots_against_update.grid(row=4, column=3)

    L12 = Label(tabteams, text="Goals For")
    L12.grid(row=5, column=2)
    goals_for_update = Entry(tabteams, bd=5)
    goals_for_update.focus_set()
    goals_for_update.grid(row=5, column=3)

    L13 = Label(tabteams, text="Goals Against")
    L13.grid(row=6, column=2)
    goals_against_update = Entry(tabteams, bd=5)
    goals_against_update.focus_set()
    goals_against_update.grid(row=6, column=3)

    L13 = Label(tabteams, text="Points")
    L13.grid(row=7, column=2)
    points_update = Entry(tabteams, bd=5)
    points_update.focus_set()
    points_update.grid(row=7, column=3)

    Button(tabteams, text="UPDATE", width=20,
        command=lambda: func_UpdateTeamData()).grid(row=8, column=3)

    Delete_l = Label(tabteams, text="Delete a Team")
    Delete_l.grid(row=0, column=4, pady=30, padx=30)

    L14 = Label(tabteams, text="Team_ID")
    L14.grid(row=1, column=4)
    team_id_delete = Entry(tabteams, bd=5)
    team_id_delete.focus_set()
    team_id_delete.grid(row=2, column=4)

    Button(tabteams, text="DELETE", width=20,
        command=lambda: func_DeleteTeamData()).grid(row=3, column=4)


    # ------------------------------------------------------Teams--------------------------------------------------------------|


    