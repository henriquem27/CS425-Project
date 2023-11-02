from tkinter import *
import psycopg2
import datetime
from tkinter import ttk
import tkinter.messagebox as MessageBox


root = Tk()
root.title('Major League Soccer Database')

root.geometry("900x900")
tabControl = ttk.Notebook(root)
tabseason = ttk.Frame(tabControl)
tabplayer = ttk.Frame(tabControl)
tabgk = ttk.Frame(tabControl)
tabgames = ttk.Frame(tabControl)
tabsalary = ttk.Frame(tabControl)
tabpasses = ttk.Frame(tabControl)
tabteams = ttk.Frame(tabControl)


tabControl.add(tabseason, text='Seasons')
tabControl.add(tabplayer, text='Player')
tabControl.add(tabgk,text='Goalkeepers')
tabControl.add(tabgames,text='Games')
tabControl.add(tabsalary,text='Salaries')
tabControl.add(tabpasses,text='Passes')
tabControl.add(tabteams,text='teams')


tabControl.pack(expand=1, fill="both")



#player-start------------------------------------------------------------------

def func_InsertPlayerData():
        
    conn = psycopg2.connect(
    host="127.0.0.1",
    database='Project-Test',
    user='postgres',
    password='123qw123'
        )
            
    try:
        playername=Player.get()
        teamp=Team.get()
        seasonp=playerseason.get()
        position1=position.get()
        minutesp=minutes.get()
        shotsp=shots.get()
        shotogp=shotog.get()
        goalsp=goals.get()
        
        team_id=teamp+seasonp
        pid=playername+"-"+seasonp

        cursor = conn.cursor()
        QUERY="INSERT INTO player VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s);"
        DATA=(pid,team_id,int(seasonp),playername,position1,int(minutesp),int(shotsp),int(shotogp),int(goalsp))
        cursor.execute(QUERY,DATA)
            
        
        conn.commit()
        MessageBox.showinfo("OK","Data Sucessfully Inserted")

    except:
        MessageBox.showerror("OPS"," something went wrong. Please check the data")

    finally:
        conn.close()


def func_SelectPlayerData():
    conn = psycopg2.connect(
    host="127.0.0.1",
    database='Project-Test',
    user='postgres',
    password='123qw123'
        )
    
    try:
        pidata=PIDSelect.get()
        if(pidata==""):
                MessageBox.showerror("Error","Please enter an ID to be Selected")

        else:
        
            cursor = conn.cursor()
            DATA=(pidata,)
            QUERY="SELECT * FROM player WHERE player_id=(%s)"
            cursor.execute(QUERY,DATA)
            row=cursor.fetchall()
            Label(tabgk,text="team_id").grid(row=2,column=2)
            LStart = Label(tabgk, text=row[0][1])
            LStart.grid(row=2,column=3)
            Label(tabgk,text="season_id").grid(row=3,column=2)
            LEND = Label(tabgk, text=row[0][2])
            LEND.grid(row=3,column=3)
            
            Label(tabgk,text="Player-Name").grid(row=4,column=2)
            LPname = Label(tabgk, text=row[0][3])
            LPname.grid(row=4,column=3)
            
            Label(tabgk,text="Position").grid(row=5,column=2)
            Label(tabgk, text=row[0][4]).grid(row=5,column=3)

            Label(tabgk,text="Minutes Played").grid(row=6,column=2)
            Label(tabgk, text=row[0][5]).grid(row=6,column=3)

            Label(tabgk,text="Shots").grid(row=7,column=2)
            Label(tabgk, text=row[0][6]).grid(row=7,column=3)


            Label(tabgk,text="Shots on Goal").grid(row=7,column=2)
            Label(tabgk, text=row[0][6]).grid(row=7,column=3)

            Label(tabgk,text="Goals").grid(row=8,column=2)
            Label(tabgk, text=row[0][7]).grid(row=8,column=3)
            
            




            
            conn.commit()

    except:
        MessageBox.showinfo("ALERT", "something went wrong.")
    finally:
        conn.close()


def func_UpdatePlayerData():
    conn = psycopg2.connect(
    host="127.0.0.1",
    database='Project-Test',
    user='postgres',
    password='123qw123'
        )
    
    try:
        Pid1data= Pid1.get()
        Teamdata = Team1.get()
        pseasondata = playerseason1.get()
        namedata = pname1.get()
        posdata = position1.get()
        mindata = minutes1.get()
        sdata = shotog1.get()
        sotdata = shotog1.get()
        gdata = goals1.get()

        team_id=Teamdata+pseasondata


        if(Pid1data==""):
                MessageBox.showerror("Error","Please enter an ID to be Updated")

        else:
            
            cursor = conn.cursor()
            
            DATA=(team_id,int(pseasondata),namedata,posdata,int(mindata),int(sdata),int(sotdata),int(gdata),Pid1data)
            QUERY="UPDATE player SET (team_id,season_id,player_name,position,minutes,shots,shotsongoal,goals)=(%s,%s,%s,%s,%s,%s,%s,%s) WHERE player_id=(%s)"
            cursor.execute(QUERY,DATA)
            MessageBox.showinfo("Sucesss","Data was Updated")




            
            conn.commit()

    except:
        MessageBox.showinfo("ALERT", "something went wrong.")
    finally:
        conn.close()





def func_DeleteSeasonDat():
    conn = psycopg2.connect(
    host="127.0.0.1",
    database='Project-Test',
    user='postgres',
    password='123qw123'
        )
    
    try:
        playerdeletedata=playerdelete.get()

        if(playerdelete==""):
                MessageBox.showerror("Error","Please enter an ID to be Updated")

        else:
            
            cursor = conn.cursor()
            
            DATA=(playerdeletedata,)
            QUERY="DELETE FROM player WHERE player_id=(%s)"
            cursor.execute(QUERY,DATA)
            MessageBox.showinfo("Sucesss","Data was Deleted")

            conn.commit()

    except:
        MessageBox.showinfo("ALERT", "something went wrong.")
    finally:
        conn.close()
    
    



#------------------------------------------------------------------------------------------------Player--------------------------------------------------------------------------------------------------------------------------
#Create an Entry widget to accept User Input for Player
Creat_l= Label(tabgk,text="Insert a New player")
Creat_l.grid(row=0,column=1,pady=30,padx=30)

Label(tabgk, text="Player-Name").grid(row=1,column=0)
Player= Entry(tabgk, bd=5)
Player.focus_set()
Player.grid(row=1,column=1)

Label(tabgk, text="Team").grid(row=2,column=0)
Team= Entry(tabgk, bd=4)
Team.focus_set()
Team.grid(row=2,column=1)


Label(tabgk, text="season").grid(row=3,column=0)
playerseason= Entry(tabgk, bd=4)
playerseason.focus_set()
playerseason.grid(row=3,column=1)

Label(tabgk, text="Position").grid(row=4,column=0)
position= Entry(tabgk, bd=4)
position.focus_set()
position.grid(row=4,column=1)

Label(tabgk, text="Minutes").grid(row=5,column=0)
minutes= Entry(tabgk, bd=4)
minutes.focus_set()
minutes.grid(row=5,column=1)


Label(tabgk, text="Shots").grid(row=6,column=0)
shots= Entry(tabgk, bd=4)
shots.focus_set()
shots.grid(row=6,column=1)


Label(tabgk, text="Shots On Goal").grid(row=7,column=0)
shotog= Entry(tabgk, bd=4)
shotog.focus_set()
shotog.grid(row=7,column=1)


Label(tabgk, text="Goals").grid(row=8,column=0)
goals= Entry(tabgk, bd=4)
goals.focus_set()
goals.grid(row=8,column=1)


Button(tabgk, text= "SUBMIT",width= 20, command=lambda:func_InsertPlayerData()).grid(row=9,column=1)

# Select Widget

Creat_l= Label(tabgk,text="Select a Player")
Creat_l.grid(row=0,column=2,pady=30,padx=30)
#Entry for Select Statement
L4 = Label(tabgk, text="Player_ID")
L4.grid(row=1,column=2)
PIDSelect= Entry(tabgk, bd=5)
PIDSelect.focus_set()
PIDSelect.grid(row=1,column=2)
Label(tabgk,text="DATA").grid(row=1,column=3)


Button(tabgk, text= "Select",width= 20, command=lambda:func_SelectPlayerData()).grid(row=9,column=2)



#Update an Entry widget to accept User Input for Season

Creat_l= Label(tabgk,text="Update Player Stats")
Creat_l.grid(row=10,column=1,pady=30,padx=30)

Label(tabgk, text="Player_ID").grid(row=11,column=0)
Pid1= Entry(tabgk, bd=5)
Pid1.focus_set()
Pid1.grid(row=11,column=1)

Label(tabgk, text="Team").grid(row=12,column=0)
Team1= Entry(tabgk, bd=4)
Team1.focus_set()
Team1.grid(row=12,column=1)


Label(tabgk, text="season").grid(row=13,column=0)
playerseason1= Entry(tabgk, bd=4)
playerseason1.focus_set()
playerseason1.grid(row=13,column=1)

Label(tabgk, text="Position").grid(row=14,column=0)
position1= Entry(tabgk, bd=4)
position1.focus_set()
position1.grid(row=14,column=1)

Label(tabgk, text="Minutes").grid(row=15,column=0)
minutes1= Entry(tabgk, bd=4)
minutes1.focus_set()
minutes1.grid(row=15,column=1)


Label(tabgk, text="Shots").grid(row=16,column=0)
shots1= Entry(tabgk, bd=4)
shots1.focus_set()
shots1.grid(row=16,column=1)


Label(tabgk, text="Shots On Goal").grid(row=17,column=0)
shotog1= Entry(tabgk, bd=4)
shotog1.focus_set()
shotog1.grid(row=17,column=1)


Label(tabgk, text="Goals").grid(row=18,column=0)
goals1= Entry(tabgk, bd=4)
goals1.focus_set()
goals1.grid(row=18,column=1)

Label(tabgk, text="Player-Name").grid(row=19,column=0)
pname1= Entry(tabgk, bd=4)
pname1.focus_set()
pname1.grid(row=19,column=1)


Button(tabgk, text= "SUBMIT",width= 20, command=lambda:func_UpdatePlayerData()).grid(row=20,column=1)



# Delete Widget

Creat_l= Label(tabgk,text="Insert Player_ID to be deleted")
Creat_l.grid(row=10,column=2,pady=30,padx=30)
#Entry for Delete Statement
Label(tabgk, text="Player_ID").grid(row=12,column=2)
playerdelete= Entry(tabgk, bd=5)
playerdelete.focus_set()
playerdelete.grid(row=13,column=2)


Button(tabgk, text= "Delete",width= 20, command=lambda:func_DeleteSeasonDat()).grid(row=14,column=2)


#------------------------------------------------------------------------------------------------Player--------------------------------------------------------------------------------------------------------------------------









































root.mainloop()