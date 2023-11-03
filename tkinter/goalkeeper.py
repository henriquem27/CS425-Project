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
tabControl.add(tabgames,text='Games')
tabControl.add(tabsalary,text='Salaries')
tabControl.add(tabpasses,text='Passes')
tabControl.add(tabteams,text='teams')


tabControl.pack(expand=1, fill="both")









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
        Pid1data= Pid1.get()
        Teamdata = Team1.get()
        pseasondata = gkseason1.get()
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
            QUERY="UPDATE gk SET (team_id,season_id,gk_name,position,minutes,shots,shotsongoal,goals)=(%s,%s,%s,%s,%s,%s,%s,%s) WHERE gk_id=(%s)"
            cursor.execute(QUERY,DATA)
            MessageBox.showinfo("Sucesss","Data was Updated")




            
            conn.commit()

    except:
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
Pid1= Entry(tabgk, bd=4)
Pid1.focus_set()
Pid1.grid(row=rowupdategk+1,column=3)

Label(tabgk, text="Team").grid(row=rowupdategk+2,column=2)
Team1= Entry(tabgk, bd=4)
Team1.focus_set()
Team1.grid(row=rowupdategk+2,column=3)


Label(tabgk, text="season").grid(row=rowupdategk+3,column=2)
gkseason1= Entry(tabgk, bd=4)
gkseason1.focus_set()
gkseason1.grid(row=rowupdategk+3,column=3)

Label(tabgk, text="Position").grid(row=rowupdategk+4,column=2)
position1= Entry(tabgk, bd=4)
position1.focus_set()
position1.grid(row=rowupdategk+4,column=3)

Label(tabgk, text="Minutes").grid(row=rowupdategk+5,column=2)
minutes1= Entry(tabgk, bd=4)
minutes1.focus_set()
minutes1.grid(row=rowupdategk+5,column=3)


Label(tabgk, text="Shots").grid(row=rowupdategk+6,column=2)
shots1= Entry(tabgk, bd=4)
shots1.focus_set()
shots1.grid(row=rowupdategk+6,column=3)


Label(tabgk, text="Shots On Goal").grid(row=rowupdategk+7,column=2)
shotog1= Entry(tabgk, bd=4)
shotog1.focus_set()
shotog1.grid(row=rowupdategk+7,column=3)


Label(tabgk, text="Goals").grid(row=rowupdategk+8,column=2)
goals1= Entry(tabgk, bd=4)
goals1.focus_set()
goals1.grid(row=rowupdategk+8,column=3)

Label(tabgk, text="Firstname-Lastname").grid(row=rowupdategk+9,column=2)
pname1= Entry(tabgk, bd=4)
pname1.focus_set()
pname1.grid(row=rowupdategk+9,column=3)


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


#------------------------------------------------------------------------------------------------Player GUI--------------------------------------------------------------------------------------------------------------------------|


















root.mainloop()
