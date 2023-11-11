from salaries import *
from season import *
from player import *
from tkinter import *
from teams import *
from gk import *
from connection import *
import psycopg2
import datetime
from tkinter import ttk
import tkinter.messagebox as MessageBox
import traceback


def generate_teamsanalytics(tabhome,root):




    def clicked():
        print("clicked")
        selected = box.curselection()  # returns a tuple
        for idx in selected:
            print(box.get(idx))


    def get_teams():
        conn = get_conn()
        cursor = conn.cursor()
        cursor.execute("SELECT DISTINCT Team from Teams;")
        records= cursor.fetchall()
        return records
    

    box = Listbox(tabhome, selectmode=MULTIPLE, height=10)

    values = get_teams()

    for val in values:
        box.insert(END, val)
    box.pack()

    def points_rollup():
        conn = get_conn()

        try:
            top_window = Toplevel(root)
            top_window.title('Total Games Rollup')
            top_window.geometry('400x400')
            cursor = conn.cursor()
            selected = box.curselection()
            teamnames = ()
            for idx in selected:
                teamnames += (box.get(idx),)

            QUERY = "SELECT Team,Season_ID,SUM(gamesplayed) FROM teams WHERE team IN %s GROUP BY ROLLUP(Team,Season_ID) ORDER BY Team,Season_ID;"
            cursor.execute(QUERY, (teamnames,))
            records = cursor.fetchall()
            Label(top_window,text="Team").grid(row=0,column=0)
            Label(top_window,text="Season").grid(row=0, column=1)
            Label(top_window,text="Games Played").grid(row=0,column=2)
            for x in range(len(records)):
                Label(top_window, text=records[x][0]).grid(row=x+1, column=0)
                Label(top_window, text=records[x][1]).grid(row=x+1, column=1)
                Label(top_window, text=records[x][2]).grid(row=x+1, column=2)

            conn.commit()

        except Exception:
            traceback.print_exc()
            MessageBox.showerror(
                "OPS", " something went wrong. Please check the data")

        finally:
            conn.close()


    Button(tabhome, text="Games Rollup", width=20,
        command=lambda: points_rollup()).pack()
