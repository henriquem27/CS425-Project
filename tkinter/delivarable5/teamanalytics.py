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


    Label(tabhome,text="Analitical Query's",font=('Times New Roman',20)).pack()
    Label(tabhome,text="This page allows the user to explore the database.",font=('Times New Roman',15)).pack()


    Label(tabhome,text='Select the Team(s) and Click a button to display the query:').pack(anchor='w')
    
    Season = Entry(tabhome)

    def clicked():
        print("clicked")
        selected = box.curselection()  # returns a tuple
        for idx in selected:
            print(box.get(idx))


    def get_teams():
        conn = get_conn()
        cursor = conn.cursor()
        cursor.execute("SELECT DISTINCT Team from Teams ORDER BY Team;")
        records= cursor.fetchall()
        return records
    

    box = Listbox(tabhome, selectmode=MULTIPLE, height=10)

    values = get_teams()

    for val in values:
        box.insert(END, val)
    box.pack(anchor='w')

    def points_rollup():
        conn = get_conn()

        try:
            top_window = Toplevel(root)
            top_window.title('Points by Season')
            top_window.geometry('400x400')
            popCanv = Canvas(top_window, width=600, height=300,
            scrollregion=(0, 0, 2000, 2000))  # width=1256, height = 1674)
            frame = Frame(popCanv)
            ksbar = Scrollbar(top_window, orient=VERTICAL,
                              command=popCanv.yview)
            popCanv.configure(yscrollcommand=ksbar.set)
            cursor = conn.cursor()
            selected = box.curselection()
            teamnames = ()
            for idx in selected:
                teamnames += (box.get(idx),)

            QUERY = "SELECT Team,Season_ID,SUM(points) FROM teams WHERE team IN %s GROUP BY ROLLUP(Team,Season_ID) ORDER BY Team,Season_ID;"
            cursor.execute(QUERY, (teamnames,))
            records = cursor.fetchall()
            Label(frame,text="Team").grid(row=0,column=0)
            Label(frame,text="Season").grid(row=0, column=1)
            Label(frame,text="Points").grid(row=0,column=2)
            for x in range(len(records)):
                Label(frame, text=records[x][0]).grid(row=x+1, column=0)
                Label(frame, text=records[x][1]).grid(row=x+1, column=1)
                Label(frame, text=records[x][2]).grid(row=x+1, column=2)
                ttk.Separator(frame, orient='horizontal').grid(
                    row=x+1, column=0, columnspan=5, ipadx=100, sticky='s')

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

    Label(tabhome,text='Shows total Points by Season and the total:').pack(anchor='w')
    Button(tabhome, text="Total Points by Season", width=20,
        command=lambda: points_rollup()).pack(anchor='w')
    
    def team_budgets2():
        conn = get_conn()

        try:
            top_window = Toplevel(root)
            top_window.title('Team Budgets')
            top_window.geometry('520x400')
            tree_frame = Frame(top_window)
            tree_frame.pack(fill='both',expand=1,pady=20)
            tree_scroll = Scrollbar(tree_frame)
            tree_scroll.pack(side=RIGHT, fill=Y)
            my_tree = ttk.Treeview(
                tree_frame, yscrollcommand=tree_scroll.set, selectmode="extended")
            
            my_tree.pack(fill='both',expand=1)

            tree_scroll.config(command=my_tree.yview)
            
            
            my_tree['columns'] = ("Team", "Season", "Total Budget", "Running Total")
            my_tree.column("#0", width=0, stretch=NO)
            my_tree.column("Team", anchor=CENTER, width=50)
            my_tree.column("Season", anchor=CENTER, width=60)
            my_tree.column("Total Budget", anchor=CENTER, width=140)
            my_tree.column("Running Total", anchor=CENTER, width=140)
            

            # Create Headings 
            my_tree.heading("#0", text="", anchor=W)
            my_tree.heading("Team", text="Team", anchor=CENTER)
            my_tree.heading("Season", text="Season", anchor=CENTER)
            my_tree.heading("Total Budget", text="Team Budget", anchor=CENTER)
            my_tree.heading("Running Total", text="Running Total", anchor=CENTER)

            my_tree.tag_configure('oddrow', background="#084370")
            my_tree.tag_configure('evenrow')

            cursor = conn.cursor()
            selected = box.curselection()
            teamnames = ()
            for idx in selected:
                teamnames += (box.get(idx),)

            QUERY = "SELECT Team,Season_ID,team_budget, SUM(TEAM_BUDGET.Team_Budget) OVER (PARTITION BY team order by season_id ROWS UNBOUNDED PRECEDING) FROM team_budget WHERE team IN %s ORDER BY Team,Season_ID;"
            cursor.execute(QUERY, (teamnames,))
            records = cursor.fetchall()
            x=0

            for x in range(len(records)):
                if x % 2 == 0:
                    my_tree.insert(parent='', index='end', iid=x, text="", values=(
                        records[x][0], records[x][1], records[x][2], records[x][3]), tags=('evenrow',))
                else:
                    my_tree.insert(parent='', index='end', iid=x, text="", values=(
                        records[x][0], records[x][1], records[x][2], records[x][3]), tags=('oddrow',))

        except Exception:
            traceback.print_exc()
            MessageBox.showerror(
                "OPS", " something went wrong. Please make sure you have at least one team selected")

        finally:
            conn.close()

    Label(tabhome, text='Shows the team budgets by season with a running total:').pack(
        anchor='w')
    Button(tabhome, text="Team Budget2", width=20,
           command=lambda: team_budgets2()).pack(anchor='w')

    def home_away_perf():
        conn = get_conn()

        try:
            top_window = Toplevel(root)
            top_window.title('Team Budgets')
            top_window.geometry('520x400')
            tree_frame = Frame(top_window)
            tree_frame.pack(fill='both', expand=1, pady=20)
            tree_scroll = Scrollbar(tree_frame)
            tree_scroll.pack(side=RIGHT, fill=Y)
            my_tree = ttk.Treeview(
                tree_frame, yscrollcommand=tree_scroll.set, selectmode="extended")

            my_tree.pack(fill='both', expand=1)

            tree_scroll.config(command=my_tree.yview)

            my_tree['columns'] = (
                "Team", "Season", "Average Home Goals", "Average Away Goals","Avg Home-Away Difference")
            my_tree.column("#0", width=0, stretch=NO)
            my_tree.column("Team", anchor=CENTER, width=50)
            my_tree.column("Season", anchor=CENTER, width=60)
            my_tree.column("Average Home Goals", anchor=CENTER, width=140)
            my_tree.column("Average Away Goals", anchor=CENTER, width=140)
            my_tree.column("Avg Home-Away Difference", anchor=CENTER, width=140)

            # Create Headings
            my_tree.heading("#0", text="", anchor=W)
            my_tree.heading("Team", text="Team", anchor=CENTER)
            my_tree.heading("Season", text="Season", anchor=CENTER)
            my_tree.heading("Average Home Goals",
                            text="Average Home Goals", anchor=CENTER)
            my_tree.heading("Average Away Goals",
                            text="Average Away Goals", anchor=CENTER)
            my_tree.heading("Avg Home-Away Difference",
                            text="Average Home-Away Goal Differential", anchor=CENTER)

            my_tree.tag_configure('oddrow', background="#084370")
            my_tree.tag_configure('evenrow')

            cursor = conn.cursor()
            selected = box.curselection()
            teamnames = ()
            for idx in selected:
                teamnames += (box.get(idx),)

            QUERY = "SELECT x.Team,x.Season_ID as Season,x.HomeAVG,y.AwayAvg, X.HomeAVG-y.AwayAvg as AVG_GOAL_DIFFERENTIAl FROM "
            QUERY = QUERY + \
                "(SELECT t.team,ROUND(AVG(g.Homegoals),4) as HomeAVG,t.Season_ID,g.home_team_id FROM teams t,games g WHERE t.team_id=g.home_team_id "
            QUERY = QUERY + \
                " GROUP BY t.team_id,g.home_team_id ORDER BY Team_ID) as x,(SELECT t.team,ROUND(AVG(g.AwayGoals),4) as AwayAvg,g.Season_ID,g.away_team_id FROM teams t,games g WHERE t.team_id=g.away_team_id "
            QUERY = QUERY+" GROUP BY t.team_id,g.away_team_id,g.Season_ID ORDER BY Team_ID) as y WHERE x.Home_Team_ID=y.Away_team_ID AND x.team IN %s;"
            cursor.execute(QUERY, (teamnames,))
            records = cursor.fetchall()
            x = 0

            for x in range(len(records)):
                if x % 2 == 0:
                    my_tree.insert(parent='', index='end', iid=x, text="", values=(
                        records[x][0], records[x][1], records[x][2], records[x][3], records[x][4]), tags=('evenrow',))
                else:
                    my_tree.insert(parent='', index='end', iid=x, text="", values=(
                        records[x][0], records[x][1], records[x][2], records[x][3], records[x][4]), tags=('oddrow',))

        except Exception:
            traceback.print_exc()
            MessageBox.showerror(
                "OPS", " something went wrong. Please make sure you have at least one team selected")

        finally:
            conn.close()

    Label(tabhome, text='Displays the Average Home-Away Performance in terms of goal:').pack(
        anchor='w')
    Button(tabhome, text="Avg Home-Away Performance", width=20,
           command=lambda: home_away_perf()).pack(anchor='w')
    
    def top_scores():
        conn = get_conn()

        try:
            top_window = Toplevel(root)
            top_window.title('Team Budgets')
            top_window.geometry('520x400')
            tree_frame = Frame(top_window)
            tree_frame.pack(fill='both', expand=1, pady=20)
            tree_scroll = Scrollbar(tree_frame)
            tree_scroll.pack(side=RIGHT, fill=Y)
            my_tree = ttk.Treeview(
                tree_frame, yscrollcommand=tree_scroll.set, selectmode="extended")

            my_tree.pack(fill='both', expand=1)

            tree_scroll.config(command=my_tree.yview)

            my_tree['columns'] = (
                "Team", "Season", "Total Budget", "Running Total")
            my_tree.column("#0", width=0, stretch=NO)
            my_tree.column("Team", anchor=CENTER, width=50)
            my_tree.column("Season", anchor=CENTER, width=60)
            my_tree.column("Total Budget", anchor=CENTER, width=140)
            my_tree.column("Running Total", anchor=CENTER, width=140)

            # Create Headings
            my_tree.heading("#0", text="", anchor=W)
            my_tree.heading("Team", text="Team", anchor=CENTER)
            my_tree.heading("Season", text="Season", anchor=CENTER)
            my_tree.heading("Total Budget", text="Team Budget", anchor=CENTER)
            my_tree.heading("Running Total",
                            text="Running Total", anchor=CENTER)

            my_tree.tag_configure('oddrow', background="#084370")
            my_tree.tag_configure('evenrow')

            cursor = conn.cursor()
            selected = box.curselection()
            teamnames = ()
            for idx in selected:
                teamnames += (box.get(idx),)

            QUERY = "SELECT Team,Season_ID,team_budget, SUM(TEAM_BUDGET.Team_Budget) OVER (PARTITION BY team order by season_id ROWS UNBOUNDED PRECEDING) FROM team_budget WHERE team IN %s ORDER BY Team,Season_ID;"
            cursor.execute(QUERY, (teamnames,))
            records = cursor.fetchall()
            x = 0

            for x in range(len(records)):
                if x % 2 == 0:
                    my_tree.insert(parent='', index='end', iid=x, text="", values=(
                        records[x][0], records[x][1], records[x][2], records[x][3]), tags=('evenrow',))
                else:
                    my_tree.insert(parent='', index='end', iid=x, text="", values=(
                        records[x][0], records[x][1], records[x][2], records[x][3]), tags=('oddrow',))

        except Exception:
            traceback.print_exc()
            MessageBox.showerror(
                "OPS", " something went wrong. Please make sure you have at least one team selected")

        finally:
            conn.close()

    Label(tabhome, text='Shows the team budgets by season with a running total:').pack(
        anchor='w')
    Button(tabhome, text="Team Budget2", width=20,
           command=lambda: team_budgets2()).pack(anchor='w')

