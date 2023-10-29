from tkinter import *
import psycopg2
import datetime
from tkinter import ttk
import tkinter.messagebox as MessageBox


root = Tk()
root.title('Major League Soccer Database')

root.geometry("700x700")
tabControl = ttk.Notebook(root)
tabseason = ttk.Frame(tabControl)
tabplayer = ttk.Frame(tabControl)
tabControl.add(tabseason, text='Seasons')
tabControl.add(tabplayer, text='Player')
tabControl.pack(expand=1, fill="both")



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
        seasonselectdata=seasonselect.get()
        if(seasonselectdata==""):
                MessageBox.showerror("Error","Please enter an ID to be Inserted")

        else:
        
            cursor = conn.cursor()
            DATA=int(seasonselectdata)
            QUERY="UPDATE seasons WHERE="
            cursor.execute(QUERY,(DATA,))
            




            
            conn.commit()

    except:
        MessageBox.showinfo("ALERT", "something went wrong.")
    finally:
        conn.close()
    
    




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


Creat_l= Label(tabseason,text="Select a Season")
Creat_l.grid(row=0,column=2,pady=30,padx=30)
#Entry for Select Statement
L4 = Label(tabseason, text="Season_ID")
L4.grid(row=1,column=2)
seasonselect= Entry(tabseason, bd=5)
seasonselect.focus_set()
seasonselect.grid(row=1,column=3)


Button(tabseason, text= "Select",width= 20, command=lambda:func_SelectSeasonData()).grid(row=4,column=3)



#end the program
root.mainloop()




