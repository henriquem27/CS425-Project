from tkinter import *
import psycopg2
import datetime
from tkinter import ttk


root = Tk()
root.title('Testing CRUD MLS')

root.geometry("700x700")
def func_CreateData():
        
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
            
        print("Data was suscessfully inserted")
        conn.commit()

    except:
        print("OPS, something went wrong. Please check the data")

    finally:
        conn.close()



#Create an Entry widget to accept User Input for Season
L1 = Label(root, text="Season")
L1.place(relx=0.2,rely=0.2,anchor='s')
season= Entry(root, bd=5)
season.focus_set()
season.place(relx=0.2,rely=0.2,anchor='n')



  

#User input for Start-Date
L2 = Label(root, text="Start_date")
L2.place(relx=0.2,rely=0.3,anchor='s')
start_date= Entry(root, bd=5)
start_date.focus_set()
start_date.place(relx=0.2,rely=0.3,anchor='n')


#User input for End-Date
L3 = Label(root, text="End_date")
L3.place(relx=0.2,rely=0.4,anchor='s')
end_date= Entry(root, bd=5)
end_date.focus_set()
end_date.place(relx=0.2,rely=0.4,anchor='n')


Button(root, text= "SUBMIT",width= 20, command=lambda:func_CreateData()).place(relx=0.2,rely=0.5,anchor='n')


#end the program
root.mainloop()