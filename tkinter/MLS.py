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


#seasons--------------------------------------------------------------------------------
def func_InsertSeasonData():
        
    conn = psycopg2.connect(
    host="127.0.0.1",
    database='Project-Test',
    user='postgres',
    password='123qw123'
        )
            
    try:
        seasondata=int(season.get())
        
        end = end_date.get()
        year, month, day = map(int, end.split('-'))
        end=datetime.date(year,month,day)
        
        start = start_date.get()
        year, month, day = map(int, start.split('-'))
        start=datetime.date(year,month,day)

        cursor = conn.cursor()
        QUERY="INSERT INTO seasons VALUES (%s,%s,%s);"
        DATA=(int(seasondata),start,end)
        cursor.execute(QUERY,DATA)
            
        
        conn.commit()
        MessageBox.showinfo("OK","Data Sucessfully Inserted")

    except:
        MessageBox.showerror("OPS"," something went wrong. Please check the data")

    finally:
        conn.close()


def func_SelectSeasonData():
    conn = psycopg2.connect(
    host="127.0.0.1",
    database='Project-Test',
    user='postgres',
    password='123qw123'
        )
    
    try:
        seasonselectdata=seasonselect.get()
        if(seasonselectdata==""):
                MessageBox.showerror("Error","Please enter an ID to be Selected")

        else:
        
            cursor = conn.cursor()
            DATA=int(seasonselectdata)
            QUERY="SELECT * FROM seasons WHERE season_id=%s"
            cursor.execute(QUERY,(DATA,))
            row=cursor.fetchall()
            Label(tabseason,text="Start-Date").grid(row=2,column=2)
            LStart = Label(tabseason, text=row[0][1])
            LStart.grid(row=2,column=3)
            Label(tabseason,text="End-Date").grid(row=3,column=2)
            LEND = Label(tabseason, text=row[0][2])
            LEND.grid(row=3,column=3)
            




            
            conn.commit()

    except:
        MessageBox.showinfo("ALERT", "something went wrong.")
    finally:
        conn.close()


def func_UpdateSeasonDat():
    conn = psycopg2.connect(
    host="127.0.0.1",
    database='Project-Test',
    user='postgres',
    password='123qw123'
        )
    
    try:
        seasonupdata=seasonupdate.get()
        startupdatdata=start_date_update.get()
        endupdatedata=end_date_update.get()
        #format
        year, month, day = map(int, startupdatdata.split('-'))
        startupdatdata=datetime.date(year,month,day)
        #format
        year, month, day = map(int, endupdatedata.split('-'))
        endupdatedata=datetime.date(year,month,day)

        if(seasonupdata==""):
                MessageBox.showerror("Error","Please enter an ID to be Updated")

        else:
        
            cursor = conn.cursor()
            
            DATA=(startupdatdata,endupdatedata,int(seasonupdata))
            QUERY="UPDATE seasons SET (start_date,end_date)=(%s,%s) WHERE season_id=(%s)"
            cursor.execute(QUERY,DATA)
            MessageBox.showinfo("Sucesss","Data was Updated")




            
            conn.commit()

    except:
        MessageBox.showinfo("ALERT", "something went wrong.")
    finally:
        conn.close()



    conn = psycopg2.connect(
    host="127.0.0.1",
    database='Project-Test',
    user='postgres',
    password='123qw123'
        )
    
    try:
        seasonselectdata=seasonselect.get()
        if(seasonselectdata==""):
                MessageBox.showerror("Error","Please enter an ID to be Selected")

        else:
        
            cursor = conn.cursor()
            DATA=int(seasonselectdata)
            QUERY="SELECT * FROM seasons WHERE season_id=%s"
            cursor.execute(QUERY,(DATA,))
            row=cursor.fetchall()
            Label(tabseason,text="Start-Date").grid(row=2,column=2)
            LStart = Label(tabseason, text=row[0][1])
            LStart.grid(row=2,column=3)
            Label(tabseason,text="End-Date").grid(row=3,column=2)
            LEND = Label(tabseason, text=row[0][2])
            LEND.grid(row=3,column=3)
            




            
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
        seasondeldata=seasondelete.get()

        if(seasondeldata==""):
                MessageBox.showerror("Error","Please enter an ID to be Updated")

        else:
            
            cursor = conn.cursor()
            
            DATA=(int(seasondeldata),)
            QUERY="DELETE FROM seasons WHERE season_id=(%s)"
            cursor.execute(QUERY,DATA)
            MessageBox.showinfo("Sucesss","Data was Deleted")

            conn.commit()

    except:
        MessageBox.showinfo("ALERT", "something went wrong.")
    finally:
        conn.close()
    
    

# region


#------------------------------------------------------------------------------------------------SEASONS--------------------------------------------------------------------------------------------------------------------------
#Create an Entry widget to accept User Input for Season
Creat_l= Label(tabseason,text="Insert Into Seasons")
Creat_l.grid(row=0,column=1,pady=30,padx=30)

L1 = Label(tabseason, text="Season_ID")
L1.grid(row=1,column=0)
season= Entry(tabseason, bd=5)
season.focus_set()
season.grid(row=1,column=1)



#User input for Start-Date
L2 = Label(tabseason, text="Start_date")
L2.grid(row=2,column=0)
start_date= Entry(tabseason, bd=5)
start_date.focus_set()
start_date.grid(row=2,column=1)


#User input for End-Date
L3 = Label(tabseason, text="End_date")
L3.grid(row=3,column=0)
end_date= Entry(tabseason, bd=5)
end_date.focus_set()
end_date.grid(row=3,column=1)

Button(tabseason, text= "SUBMIT",width= 20, command=lambda:func_InsertSeasonData()).grid(row=4,column=1)

# Select Widget

Creat_l= Label(tabseason,text="Select a Season")
Creat_l.grid(row=0,column=2,pady=30,padx=30)
#Entry for Select Statement
L4 = Label(tabseason, text="Season_ID")
L4.grid(row=1,column=2)
seasonselect= Entry(tabseason, bd=5)
seasonselect.focus_set()
seasonselect.grid(row=1,column=2)
Label(tabseason,text="DATA").grid(row=1,column=3)


Button(tabseason, text= "Select",width= 20, command=lambda:func_SelectSeasonData()).grid(row=4,column=2)



#Update an Entry widget to accept User Input for Season
Update_l= Label(tabseason,text="Update a Season")
Update_l.grid(row=5,column=1,pady=30,padx=30)

Label(tabseason, text="Season_ID").grid(row=6,column=0)
seasonupdate= Entry(tabseason, bd=5)
seasonupdate.focus_set()
seasonupdate.grid(row=6,column=1)



  

#User input for Start-Date
L2 = Label(tabseason, text="Start_date")
L2.grid(row=7,column=0)
start_date_update= Entry(tabseason, bd=5)
start_date_update.focus_set()
start_date_update.grid(row=7,column=1)


#User input for End-Date
L3 = Label(tabseason, text="End_date")
L3.grid(row=8,column=0)
end_date_update= Entry(tabseason, bd=5)
end_date_update.focus_set()
end_date_update.grid(row=8,column=1)

Button(tabseason, text= "SUBMIT",width= 20, command=lambda:func_UpdateSeasonDat()).grid(row=9,column=1)



# Delete Widget

Creat_l= Label(tabseason,text="Select a Season to be deleted")
Creat_l.grid(row=5,column=2,pady=30,padx=30)
#Entry for Delete Statement
L4 = Label(tabseason, text="Season_ID")
L4.grid(row=6,column=2)
seasondelete= Entry(tabseason, bd=5)
seasondelete.focus_set()
seasondelete.grid(row=6,column=2)


Button(tabseason, text= "Delete",width= 20, command=lambda:func_DeleteSeasonDat()).grid(row=9,column=2)


#------------------------------------------------------------------------------------------------SEASONS--------------------------------------------------------------------------------------------------------------------------


# endregion



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
            Label(tabplayer,text="team_id").grid(row=2,column=2)
            LStart = Label(tabplayer, text=row[0][1])
            LStart.grid(row=2,column=3)
            Label(tabplayer,text="season_id").grid(row=3,column=2)
            LEND = Label(tabplayer, text=row[0][2])
            LEND.grid(row=3,column=3)
            
            Label(tabplayer,text="Player-Name").grid(row=4,column=2)
            LPname = Label(tabplayer, text=row[0][3])
            LPname.grid(row=4,column=3)
            
            Label(tabplayer,text="Position").grid(row=5,column=2)
            Label(tabplayer, text=row[0][4]).grid(row=5,column=3)

            Label(tabplayer,text="Minutes Played").grid(row=6,column=2)
            Label(tabplayer, text=row[0][5]).grid(row=6,column=3)

            Label(tabplayer,text="Shots").grid(row=7,column=2)
            Label(tabplayer, text=row[0][6]).grid(row=7,column=3)


            Label(tabplayer,text="Shots on Goal").grid(row=7,column=2)
            Label(tabplayer, text=row[0][6]).grid(row=7,column=3)

            Label(tabplayer,text="Goals").grid(row=8,column=2)
            Label(tabplayer, text=row[0][7]).grid(row=8,column=3)
            
            




            
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
Creat_l= Label(tabplayer,text="Insert a New player")
Creat_l.grid(row=0,column=1,pady=30,padx=30)

Label(tabplayer, text="Player-Name").grid(row=1,column=0)
Player= Entry(tabplayer, bd=5)
Player.focus_set()
Player.grid(row=1,column=1)

Label(tabplayer, text="Team").grid(row=2,column=0)
Team= Entry(tabplayer, bd=4)
Team.focus_set()
Team.grid(row=2,column=1)


Label(tabplayer, text="season").grid(row=3,column=0)
playerseason= Entry(tabplayer, bd=4)
playerseason.focus_set()
playerseason.grid(row=3,column=1)

Label(tabplayer, text="Position").grid(row=4,column=0)
position= Entry(tabplayer, bd=4)
position.focus_set()
position.grid(row=4,column=1)

Label(tabplayer, text="Minutes").grid(row=5,column=0)
minutes= Entry(tabplayer, bd=4)
minutes.focus_set()
minutes.grid(row=5,column=1)


Label(tabplayer, text="Shots").grid(row=6,column=0)
shots= Entry(tabplayer, bd=4)
shots.focus_set()
shots.grid(row=6,column=1)


Label(tabplayer, text="Shots On Goal").grid(row=7,column=0)
shotog= Entry(tabplayer, bd=4)
shotog.focus_set()
shotog.grid(row=7,column=1)


Label(tabplayer, text="Goals").grid(row=8,column=0)
goals= Entry(tabplayer, bd=4)
goals.focus_set()
goals.grid(row=8,column=1)


Button(tabplayer, text= "SUBMIT",width= 20, command=lambda:func_InsertPlayerData()).grid(row=9,column=1)

# Select Widget

Creat_l= Label(tabplayer,text="Select a Player")
Creat_l.grid(row=0,column=2,pady=30,padx=30)
#Entry for Select Statement
L4 = Label(tabplayer, text="Player_ID")
L4.grid(row=1,column=2)
PIDSelect= Entry(tabplayer, bd=5)
PIDSelect.focus_set()
PIDSelect.grid(row=1,column=2)
Label(tabplayer,text="DATA").grid(row=1,column=3)


Button(tabplayer, text= "Select",width= 20, command=lambda:func_SelectPlayerData()).grid(row=9,column=2)



#Update an Entry widget to accept User Input for Season

Creat_l= Label(tabplayer,text="Update Player Stats")
Creat_l.grid(row=10,column=1,pady=30,padx=30)

Label(tabplayer, text="Player_ID").grid(row=11,column=0)
Pid1= Entry(tabplayer, bd=5)
Pid1.focus_set()
Pid1.grid(row=11,column=1)

Label(tabplayer, text="Team").grid(row=12,column=0)
Team1= Entry(tabplayer, bd=4)
Team1.focus_set()
Team1.grid(row=12,column=1)


Label(tabplayer, text="season").grid(row=13,column=0)
playerseason1= Entry(tabplayer, bd=4)
playerseason1.focus_set()
playerseason1.grid(row=13,column=1)

Label(tabplayer, text="Position").grid(row=14,column=0)
position1= Entry(tabplayer, bd=4)
position1.focus_set()
position1.grid(row=14,column=1)

Label(tabplayer, text="Minutes").grid(row=15,column=0)
minutes1= Entry(tabplayer, bd=4)
minutes1.focus_set()
minutes1.grid(row=15,column=1)


Label(tabplayer, text="Shots").grid(row=16,column=0)
shots1= Entry(tabplayer, bd=4)
shots1.focus_set()
shots1.grid(row=16,column=1)


Label(tabplayer, text="Shots On Goal").grid(row=17,column=0)
shotog1= Entry(tabplayer, bd=4)
shotog1.focus_set()
shotog1.grid(row=17,column=1)


Label(tabplayer, text="Goals").grid(row=18,column=0)
goals1= Entry(tabplayer, bd=4)
goals1.focus_set()
goals1.grid(row=18,column=1)

Label(tabplayer, text="Player-Name").grid(row=19,column=0)
pname1= Entry(tabplayer, bd=4)
pname1.focus_set()
pname1.grid(row=19,column=1)


Button(tabplayer, text= "SUBMIT",width= 20, command=lambda:func_UpdatePlayerData()).grid(row=20,column=1)



# Delete Widget

Creat_l= Label(tabplayer,text="Insert Player_ID to be deleted")
Creat_l.grid(row=10,column=2,pady=30,padx=30)
#Entry for Delete Statement
Label(tabplayer, text="Player_ID").grid(row=12,column=2)
playerdelete= Entry(tabplayer, bd=5)
playerdelete.focus_set()
playerdelete.grid(row=13,column=2)


Button(tabplayer, text= "Delete",width= 20, command=lambda:func_DeleteSeasonDat()).grid(row=14,column=2)


#------------------------------------------------------------------------------------------------Player--------------------------------------------------------------------------------------------------------------------------











#end the program
root.mainloop()




