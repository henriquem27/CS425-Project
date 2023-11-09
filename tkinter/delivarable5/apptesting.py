from salaries import *
from season import *
from player import *
from tkinter import *
from teams import *
from gk import *
import psycopg2
import datetime
from tkinter import ttk
import tkinter.messagebox as MessageBox
import traceback

root = Tk()
root.title('Major League Soccer Database')

root.geometry("1200x900")
tabControl = ttk.Notebook(root)
tabseason = ttk.Frame(tabControl)
tabplayer = ttk.Frame(tabControl)
tabgk = ttk.Frame(tabControl)
tabgames = ttk.Frame(tabControl)
tabsalary = ttk.Frame(tabControl)
tabpasses = ttk.Frame(tabControl)
tabteams = ttk.Frame(tabControl)
tabhome = ttk.Frame(tabControl)

tabControl.add(tabhome, text='Home')
tabControl.add(tabseason, text='Seasons')
tabControl.add(tabplayer, text='Player')
tabControl.add(tabgk, text='Goalkeepers')
tabControl.add(tabteams, text='Teams')
tabControl.add(tabsalary, text='Salaries')


tabControl.pack(expand=1, fill="both")

Label(tabhome, text="Major League Soccer Database GUI",
      font=('Arial', 30)).pack(padx=30, pady=30)


Label(tabhome, text="This GUI is conncted to a Major league Soccer and Allows for C.R.U.D Operations",
      font=('Arial', 15)).pack(padx=30, pady=30)


Label(tabhome, bg='red', text="this page is still under construction",
      font=('Times New Roman', 15)).pack(padx=30, pady=30)


def team_budgets():
    conn = psycopg2.connect(
    host="127.0.0.1",
    database='Project-Test',
    user='postgres',
    password='123qw123'
        )
            
    try:
        top_window = Toplevel(root)
        cursor=conn.cursor()

        cursor.execute("SELECT Team,Season_ID,SUM(Points) FROM teams WHERE team IN ('ATL','MIA')GROUP BY ROLLUP(Team,Season_ID) ORDER BY Team,Season_ID;")
        conn.commit()
        MessageBox.showinfo("OK","Data Sucessfully Inserted")
    

    except Exception:
        traceback.print_exc()
        MessageBox.showerror("OPS"," something went wrong. Please check the data")

    finally:
        conn.close()


# call function to fill salary tab
generate_salary(tabsalary)


# call function to fill salary tab
generate_season(tabseason)

generate_player(tabplayer)

generate_gk(tabgk)

generate_teams(tabteams)

root.mainloop()
