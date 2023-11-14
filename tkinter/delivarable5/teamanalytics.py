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


    Label(tabhome,text='Please Select the Teams:',font=('Arial',20),padx=5,pady=10).pack()

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
            top_window.title('Games Played')
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
            ttk.Separator(top_window, orient=HORIZONTAL).grid(
                row=0, columnspan=2, sticky='ns')
            ttk.Separator(top_window, orient=HORIZONTAL).grid(
                row=0, columnspan=3, sticky='ns')
            for x in range(len(records)):
                Label(top_window, text=records[x][0]).grid(row=x+1, column=0)
                Label(top_window, text=records[x][1]).grid(row=x+1, column=1)
                Label(top_window, text=records[x][2]).grid(row=x+1, column=2)
                ttk.Separator(top_window, orient=HORIZONTAL).grid(
                    row=x+1, columnspan=2, sticky='ns')
                ttk.Separator(top_window, orient=HORIZONTAL).grid(
                    row=x+1, columnspan=3, sticky='ns')

            conn.commit()

        except Exception:
            traceback.print_exc()
            MessageBox.showerror(
                "OPS", " something went wrong. Please make sure you have at least one team selected")

        finally:
            conn.close()


    Button(tabhome, text="Games Rollup", width=20,
        command=lambda: points_rollup()).pack()
    

    def team_budgets():
        conn = get_conn()

        try:
            top_window = Toplevel(root)
            top_window.title('Team Budgets')
            top_window.geometry('400x400')
            popCanv = Canvas(top_window, width=600, height=300,
                             scrollregion=(0, 0, 10000, 10000))  # width=1256, height = 1674)
            frame = Frame(popCanv)
            ksbar = Scrollbar(top_window, orient=VERTICAL,
                              command=popCanv.yview)
            popCanv.configure(yscrollcommand=ksbar.set)
            cursor = conn.cursor()
            selected = box.curselection()
            teamnames = ()
            for idx in selected:
                teamnames += (box.get(idx),)

            QUERY = "SELECT Team,Season_ID,team_budget, SUM(TEAM_BUDGET.Team_Budget) OVER (PARTITION BY team order by season_id ROWS UNBOUNDED PRECEDING) FROM team_budget WHERE team IN %s ORDER BY Team,Season_ID;"
            cursor.execute(QUERY, (teamnames,))
            records = cursor.fetchall()
            Label(frame,text="Team",background='grey').grid(row=0,column=0,padx=5)
            Label(frame,text="Season",background='grey').grid(row=0, column=1,padx=5)
            Label(frame, text="Budget", background='grey').grid(
                row=0, column=2, padx=5)
            Label(frame, text="Budget Running Total", background='grey').grid(
                row=0, column=3, padx=5)
            ttk.Separator(frame, orient=HORIZONTAL).grid(
                    row=0, columnspan=2, sticky='ns')
            ttk.Separator(frame, orient=HORIZONTAL).grid(
                    row=0, columnspan=3, sticky='ns')
            ttk.Separator(frame, orient=VERTICAL).grid(
                row=0, column=3, columnspan=1, rowspan=2, sticky='e')
            
            for x in range(len(records)):
                Label(frame, text=records[x][0]).grid(
                    row=x+1, column=0, padx=5)
                Label(frame, text=records[x][1]).grid(
                    row=x+1, column=1, padx=5)
                Label(frame, text=records[x][2]).grid(
                    row=x+1, column=2, padx=5)
                Label(frame, text=records[x][3]).grid(
                    row=x+1, column=3, padx=5)
                ttk.Separator(frame, orient=HORIZONTAL).grid(
                    row=x+1, columnspan=2, sticky='ns')
                ttk.Separator(frame, orient=HORIZONTAL).grid(
                    row=x+1, columnspan=3, sticky='ns')
            
            ksbar.pack(side="right", fill="y")
            popCanv.pack(side="left", fill="both", expand=True)
            popCanv.create_window((4, 4), window=frame, anchor="nw")
            conn.commit()

        except Exception:
            traceback.print_exc()
            MessageBox.showerror(
                "OPS", " something went wrong. Please make sure you have at least one team selected")

        finally:
            conn.close()
    
    
    Button(tabhome, text="Team Budget", width=20,
           command=lambda: team_budgets()).pack()

    def Home_Away_avg2():
        conn = get_conn()

        try:
            top_window = Toplevel(root)
            top_window.title('Average Home-Away Performance')
            top_window.geometry('700x400')
            popCanv = Canvas(top_window, width=600, height = 300,
                             scrollregion=(0, 0, 3000, 3000))  # width=1256, height = 1674)
            frame = Frame(popCanv)
            ksbar = Scrollbar(top_window, orient=VERTICAL,
                              command=popCanv.yview)
            popCanv.configure(yscrollcommand = ksbar.set)
            
            
            
            cursor = conn.cursor()
            selected = box.curselection()
            teamnames = ()
            for idx in selected:
                teamnames += (box.get(idx),)

            QUERY = "SELECT x.Team,x.Season_ID as Season,x.HomeAVG,y.AwayAvg, X.HomeAVG-y.AwayAvg as AVG_GOAL_DIFFERENTIAl FROM "
            QUERY=QUERY+"(SELECT t.team,ROUND(AVG(g.Homegoals),4) as HomeAVG,t.Season_ID,g.home_team_id FROM teams t,games g WHERE t.team_id=g.home_team_id "
            QUERY=QUERY+" GROUP BY t.team_id,g.home_team_id ORDER BY Team_ID) as x,(SELECT t.team,ROUND(AVG(g.AwayGoals),4) as AwayAvg,g.Season_ID,g.away_team_id FROM teams t,games g WHERE t.team_id=g.away_team_id "
            QUERY=QUERY+" GROUP BY t.team_id,g.away_team_id,g.Season_ID ORDER BY Team_ID) as y WHERE x.Home_Team_ID=y.Away_team_ID AND x.team IN %s;"
            cursor.execute(QUERY, (teamnames,))
            records = cursor.fetchall()
            Label(frame, text="Team", background='grey').grid(
                row=0, column=0, padx=5)
            Label(frame, text="Season", background='grey').grid(
                row=0, column=1, padx=5)
            Label(frame, text="Average Home Goals", background='grey').grid(
                row=0, column=2, padx=5)
            Label(frame, text="Average Away Goals", background='grey').grid(
                row=0, column=3, padx=5)
            Label(frame, text="Average Home-Away Goal Differrential", background='grey').grid(
                row=0, column=4, padx=5)
            
            
            for x in range(len(records)):
                Label(frame, text=records[x][0]).grid(
                    row=x+1, column=0, padx=5)
                Label(frame, text=records[x][1]).grid(
                    row=x+1, column=1, padx=5)
                Label(frame, text=records[x][2]).grid(
                    row=x+1, column=2, padx=5)
                Label(frame, text=records[x][3]).grid(
                    row=x+1, column=3, padx=5)
                Label(frame, text=records[x][4]).grid(
                    row=x+1, column=4, padx=5)
                
            ksbar.pack(side="right", fill="y")
            popCanv.pack(side="left", fill="both", expand=True)
            popCanv.create_window((4,4), window=frame, anchor="nw")  
            conn.commit()

        except Exception:
            traceback.print_exc()
            MessageBox.showerror(
                "OPS", " something went wrong. Please make sure you have at least one team selected")

        finally:
            conn.close()


    Button(tabhome, text="Home-Away-Performance", width=20,
           command=lambda: Home_Away_avg2()).pack()
    
    



