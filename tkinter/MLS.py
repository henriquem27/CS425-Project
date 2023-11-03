from tkinter import *
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


tabControl.add(tabseason, text='Seasons')
tabControl.add(tabplayer, text='Player')
tabControl.add(tabgk,text='Goalkeepers')
tabControl.add(tabteams,text='Teams')
tabControl.add(tabgames,text='Games')
tabControl.add(tabsalary,text='Salaries')
tabControl.add(tabpasses,text='Passes')



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



#player-----------------------------------------------------------------------------------------FUNCTIONS------------------------------------------------------------------

def func_InsertPlayerData():
        
    conn = psycopg2.connect(
    host="127.0.0.1",
    database='Project-Test',
    user='postgres',
    password='123qw123'
        )
            
    try:
        firstname=firstnamein.get()
        lastname= lastnamein.get()
        teamp=Team.get()
        seasonp=playerseason.get()
        position1=position.get()
        minutesp=minutes.get()
        shotsp=shots.get()
        shotogp=shotog.get()
        goalsp=goals.get()
        
        playername = firstname+"-"+lastname
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
        fname = fnameSelect.get()
        lname = lnameSelect.get()
        playername= fname+"-"+lname

        if(pidata=="" and fname=="" and lname==""):
                MessageBox.showerror("Error","Please enter a Player_ID or First and Last name")
        if(pidata!="" and fname!="" and lname!=""):
                MessageBox.showerror("Error","Please make sure you are only using Player_ID or First and Last name")
        

        if(pidata=="" and fname!="" and lname!=""):
        
            cursor = conn.cursor()
            DATA=(playername,)
            QUERY="SELECT * FROM player WHERE player_name=(%s)"
            cursor.execute(QUERY,DATA)
            records=cursor.fetchall()
            #Clear the loop entries for the data after row 13
            for label in tabplayer.grid_slaves():
             if int(label.grid_info()["row"]) > 13:
                label.grid_forget()
            output = ''
            # Loop thru the result
            Label(tabplayer,text="Player_id").grid(row=14,column=0)
            Label(tabplayer,text="Team").grid(row=14,column=1)
            Label(tabplayer,text="season_id").grid(row=14,column=2)
            Label(tabplayer,text="Player Name").grid(row=14,column=3)
            Label(tabplayer,text="Position").grid(row=14,column=4)
            Label(tabplayer,text="Minutes").grid(row=14,column=5,padx=5)
            Label(tabplayer,text=" Shots").grid(row=14,column=6,padx=5)
            Label(tabplayer,text="Shots on Goal").grid(row=14,column=7,padx=5)
            Label(tabplayer,text="Goals").grid(row=14,column=8,padx=5)
            for x in range(len(records)):
                 Label(tabplayer,text=records[x][0]).grid(row=x+15,column=0)
                 team=records[x][1]
                 Label(tabplayer,text=team[:3]).grid(row=x+15,column=1)
                 Label(tabplayer,text=records[x][2]).grid(row=x+15,column=2)
                 Label(tabplayer,text=records[x][3]).grid(row=x+15,column=3)
                 Label(tabplayer,text=records[x][4]).grid(row=x+15,column=4)
                 Label(tabplayer,text=records[x][5]).grid(row=x+15,column=5)
                 Label(tabplayer,text=records[x][6]).grid(row=x+15,column=6)
                 Label(tabplayer,text=records[x][7]).grid(row=x+15,column=7)
                 Label(tabplayer,text=records[x][8]).grid(row=x+15,column=8)
            conn.commit()
        if(pidata!="" and fname=="" and lname==""):
            cursor = conn.cursor()
            DATA=(pidata,)
            QUERY="SELECT * FROM player WHERE player_id=(%s)"
            cursor.execute(QUERY,DATA)
            records=cursor.fetchall()
            for label in tabplayer.grid_slaves():
             if int(label.grid_info()["row"]) > 13:
                label.grid_forget()
            output = ''
            # Loop thru the result
            Label(tabplayer,text="Player_id").grid(row=14,column=0)
            Label(tabplayer,text="Team_ID").grid(row=14,column=1)
            Label(tabplayer,text="season_id").grid(row=14,column=2)
            Label(tabplayer,text="Position").grid(row=14,column=3)
            Label(tabplayer,text="Minutes").grid(row=14,column=4)
            Label(tabplayer,text=" Shots ").grid(row=14,column=5)
            Label(tabplayer,text=" ShotsOnGoal ").grid(row=14,column=6,padx=2)
            Label(tabplayer,text="Goals").grid(row=14,column=7,padx=5)
            for x in range(len(records)):
                 Label(tabplayer,text=records[x][0]).grid(row=x+15,column=0)
                 Label(tabplayer,text=records[x][1]).grid(row=x+15,column=1)
                 Label(tabplayer,text=records[x][2]).grid(row=x+15,column=2)
                 Label(tabplayer,text=records[x][3]).grid(row=x+15,column=3)
                 Label(tabplayer,text=records[x][4]).grid(row=x+15,column=4)
                 Label(tabplayer,text=records[x][5]).grid(row=x+15,column=5)
                 Label(tabplayer,text=records[x][6]).grid(row=x+15,column=6)
                 Label(tabplayer,text=records[x][7]).grid(row=x+15,column=7)
                 Label(tabplayer,text=records[x][8]).grid(row=x+15,column=8)
            conn.commit()
             
                 
            




            
            
        

    except Exception:
        traceback.print_exc()
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


def func_DelePlayerDat():
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
    
    
#player-----------------------------------------------------------------------------------------FUNCTIONS------------------------------------------------------------------



#------------------------------------------------------------------------------------------------Player GUI--------------------------------------------------------------------------------------------------------------------------



#Create an Entry widget to accept User Input for Player
Creat_l= Label(tabplayer,text="Insert a New player")
Creat_l.grid(row=0,column=1,pady=30,padx=30)

Label(tabplayer, text="First Name").grid(row=1,column=0,padx=1,pady=1)
firstnamein= Entry(tabplayer, bd=5)
firstnamein.focus_set()
firstnamein.grid(row=1,column=1)

Label(tabplayer, text="Last Name").grid(row=2,column=0)
lastnamein= Entry(tabplayer, bd=4)
lastnamein.focus_set()
lastnamein.grid(row=2,column=1)


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

Label(tabplayer, text="Team").grid(row=9,column=0)
Team= Entry(tabplayer, bd=4)
Team.focus_set()
Team.grid(row=9,column=1)


Button(tabplayer, text= "SUBMIT",width= 20, command=lambda:func_InsertPlayerData()).grid(row=10,column=1)

# Select Widget

Creat_l= Label(tabplayer,text="<<---Select a Player---->")
Creat_l.grid(row= 11,column=2,pady=30,padx=30)
#Entry for Select Statement
L4 = Label(tabplayer, text="Player_ID")
L4.grid(row=11,column=1)
PIDSelect= Entry(tabplayer, bd=5)
PIDSelect.focus_set()
PIDSelect.grid(row=12,column=1)


#Entry for Select Statement
L4 = Label(tabplayer, text="First Name")
L4.grid(row=11,column=3)
fnameSelect= Entry(tabplayer, bd=5)
fnameSelect.focus_set()
fnameSelect.grid(row=12,column=3)

L4 = Label(tabplayer, text="Last Name")
L4.grid(row=11,column=4)
lnameSelect= Entry(tabplayer, bd=5)
lnameSelect.focus_set()
lnameSelect.grid(row=12,column=4)




Button(tabplayer, text= "Select",width= 20, command=lambda:func_SelectPlayerData()).grid(row=12,column=2)




#Update an Entry widget to accept User Input for Season

rowupdateplayer=0

Creat_l= Label(tabplayer,text="Update Player Stats")
Creat_l.grid(row=rowupdateplayer,column=3,pady=30,padx=30)

Label(tabplayer, text="Player_ID").grid(row=rowupdateplayer+1,column=2,padx=2,pady=2)
Pid1= Entry(tabplayer, bd=4)
Pid1.focus_set()
Pid1.grid(row=rowupdateplayer+1,column=3)

Label(tabplayer, text="Team").grid(row=rowupdateplayer+2,column=2)
Team1= Entry(tabplayer, bd=4)
Team1.focus_set()
Team1.grid(row=rowupdateplayer+2,column=3)


Label(tabplayer, text="season").grid(row=rowupdateplayer+3,column=2)
playerseason1= Entry(tabplayer, bd=4)
playerseason1.focus_set()
playerseason1.grid(row=rowupdateplayer+3,column=3)

Label(tabplayer, text="Position").grid(row=rowupdateplayer+4,column=2)
position1= Entry(tabplayer, bd=4)
position1.focus_set()
position1.grid(row=rowupdateplayer+4,column=3)

Label(tabplayer, text="Minutes").grid(row=rowupdateplayer+5,column=2)
minutes1= Entry(tabplayer, bd=4)
minutes1.focus_set()
minutes1.grid(row=rowupdateplayer+5,column=3)


Label(tabplayer, text="Shots").grid(row=rowupdateplayer+6,column=2)
shots1= Entry(tabplayer, bd=4)
shots1.focus_set()
shots1.grid(row=rowupdateplayer+6,column=3)


Label(tabplayer, text="Shots On Goal").grid(row=rowupdateplayer+7,column=2)
shotog1= Entry(tabplayer, bd=4)
shotog1.focus_set()
shotog1.grid(row=rowupdateplayer+7,column=3)


Label(tabplayer, text="Goals").grid(row=rowupdateplayer+8,column=2)
goals1= Entry(tabplayer, bd=4)
goals1.focus_set()
goals1.grid(row=rowupdateplayer+8,column=3)

Label(tabplayer, text="Firstname-Lastname").grid(row=rowupdateplayer+9,column=2)
pname1= Entry(tabplayer, bd=4)
pname1.focus_set()
pname1.grid(row=rowupdateplayer+9,column=3)


Button(tabplayer, text= "SUBMIT",width= 20, command=lambda:func_UpdatePlayerData()).grid(row=rowupdateplayer+10,column=3)



# Delete Widget

Creat_l= Label(tabplayer,text="Insert Player_ID to be deleted")
Creat_l.grid(row=0,column=4,pady=30,padx=30)
#Entry for Delete Statement
Label(tabplayer, text="Player_ID").grid(row=1,column=4)
playerdelete= Entry(tabplayer, bd=5)
playerdelete.focus_set()
playerdelete.grid(row=2,column=4)


Button(tabplayer, text= "Delete",width= 20, command=lambda:func_DelePlayerDat()).grid(row=4,column=4)


#------------------------------------------------------------------------------------------------Player GUI--------------------------------------------------------------------------------------------------------------------------|






#gk-----------------------------------------------------------------------------------------FUNCTIONS------------------------------------------------------------------

def func_InsertgkData():
        
    conn = psycopg2.connect(
    host="127.0.0.1",
    database='Project-Test',
    user='postgres',
    password='123qw123'
        )
            
    try:
        firstname=firstnameingk.get()
        lastname= lastnameingk.get()
        teamp=Teamgk.get()
        seasonp=gkseason.get()
        minutes=minutesgk.get()
        shtsfaced=shtfa.get()
        gconceded=gcon.get()
        savesgk=saves.get()
        
        gkname = firstname+"-"+lastname
        team_id=teamp+seasonp
        pid=gkname+"-"+seasonp

        cursor = conn.cursor()
        QUERY="INSERT INTO goalkeepers VALUES (%s,%s,%s,%s,%s,%s,%s,%s);"
        DATA=(pid,team_id,int(seasonp),gkname,int(minutes),int(shtsfaced),int(gconceded),int(savesgk))
        cursor.execute(QUERY,DATA)
            
        
        conn.commit()
        MessageBox.showinfo("OK","Data Sucessfully Inserted")

    except:
        MessageBox.showerror("OPS"," something went wrong. Please check the data")

    finally:
        conn.close()


def func_SelectgkData():
    conn = psycopg2.connect(
    host="127.0.0.1",
    database='Project-Test',
    user='postgres',
    password='123qw123'
        )
    
    try:
        
        pidata=PIDSelectgk.get()
        fname = fnameSelectgk.get()
        lname = lnameSelectgk.get()
        gkname= fname+"-"+lname

        if(pidata=="" and fname=="" and lname==""):
                MessageBox.showerror("Error","Please enter a gk_ID or First and Last name")
        if(pidata!="" and fname!="" and lname!=""):
                MessageBox.showerror("Error","Please make sure you are only using gk_ID or First and Last name")
        

        if(pidata=="" and fname!="" and lname!=""):
        
            cursor = conn.cursor()
            DATA=(gkname,)
            QUERY="SELECT * FROM goalkeepers WHERE gk_name=(%s)"
            cursor.execute(QUERY,DATA)
            records=cursor.fetchall()
            #Clear the loop entries for the data after row 13
            for label in tabgk.grid_slaves():
             if int(label.grid_info()["row"]) > 13:
                label.grid_forget()
            output = ''
            # Loop thru the result
            Label(tabgk,text="gk_id").grid(row=14,column=0)
            Label(tabgk,text="Team").grid(row=14,column=1)
            Label(tabgk,text="season_id").grid(row=14,column=2)
            Label(tabgk,text="gk Name").grid(row=14,column=3)
            Label(tabgk,text="Minutes").grid(row=14,column=4)
            Label(tabgk,text="Shots Faced").grid(row=14,column=5,padx=5)
            Label(tabgk,text="Goals Conceded").grid(row=14,column=6,padx=5)
            Label(tabgk,text="Saves").grid(row=14,column=7,padx=5)
            for x in range(len(records)):
                 Label(tabgk,text=records[x][0]).grid(row=x+15,column=0)
                 team=records[x][1]
                 Label(tabgk,text=team[:3]).grid(row=x+15,column=1)
                 Label(tabgk,text=records[x][2]).grid(row=x+15,column=2)
                 Label(tabgk,text=records[x][3]).grid(row=x+15,column=3)
                 Label(tabgk,text=records[x][4]).grid(row=x+15,column=4)
                 Label(tabgk,text=records[x][5]).grid(row=x+15,column=5)
                 Label(tabgk,text=records[x][6]).grid(row=x+15,column=6)
                 Label(tabgk,text=records[x][7]).grid(row=x+15,column=7)
            conn.commit()
        if(pidata!="" and fname=="" and lname==""):
            cursor = conn.cursor()
            DATA=(pidata,)
            QUERY="SELECT * FROM goalkeepers WHERE gk_id=(%s)"
            cursor.execute(QUERY,DATA)
            records=cursor.fetchall()
            for label in tabgk.grid_slaves():
             if int(label.grid_info()["row"]) > 13:
                label.grid_forget()
            output = ''
            # Loop thru the result
            Label(tabgk,text="gk_id").grid(row=14,column=0)
            Label(tabgk,text="Team_if").grid(row=14,column=1)
            Label(tabgk,text="season_id").grid(row=14,column=2)
            Label(tabgk,text="gk-Name").grid(row=14,column=3)
            Label(tabgk,text="Minutes").grid(row=14,column=4)
            Label(tabgk,text="Shots Faced").grid(row=14,column=5,padx=5)
            Label(tabgk,text="Goals Conceded").grid(row=14,column=6,padx=5)
            Label(tabgk,text="Saves").grid(row=14,column=7,padx=5)
            for x in range(len(records)):
                 Label(tabgk,text=records[x][0]).grid(row=x+15,column=0)
                 Label(tabgk,text=records[x][1]).grid(row=x+15,column=1)
                 Label(tabgk,text=records[x][2]).grid(row=x+15,column=2)
                 Label(tabgk,text=records[x][3]).grid(row=x+15,column=3)
                 Label(tabgk,text=records[x][4]).grid(row=x+15,column=4)
                 Label(tabgk,text=records[x][5]).grid(row=x+15,column=5)
                 Label(tabgk,text=records[x][6]).grid(row=x+15,column=6)
                 Label(tabgk,text=records[x][7]).grid(row=x+15,column=7)

            conn.commit()
             
                 
            




            
            
        

    except Exception:
        traceback.print_exc()
        MessageBox.showinfo("ALERT", "something went wrong.")
    finally:
        conn.close()


def func_UpdategkData():
    conn = psycopg2.connect(
    host="127.0.0.1",
    database='Project-Test',
    user='postgres',
    password='123qw123'
        )
    
    try:
        Pid1data= Pid1gk.get()
        Teamdata = Team1gk.get()
        pseasondata = gkseason1.get()
        namedata = flnamegk.get()
        mindata = minutes1gk.get()
        shtfaced= shfacedgk.get()
        gcon = gcon1gk.get()
        saves = savesgk1.get()

        team_id=Teamdata+pseasondata


        if(Pid1data==""):
                MessageBox.showerror("Error","Please enter an ID to be Updated")

        else:
            
            cursor = conn.cursor()
            
            DATA=(team_id,int(pseasondata),namedata,int(mindata),int(shtfaced),int(gcon),int(saves),Pid1data)
            QUERY="UPDATE goalkeepers SET (team_id,season_id,gk_name,minutes,shotsfaced,goalsconceded,saves)=(%s,%s,%s,%s,%s,%s,%s) WHERE gk_id=(%s)"
            cursor.execute(QUERY,DATA)
            MessageBox.showinfo("Sucesss","Data was Updated")




            
            conn.commit()

    except Exception:
        traceback.print_exc()
        MessageBox.showinfo("ALERT", "something went wrong.")
    finally:
        conn.close()


def func_DelegkDat():
    conn = psycopg2.connect(
    host="127.0.0.1",
    database='Project-Test',
    user='postgres',
    password='123qw123'
        )
    
    try:
        gkdeletedata=gkdelete.get()

        if(gkdelete==""):
                MessageBox.showerror("Error","Please enter an ID to be Updated")

        else:
            
            cursor = conn.cursor()
            
            DATA=(gkdeletedata,)
            QUERY="DELETE FROM goalkeepers WHERE gk_id=(%s)"
            cursor.execute(QUERY,DATA)
            MessageBox.showinfo("Sucesss","Data was Deleted")

            conn.commit()

    except:
        MessageBox.showinfo("ALERT", "something went wrong.")
    finally:
        conn.close()
    
    
#gk-----------------------------------------------------------------------------------------FUNCTIONS------------------------------------------------------------------



#------------------------------------------------------------------------------------------------gk GUI--------------------------------------------------------------------------------------------------------------------------



#Create an Entry widget to accept User Input for gk
Creat_l= Label(tabgk,text="Insert a New gk")
Creat_l.grid(row=0,column=1,pady=30,padx=30)

Label(tabgk, text="First Name").grid(row=1,column=0,padx=1,pady=1)
firstnameingk= Entry(tabgk, bd=5)
firstnameingk.focus_set()
firstnameingk.grid(row=1,column=1)

Label(tabgk, text="Last Name").grid(row=2,column=0)
lastnameingk= Entry(tabgk, bd=4)
lastnameingk.focus_set()
lastnameingk.grid(row=2,column=1)


Label(tabgk, text="season").grid(row=3,column=0)
gkseason= Entry(tabgk, bd=4)
gkseason.focus_set()
gkseason.grid(row=3,column=1)


Label(tabgk, text="Minutes").grid(row=4,column=0)
minutesgk= Entry(tabgk, bd=4)
minutesgk.focus_set()
minutesgk.grid(row=4,column=1)


Label(tabgk, text="Shots Faced").grid(row=5,column=0)
shtfa= Entry(tabgk, bd=4)
shtfa.focus_set()
shtfa.grid(row=5,column=1)


Label(tabgk, text="Goals Conceded").grid(row=6,column=0)
gcon= Entry(tabgk, bd=4)
gcon.focus_set()
gcon.grid(row=6,column=1)


Label(tabgk, text="Saves").grid(row=7,column=0)
saves= Entry(tabgk, bd=4)
saves.focus_set()
saves.grid(row=7,column=1)

Label(tabgk, text="Team").grid(row=8,column=0)
Teamgk= Entry(tabgk, bd=4)
Teamgk.focus_set()
Teamgk.grid(row=8,column=1)


Button(tabgk, text= "SUBMIT",width= 20, command=lambda:func_InsertgkData()).grid(row=10,column=1)

# Select Widget

Creat_l= Label(tabgk,text="<<---Select a gk---->")
Creat_l.grid(row= 11,column=2,pady=30,padx=30)
#Entry for Select Statement
L4 = Label(tabgk, text="gk_ID")
L4.grid(row=11,column=1)
PIDSelectgk= Entry(tabgk, bd=5)
PIDSelectgk.focus_set()
PIDSelectgk.grid(row=12,column=1)


#Entry for Select Statement
L4 = Label(tabgk, text="First Name")
L4.grid(row=11,column=3)
fnameSelectgk= Entry(tabgk, bd=5)
fnameSelectgk.focus_set()
fnameSelectgk.grid(row=12,column=3)

L4 = Label(tabgk, text="Last Name")
L4.grid(row=11,column=4)
lnameSelectgk= Entry(tabgk, bd=5)
lnameSelectgk.focus_set()
lnameSelectgk.grid(row=12,column=4)




Button(tabgk, text= "Select",width= 20, command=lambda:func_SelectgkData()).grid(row=12,column=2)




#Update an Entry widget to accept User Input for Season

rowupdategk=0

Creat_l= Label(tabgk,text="Update gk Stats")
Creat_l.grid(row=rowupdategk,column=3,pady=30,padx=30)

Label(tabgk, text="gk_ID").grid(row=rowupdategk+1,column=2,padx=2,pady=2)
Pid1gk= Entry(tabgk, bd=4)
Pid1gk.focus_set()
Pid1gk.grid(row=rowupdategk+1,column=3)

Label(tabgk, text="Team").grid(row=rowupdategk+2,column=2)
Team1gk= Entry(tabgk, bd=4)
Team1gk.focus_set()
Team1gk.grid(row=rowupdategk+2,column=3)


Label(tabgk, text="season").grid(row=rowupdategk+3,column=2)
gkseason1= Entry(tabgk, bd=4)
gkseason1.focus_set()
gkseason1.grid(row=rowupdategk+3,column=3)

Label(tabgk, text="First-Lastname").grid(row=rowupdategk+4,column=2)
flnamegk= Entry(tabgk, bd=4)
flnamegk.focus_set()
flnamegk.grid(row=rowupdategk+4,column=3)

Label(tabgk, text="Minutes").grid(row=rowupdategk+5,column=2)
minutes1gk= Entry(tabgk, bd=4)
minutes1gk.focus_set()
minutes1gk.grid(row=rowupdategk+5,column=3)


Label(tabgk, text="Shots Faced").grid(row=rowupdategk+6,column=2)
shfacedgk= Entry(tabgk, bd=4)
shfacedgk.focus_set()
shfacedgk.grid(row=rowupdategk+6,column=3)


Label(tabgk, text="Goals Conceded").grid(row=rowupdategk+7,column=2)
gcon1gk= Entry(tabgk, bd=4)
gcon1gk.focus_set()
gcon1gk.grid(row=rowupdategk+7,column=3)


Label(tabgk, text="Saves").grid(row=rowupdategk+8,column=2)
savesgk1= Entry(tabgk, bd=4)
savesgk1.focus_set()
savesgk1.grid(row=rowupdategk+8,column=3)


Button(tabgk, text= "SUBMIT",width= 20, command=lambda:func_UpdategkData()).grid(row=rowupdategk+10,column=3)



# Delete Widget

Creat_l= Label(tabgk,text="Insert gk_ID to be deleted")
Creat_l.grid(row=0,column=4,pady=30,padx=30)
#Entry for Delete Statement
Label(tabgk, text="gk_ID").grid(row=1,column=4)
gkdelete= Entry(tabgk, bd=5)
gkdelete.focus_set()
gkdelete.grid(row=2,column=4)


Button(tabgk, text= "Delete",width= 20, command=lambda:func_DelegkDat()).grid(row=4,column=4)


#------------------------------------------------------------------------------------------------Goalkeepers GUI--------------------------------------------------------------------------------------------------------------------------|






#------------------------------------------------------Teams--------------------------------------------------------------|


def func_InsertTeamData():
    conn = psycopg2.connect(
        host="127.0.0.1",
        database='Project-Test',
        user='postgres',
        password='123qw123'
    )
    try:
        team = team_id_entry.get()
        games = int(games_entry.get())
        shots_for = int(shots_for_entry.get())
        shots_against = int(shots_against_entry.get())
        goals_for = int(goals_for_entry.get())
        goals_against = int(goals_against_entry.get())
        season = season_entry.get()
        team_id=team+season
        cursor = conn.cursor()
        QUERY = "INSERT INTO Teams (team_id,season_id ,team,gamesplayed, ShotsFor, ShotsAgainst, GoalsFor, GoalsAgainst) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);"
        DATA = (team_id,int(season) ,team,games, shots_for, shots_against, goals_for, goals_against)
        cursor.execute(QUERY, DATA)
        conn.commit()
        MessageBox.showinfo("OK", "Data Successfully Inserted")
    except Exception:
        traceback.print_exc()
        MessageBox.showerror("OPS", "Something went wrong. Please check the data")
    finally:
        conn.close()

def func_SelectTeamData():
    conn = psycopg2.connect(
        host="127.0.0.1",
        database='Project-Test',
        user='postgres',
        password='123qw123'
    )
    try:
        team_id = team_id_select.get()
        if team_id == "":
            MessageBox.showerror("Error", "Please enter a Team name to be selected")
        else:
            cursor = conn.cursor()
            QUERY = "SELECT * FROM Teams WHERE team=%s;"
            cursor.execute(QUERY, (team_id,))
            records = cursor.fetchall()
            for label in tabteams.grid_slaves():
             if int(label.grid_info()["row"]) > 14:
                label.grid_forget()
            Label(tabteams,text="team_id").grid(row=15,column=0)
            Label(tabteams,text="Season_ID").grid(row=15,column=1)
            Label(tabteams,text="Team").grid(row=15,column=2)
            Label(tabteams,text="Games Played").grid(row=15,column=3)
            Label(tabteams,text="Shots For").grid(row=15,column=4)
            Label(tabteams,text="Shots Faced").grid(row=15,column=5,padx=5)
            Label(tabteams,text="Goals For").grid(row=15,column=6,padx=5)
            Label(tabteams,text="Goals Against").grid(row=15,column=7,padx=5)
            Label(tabteams,text="Points").grid(row=15,column=8,padx=5)
            for x in range(len(records)):
                 Label(tabteams,text=records[x][0]).grid(row=x+16,column=0)
                 Label(tabteams,text=records[x][1]).grid(row=x+16,column=1)
                 Label(tabteams,text=records[x][2]).grid(row=x+16,column=2)
                 Label(tabteams,text=records[x][3]).grid(row=x+16,column=3)
                 Label(tabteams,text=records[x][4]).grid(row=x+16,column=4)
                 Label(tabteams,text=records[x][5]).grid(row=x+16,column=5)
                 Label(tabteams,text=records[x][6]).grid(row=x+16,column=6)
                 Label(tabteams,text=records[x][7]).grid(row=x+16,column=7)
                 Label(tabteams,text=records[x][8]).grid(row=x+16,column=8)
            conn.commit()

    except Exception:
        traceback.print_exc()
        MessageBox.showinfo("Alert", "Something went wrong.")
    finally:
        conn.close()

def func_UpdateTeamData():
    conn = psycopg2.connect(
        host="127.0.0.1",
        database='Project-Test',
        user='postgres',
        password='123qw123'
    )
    try:
        player_id = player_id_update.get()
        games = int(games_update.get())
        shots_for = int(shots_for_update.get())
        shots_against = int(shots_against_update.get())
        goals_for = int(goals_for_update.get())
        goals_against = int(goals_against_update.get())
        if player_id == "":
            MessageBox.showerror("Error", "Please enter a Player ID to be updated")
        else:
            cursor = conn.cursor()
            QUERY = "UPDATE Teams SET gamesplayed=%s, ShotsFor=%s, ShotsAgainst=%s, GoalsFor=%s, GoalsAgainst=%s WHERE team_id=%s;"
            DATA = (games, shots_for, shots_against, goals_for, goals_against, player_id)
            cursor.execute(QUERY, DATA)
            conn.commit()
            MessageBox.showinfo("Success", "Data was updated")

    except Exception:
        traceback.print_exc()
        MessageBox.showinfo("Alert", "Something went wrong.")
    finally:
        conn.close()

def func_DeleteTeamData():
    conn = psycopg2.connect(
        host="127.0.0.1",
        database='Project-Test',
        user='postgres',
        password='123qw123'
    )
    try:
        team_id = player_id_delete.get()
        if team_id== "":
            MessageBox.showerror("Error", "Please enter a Player ID to be deleted")
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
season_entry = Entry(tabteams, bd=5)
season_entry.focus_set()
season_entry.grid(row=7, column=1)

Button(tabteams, text="INSERT", width=20, command=lambda: func_InsertTeamData()).grid(row=8, column=1)

# Create widgets for the Select, Update, and Delete sections
Select_l = Label(tabteams, text="Select a Team")
Select_l.grid(row=11, column=0, pady=30, padx=30)

L7 = Label(tabteams, text="Team")
L7.grid(row=12, column=0)
team_id_select = Entry(tabteams, bd=5)
team_id_select.focus_set()
team_id_select.grid(row=13, column=0)
Button(tabteams, text="SELECT", width=20, command=lambda: func_SelectTeamData()).grid(row=14, column=0)

Update_l = Label(tabteams, text="Update a Team")
Update_l.grid(row=0, column=2, pady=30, padx=30)

L8 = Label(tabteams, text="TEAM_ID")
L8.grid(row=1, column=2)
player_id_update = Entry(tabteams, bd=5)
player_id_update.focus_set()
player_id_update.grid(row=1, column=3)

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

Button(tabteams, text="UPDATE", width=20, command=lambda: func_UpdateTeamData()).grid(row=8, column=3)

Delete_l = Label(tabteams, text="Delete a Team")
Delete_l.grid(row=0, column=4, pady=30, padx=30)

L14 = Label(tabteams, text="Team_ID")
L14.grid(row=1, column=4)
player_id_delete = Entry(tabteams, bd=5)
player_id_delete.focus_set()
player_id_delete.grid(row=2, column=4)

Button(tabteams, text="DELETE", width=20, command=lambda: func_DeleteTeamData()).grid(row=3, column=4)


#------------------------------------------------------Teams--------------------------------------------------------------|





#end the program
root.mainloop()




