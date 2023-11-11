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
from teamanalytics import *

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
tabanalytics= ttk.Frame(tabControl)

tabControl.add(tabhome, text='Home')
tabControl.add(tabseason, text='Seasons')
tabControl.add(tabplayer, text='Player')
tabControl.add(tabgk, text='Goalkeepers')
tabControl.add(tabteams, text='Teams')
tabControl.add(tabsalary, text='Salaries')
tabControl.add(tabanalytics, text='Team Analytics')


tabControl.pack(expand=1, fill="both")

Label(tabhome, text="Major League Soccer Database GUI",
      font=('Arial', 30)).pack(padx=30, pady=30)


Label(tabhome, text="This GUI is conncted to a Major league Soccer and Allows for C.R.U.D Operations",
      font=('Arial', 15)).pack(padx=30, pady=30)


Label(tabhome, bg='red', text="this page is still under construction",
      font=('Times New Roman', 15)).pack(padx=30, pady=30)








generate_teamsanalytics(tabanalytics,root)





# call function to fill salary tab
generate_salary(tabsalary)


# call function to fill salary tab
generate_season(tabseason)

generate_player(tabplayer)

generate_gk(tabgk)

generate_teams(tabteams)

root.mainloop()
