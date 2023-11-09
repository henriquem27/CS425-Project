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


def points_rollup():
    conn = psycopg2.connect(
    host="127.0.0.1",
    database='Project-Test',
    user='postgres',
    password='123qw123'
        )
            
    try:
        top_window = Toplevel(root)
        cursor=conn.cursor()
        selected = box.curselection()
        teamnames=()
        for idx in selected:
            teamnames+=(box.get(idx),)
        print(teamnames)
        QUERY = "SELECT Team,Season_ID,SUM(Points) FROM teams WHERE team IN %s GROUP BY ROLLUP(Team,Season_ID) ORDER BY Team,Season_ID;"
        cursor.execute(QUERY,(teamnames,))
        records= cursor.fetchall()
        for x in range(len(records)):
            Label(top_window, text=records[x][0]).grid(row=x, column=0)
            Label(top_window, text=records[x][1]).grid(row=x, column=2)
            Label(top_window, text=records[x][2]).grid(row=x, column=3)
        
        conn.commit()
        MessageBox.showinfo("OK","Data Sucessfully Inserted")
    

    except Exception:
        traceback.print_exc()
        MessageBox.showerror("OPS"," something went wrong. Please check the data")

    finally:
        conn.close()


def clicked():
    print("clicked")
    selected = box.curselection()  # returns a tuple
    for idx in selected:
        print(box.get(idx))


box = Listbox(tabhome,selectmode=MULTIPLE,height=4)

values=['MIA','CHI','NYC','LAFC','LAG','NSH']

for val in values:
    box.insert(END, val)
box.pack()

Button(tabhome, text="Points Rollup", width=20,
       command=lambda: points_rollup()).pack()






# call function to fill salary tab
generate_salary(tabsalary)


# call function to fill salary tab
generate_season(tabseason)

generate_player(tabplayer)

generate_gk(tabgk)

generate_teams(tabteams)

root.mainloop()
