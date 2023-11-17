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

    #not used
    def download_sql_query_to_csv(sql_query,seasoninput,file_path):
        try:
            # Establish a connection to the PostgreSQL database
            conn = get_conn()
            db_cursor=conn.cursor()
            # Build the SQL query for file output
            sql_for_file_output = "COPY ({0}) TO STDOUT WITH CSV HEADER".format(sql_query)

            # Open the file for writing
            with open(file_path, 'w') as f_output:
                # Execute the copy_expert method to export data to CSV
                db_cursor.copy_expert(sql_for_file_output, f_output)

            print(f"Query results downloaded to {file_path}")

        except psycopg2.Error as e:
            print("Error: Unable to download query results.")
            print(e)

        finally:
            # Close the cursor and connection
            if conn:
                conn.close()

    Label(tabhome,text="Data Exploration",font=('Times New Roman',20),relief='raised',padx=5,pady=10,bd=5).grid(row=0,column=1,columnspan=2,pady=5)

    Label(tabhome, text="Team Seaction",
          font=('Times New Roman', 15), relief='raised', padx=5, pady=5, bd=5).grid(row=2, column=0,pady=5)
    Label(tabhome, text="Player Section",
          font=('Times New Roman', 15), relief='raised', padx=5, pady=5, bd=5).grid(row=2, column=1,columnspan=2,pady=5)
    Label(tabhome, text="Games Seaction",
          font=('Times New Roman', 15), relief='raised', padx=5, pady=5, bd=5).grid(row=2, column=3, pady=5,padx=10)
    
    

    Label(tabhome, text='Select the Team(s) and Click one of the buttons to display the query:',relief='ridge',padx=5,pady=5,wraplength=200).grid(
        row=3, column=0)
    Label(tabhome, text='Select the a Season and Click one of the buttons to display the query:', relief='ridge', padx=5, pady=5,wraplength=200).grid(
        row=3, column=1)
    Label(tabhome, text='Select the Team(s) and Click one of the buttons to display the query:', relief='ridge', padx=5, pady=5, wraplength=200).grid(
        row=3, column=2)
    
    Label(tabhome, text='Queries related to the Games table: ', relief='ridge', padx=5, pady=5, wraplength=200).grid(
        row=3, column=3,padx=10)

    def clicked():
        print("clicked")
        selected = box.curselection()  # returns a tuple
        for idx in selected:
            print(box.get(idx))

    def call_delete(listBox):
        selection = listBox.curselection()
        for i in reversed(selection):
            listBox.delete(i)

    def get_teams():
        conn = get_conn()
        cursor = conn.cursor()
        cursor.execute("SELECT DISTINCT Team from Teams WHERE Team NOT IN ('CHV') ORDER BY Team;")
        records= cursor.fetchall()
        return records
    
    def get_seasons():
        conn = get_conn()
        cursor = conn.cursor()
        cursor.execute("SELECT DISTINCT Season_ID from Seasons ORDER BY Season_ID;")
        records = cursor.fetchall()
        return records
    

    box = Listbox(tabhome, selectmode=MULTIPLE, height=10,exportselection=0)

    values = get_teams()

    for val in values:
        box.insert(END, val)
    box.grid(row=4, column=0)

    seasonbox = Listbox(tabhome, selectmode=MULTIPLE, height=10,exportselection=0)

    values2 = get_seasons()

    for val in values2:
        seasonbox.insert(END, val)
    seasonbox.grid(row=4, column=1)
    
    teambox = Listbox(tabhome, selectmode=MULTIPLE, height=10,exportselection=0)

    values3 = get_teams()

    for val in values3:
        teambox.insert(END, val)
    teambox.grid(row=4, column=2,padx=5,pady=5)


    #Games
    gamesbox = Listbox(tabhome, selectmode=MULTIPLE,
                        height=10, exportselection=0)

    values4 = get_seasons()

    for val in values4:
        gamesbox.insert(END, val)
    gamesbox.grid(row=4, column=3)



    # Buttons to select all and clear all
    Button(tabhome, text="Select All", command=lambda: teambox.select_set(0, END)).grid(row=5,column=2)
    Button(tabhome, text="Select All", command=lambda: seasonbox.select_set(0, END)).grid(row=5,column=1)
    Button(tabhome, text="Clear All Selections", command=lambda: seasonbox.selection_clear(0,END)).grid(row=6, column=1)
    Button(tabhome, text="Clear All Selections",command=lambda: teambox.selection_clear(0, END)).grid(row=6, column=2)
    Button(tabhome, text="Select All", command=lambda: box.select_set(0, END)).grid(row=5, column=0)
    Button(tabhome, text="Clear All Selections",command=lambda: box.selection_clear(0, END)).grid(row=6, column=0)
    # games
    Button(tabhome, text="Select All", command=lambda: gamesbox.select_set(0, END)).grid(row=5, column=3)
    Button(tabhome, text="Clear All Selections",command=lambda: gamesbox.selection_clear(0, END)).grid(row=6, column=3)

    #OLAP
    
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

    Label(tabhome, text='Shows total Points by Season and the total:', relief='ridge',padx=5,pady=5).grid(
        row=7, column=0)
    Button(tabhome, text="Total Points by Season", width=20,
           command=lambda: points_rollup()).grid(row=8, column=0)
    
    # OLAP
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
    
    Label(tabhome, text='Shows the team budgets by season with a running total:', relief='ridge', padx=5, pady=5).grid(
        row=9, column=0)
    Button(tabhome, text="Team Budget", width=20,
           command=lambda: team_budgets2()).grid(row=10, column=0)

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

    Label(tabhome, text='Displays the Average Home-Away Performance in terms of goals:',
          relief='ridge', padx=2, pady=2, wraplength=200).grid(row=11, column=0)
    Button(tabhome, text="Avg Home-Away Performance", width=20,
           command=lambda: home_away_perf()).grid(row=12, column=0)

    # Olap
    def Budget_with_Subtotals():
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
                "Year", "Team", "$USD")
            my_tree.column("#0", width=0, stretch=NO)
            my_tree.column("Year", anchor=CENTER, width=100)
            my_tree.column("Team", anchor=CENTER, width=100)
            my_tree.column("$USD", anchor=CENTER, width=140)

            # Create Headings
            my_tree.heading("#0", text="", anchor=W)
            my_tree.heading("Year", text="Year", anchor=CENTER)
            my_tree.heading("Team", text="Team", anchor=CENTER)
            my_tree.heading("$USD",text="Budget in $USD", anchor=CENTER)

            my_tree.tag_configure('none', background="#084370")
            my_tree.tag_configure('all')
            my_tree.tag_configure('Total', background="#700808")
            my_tree.tag_configure('year', background="#008000")

            cursor = conn.cursor()
            selected = box.curselection()
            teamnames = ()
            for idx in selected:
                teamnames += (box.get(idx),)
            QUERY = "SELECT se4ason_id,team,SUM(team_budget) As Total_Budget from team_budget where team in %s GROUP BY CUBE(season_id,team) ORDER BY (team,season_id);"
            cursor.execute(QUERY, (teamnames,))
            records = cursor.fetchall()
            x = 0

            for x in range(len(records)):
                if records[x][0] is None and records[x][1] is not None:
                    # Convert the tuple to a list
                    record_list = list(records[x])
                    # Assign a new value to the first element of the list
                    record_list[0] = "Subtotal"
                    # Convert the list back to a tuple
                    records[x] = tuple(record_list)
                    my_tree.insert(parent='', index='end', text="", values=(records[x][0], records[x][1], records[x][2]), tags=('none',))
                
                elif records[x][0] is not None and records[x][1] is None:
                    # Convert the tuple to a list
                    record_list = list(records[x])
                    # Assign a new value to the first element of the list
                    record_list[1] = "Subtotal"
                    # Convert the list back to a tuple
                    records[x] = tuple(record_list)
                    my_tree.insert(parent='', index='end', text="", values=(
                        records[x][0], records[x][1], records[x][2]), tags=('year',))
                elif records[x][1] is None and records[x][0] is None:
                    # Convert the tuple to a list
                    record_list = list(records[x])
                    # Assign a new value to the first element of the list
                    record_list[1] = "Total"
                    record_list[0] = "-----"
                    # Convert the list back to a tuple
                    records[x] = tuple(record_list)
                    my_tree.insert(parent='', index='end', text="",values=(
                        records[x][0], records[x][1], records[x][2]), tags=('Total',))
                
                elif records[x][0] is not None and records[x][1] is not None:
                    my_tree.insert(parent='', index='end', text="", values=(
                        records[x][0], records[x][1], records[x][2]), tags=('all',))

        except Exception:
            traceback.print_exc()
            MessageBox.showerror(
                "OPS", " something went wrong. Please make sure you have at least one team selected")

        finally:
            conn.close()

    Label(tabhome, text='Displays the Team Budgets with Subtotals',
          relief='ridge', padx=5, pady=5).grid(row=13, column=0)
    Button(tabhome, text="Budget with subtotals", width=20,
           command=lambda: Budget_with_Subtotals()).grid(row=14, column=0)
    
    def top_scorers():
        conn = get_conn()

        try:
            top_window = Toplevel(root)
            top_window.title('Top Scorers')
            top_window.geometry('600x600')
            tree_frame = Frame(top_window)
            tree_frame.pack(fill='both',expand=1,pady=20)
            tree_scroll = Scrollbar(tree_frame)
            tree_scroll.pack(side=RIGHT, fill=Y)
            my_tree = ttk.Treeview(
                tree_frame, yscrollcommand=tree_scroll.set, selectmode="extended")
            
            my_tree.pack(fill='both',expand=1)

            tree_scroll.config(command=my_tree.yview)
            
            
            my_tree['columns'] = ("Player-Name","Position","Team", "Season", "Shots On Goal", "Goals")
            my_tree.column("#0", width=0, stretch=NO)
            my_tree.column("Player-Name", anchor=CENTER, width=100)
            my_tree.column("Position", anchor=CENTER, width=60)
            my_tree.column("Team", anchor=CENTER, width=50)
            my_tree.column("Season", anchor=CENTER, width=60)
            my_tree.column("Shots On Goal", anchor=CENTER, width=60)
            my_tree.column("Goals", anchor=CENTER, width=40)
            

            # Create Headings 
            my_tree.heading("#0", text="", anchor=W)
            my_tree.heading("Player-Name", text="Player-Name", anchor=CENTER)
            my_tree.heading("Position", text="Position", anchor=CENTER)

            my_tree.heading("Team", text="Team", anchor=CENTER)
            my_tree.heading("Season", text="Season", anchor=CENTER)
            my_tree.heading("Shots On Goal", text="Shots On Goal", anchor=CENTER)
            my_tree.heading("Goals", text="Goals", anchor=CENTER)

            my_tree.tag_configure('oddrow', background="#084370")
            my_tree.tag_configure('evenrow')

            cursor = conn.cursor()
            selected = teambox.curselection()
            teamnames = ()
            seasonsel =[]
            for idx in selected:
                teamnames += (teambox.get(idx),)
            seasons = seasonbox.curselection()
            
            for idx in seasons:
                seasonsel.append(seasonbox.get(idx))
            
            forseason = tuple(item[0] for item in seasonsel)
            
            QUERY = "SELECT player_name,position,Team,player.Season_ID,ShotsOnGoal,Goals" 
            QUERY=QUERY+" FROM player,Teams WHERE Player.Season_ID IN %s AND minutes>1000 AND player.Team_ID=Teams.Team_ID AND team IN %s AND ShotsOnGoal>1 ORDER BY Goals DESC"
            
            cursor.execute(QUERY, (forseason,teamnames,))
            
            
            
            records = cursor.fetchall()
            x=0

            for x in range(len(records)):
                if x % 2 == 0:
                    my_tree.insert(parent='', index='end', iid=x, text="", values=(
                        records[x][0], records[x][1], records[x][2], records[x][3],records[x][4],records[x][5]), tags=('evenrow',))
                else:
                    my_tree.insert(parent='', index='end', iid=x, text="", values=(
                        records[x][0], records[x][1], records[x][2], records[x][3],records[x][4],records[x][5]), tags=('oddrow',))

        except Exception:
            traceback.print_exc()
            MessageBox.showerror(
                "OPS", " something went wrong. Please make sure you have at least one team selected and One season selected")

        finally:
            conn.close()

    Label(tabhome, text='Shows Top Scorers Based on Season or Team', relief='ridge', padx=5, pady=5).grid(
        row=7, column=1,columnspan=2,pady=5)
    Button(tabhome, text="Top Scorers", width=20,
           command=lambda: top_scorers()).grid(row=8, column=1,columnspan=2)

    def top_salaries():
        conn = get_conn()

        try:
            top_window = Toplevel(root)
            top_window.title('Player Salaries Rank')
            top_window.geometry('600x600')
            tree_frame = Frame(top_window)
            tree_frame.pack(fill='both', expand=1, pady=20)
            tree_scroll = Scrollbar(tree_frame)
            tree_scroll.pack(side=RIGHT, fill=Y)
            my_tree = ttk.Treeview(
                tree_frame, yscrollcommand=tree_scroll.set, selectmode="extended")

            my_tree.pack(fill='both', expand=1)

            tree_scroll.config(command=my_tree.yview)

            my_tree['columns'] = ("Player-Name", "Position",
                                  "Team", "Season", "Guaranteed Compensation", "Rank")
            my_tree.column("#0", width=0, stretch=NO)
            my_tree.column("Player-Name", anchor=CENTER, width=100)
            my_tree.column("Position", anchor=CENTER, width=60)
            my_tree.column("Team", anchor=CENTER, width=50)
            my_tree.column("Season", anchor=CENTER, width=60)
            my_tree.column("Guaranteed Compensation", anchor=CENTER, width=150)
            my_tree.column("Rank", anchor=CENTER, width=40)

            # Create Headings
            my_tree.heading("#0", text="", anchor=W)
            my_tree.heading("Player-Name", text="Player-Name", anchor=CENTER)
            my_tree.heading("Position", text="Position", anchor=CENTER)

            my_tree.heading("Team", text="Team", anchor=CENTER)
            my_tree.heading("Season", text="Season", anchor=CENTER)
            my_tree.heading("Guaranteed Compensation",
                            text="Guaranteed Compensation", anchor=CENTER)
            my_tree.heading("Rank", text="Rank", anchor=CENTER)

            my_tree.tag_configure('oddrow', background="#084370")
            my_tree.tag_configure('evenrow')

            cursor = conn.cursor()

            # grab selectiions
            selected = teambox.curselection()
            teamnames = ()
            seasonsel = []
            for idx in selected:
                teamnames += (teambox.get(idx),)
            
            #grab selections
            
            seasons = seasonbox.curselection()

            for idx in seasons:
                seasonsel.append(seasonbox.get(idx))

            #FORMAT TO POSTGRESQL TUPLE (year1,year2...)
            forseason = tuple(item[0] for item in seasonsel)

            QUERY ="SELECT p.Player_Name,p.Position,t.team,p.Season_ID,CAST(guaranteedcompensation AS money),dense_rank() OVER (ORDER BY s.GuaranteedCompensation DESC) as Dense_Rank  FROM Teams t ,Salaries s ,Player p WHERE s.Season_ID IN %s AND t.team IN %s AND p.Player_ID=S.Player_ID AND p.Team_ID=t.team_id order by Dense_Rank;"

            cursor.execute(QUERY, (forseason, teamnames,))

            records = cursor.fetchall()
            x = 0

            for x in range(len(records)):
                if x % 2 == 0:
                    my_tree.insert(parent='', index='end', iid=x, text="", values=(
                        records[x][0], records[x][1], records[x][2], records[x][3], records[x][4], records[x][5]), tags=('evenrow',))
                else:
                    my_tree.insert(parent='', index='end', iid=x, text="", values=(
                        records[x][0], records[x][1], records[x][2], records[x][3], records[x][4], records[x][5]), tags=('oddrow',))

        except Exception:
            traceback.print_exc()
            MessageBox.showerror(
                "OPS", " something went wrong. Please make sure you have at least one team selected and one Season selected")

        finally:
            conn.close()

    Label(tabhome, text='Shows Top Salaries', relief='ridge', padx=5, pady=5).grid(
        row=9, column=1, columnspan=2, pady=5)
    Button(tabhome, text="Top Salaries", width=20,
           command=lambda: top_salaries()).grid(row=10, column=1, columnspan=2)



    def top_accuracy():
        conn = get_conn()

        try:
            top_window = Toplevel(root)
            top_window.title('Top Accuracy')
            top_window.geometry('600x600')
            tree_frame = Frame(top_window)
            tree_frame.pack(fill='both', expand=1, pady=20)
            tree_scroll = Scrollbar(tree_frame)
            tree_scroll.pack(side=RIGHT, fill=Y)
            my_tree = ttk.Treeview(
                tree_frame, yscrollcommand=tree_scroll.set, selectmode="extended")

            my_tree.pack(fill='both', expand=1)

            tree_scroll.config(command=my_tree.yview)

            my_tree['columns'] = ("Player-Name",
                                  "Team", "Goals", "SoG","gsog")
            my_tree.column("#0", width=0, stretch=NO)
            my_tree.column("Player-Name", anchor=CENTER, width=100)
            my_tree.column("Team", anchor=CENTER, width=60)
            my_tree.column("Goals", anchor=CENTER, width=100)
            my_tree.column("SoG", anchor=CENTER, width=150)
            my_tree.column("gsog", anchor=CENTER, width=100)

            # Create Headings
            my_tree.heading("#0", text="", anchor=W)
            my_tree.heading("Player-Name", text="Player-Name", anchor=CENTER)
            my_tree.heading("Team", text="Team", anchor=CENTER)
            my_tree.heading("Goals", text="Average Goals", anchor=CENTER)
            my_tree.heading("SoG",text="Average Shots on Goal", anchor=CENTER)
            my_tree.heading("gsog", text="Average Ration of Goal/Shots on Goal", anchor=CENTER)

            my_tree.tag_configure('oddrow', background="#084370")
            my_tree.tag_configure('evenrow')

            cursor = conn.cursor()

            # grab selectiions
            selected = teambox.curselection()
            teamnames = ()
            seasonsel = []
            for idx in selected:
                teamnames += (teambox.get(idx),)

            # grab selections

            seasons = seasonbox.curselection()

            for idx in seasons:
                seasonsel.append(seasonbox.get(idx))

            # FORMAT TO POSTGRESQL TUPLE (year1,year2...)
            forseason = tuple(item[0] for item in seasonsel)

            QUERY = "SELECT Player_Name,MAX(team),round(AVG(Goals),2) as AGoals,round(AVG(ShotsOnGoal),2),round(AVG(cast(goals as decimal)/cast(shotsongoal as decimal)),2) AS Ratio_GoalsVSShotsonGoal FROM player JOIN teams on player.team_id = teams.team_id WHERE player.Season_ID in %s AND team in %s AND minutes>1000 AND Shotsongoal>1 AND goals>1  group by Player_Name order by AGoals DESC,Ratio_GoalsVSShotsonGoal DESC"

            cursor.execute(QUERY, (forseason, teamnames,))

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
                "OPS", " something went wrong. Please make sure you have at least one team selected and one season selected")

        finally:
            conn.close()

    
    Label(tabhome, text='Shows Top Accuracy based on a Average over the Seasons of Goals,Shots on Goal and Goals/Shots On Goal', relief='ridge',wraplength=200, padx=5, pady=5).grid(
        row=11, column=1, columnspan=2, pady=5)
    Button(tabhome, text="Top Accuracy", width=20,
           command=lambda: top_accuracy()).grid(row=12, column=1, columnspan=2)
    
    def games_moving_avg():
        conn = get_conn()

        try:
            top_window = Toplevel(root)
            top_window.title('Top Accuracy')
            top_window.geometry('600x600')
            tree_frame = Frame(top_window)
            tree_frame.pack(fill='both', expand=1, pady=20)
            tree_scroll = Scrollbar(tree_frame)
            tree_scroll.pack(side=RIGHT, fill=Y)
            my_tree = ttk.Treeview(
                tree_frame, yscrollcommand=tree_scroll.set, selectmode="extended")

            my_tree.pack(fill='both', expand=1)

            tree_scroll.config(command=my_tree.yview)

            my_tree['columns'] = ("Date",
                                  "Goals", "AVG")
            my_tree.column("#0", width=0, stretch=NO)
            my_tree.column("Date", anchor=CENTER, width=100)
            my_tree.column("Goals", anchor=CENTER, width=60)
            my_tree.column("AVG", anchor=CENTER, width=100)
            

            # Create Headings
            my_tree.heading("#0", text="", anchor=W)
            my_tree.heading("Date", text="Date", anchor=CENTER)
            my_tree.heading("Goals", text="Total Goals", anchor=CENTER)
            my_tree.heading("AVG", text="7-Day Moving Average Total Goals", anchor=CENTER)
    

            my_tree.tag_configure('oddrow', background="#084370")
            my_tree.tag_configure('evenrow')

            cursor = conn.cursor()
            seasons = gamesbox.curselection()
            seasonsel = []
            for idx in seasons:
                seasonsel.append(gamesbox.get(idx))

            # FORMAT TO POSTGRESQL TUPLE (year1,year2...)
            forseason = tuple(item[0] for item in seasonsel)

            QUERY = "SELECT date,homegoals+games.awaygoals as Total_Goals,ROUND(AVG(homegoals+games.awaygoals) OVER (ORDER BY Date ROWS BETWEEN 3 PRECEDING AND 3 FOLLOWING),2) as Moving_AVG_7_Day FROM Games WHERE season_id IN %s ;"
            cursor.execute(QUERY,(forseason,))

            records = cursor.fetchall()
            x = 0

            for x in range(len(records)):
                if x % 2 == 0:
                    my_tree.insert(parent='', index='end', iid=x, text="", values=(
                        records[x][0], records[x][1], records[x][2]), tags=('evenrow',))
                else:
                    my_tree.insert(parent='', index='end', iid=x, text="", values=(
                        records[x][0], records[x][1], records[x][2]), tags=('oddrow',))

        except Exception:
            traceback.print_exc()
            MessageBox.showerror(
                "OPS", " something went wrong. Please make sure you have at least one season selected")

        finally:
            conn.close()


    Label(tabhome, text='7-Day Moving Average for Total Goals', relief='ridge', wraplength=200, padx=5, pady=5).grid(
        row=7, column=3, pady=5)
    Button(tabhome, text="Top Goals MA", width=20,
           command=lambda: games_moving_avg()).grid(row=8, column=3)



