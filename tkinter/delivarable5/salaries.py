from tkinter import *
import psycopg2
import datetime
from tkinter import ttk
import tkinter.messagebox as MessageBox
import traceback



def generate_salary(tabsalary):



    def func_InsertSalaryData():
        conn = psycopg2.connect(
            host="127.0.0.1",
            database='Project-Test',
            user='postgres',
            password='123qw123'
        )
        
        try:
            player_id = player_id_entry.get()
            base_salary = float(base_salary_entry.get())
            guaranteed_compensation = float(guaranteed_comp_entry.get())
            season_id = int(season_entry.get())
            cursor = conn.cursor()
            QUERY = "INSERT INTO Salaries (Player_ID, Base_Salary, GuaranteedCompensation,season_id) VALUES (%s, %s, %s, %s);"
            DATA = (player_id, base_salary, guaranteed_compensation,season_id)
            cursor.execute(QUERY, DATA)
            
            conn.commit()
            MessageBox.showinfo("OK", "Data Successfully Inserted")
        
        except Exception:
            traceback.print_exc()
            MessageBox.showerror("OPS", "Something went wrong. Please check the data")
        
        finally:
            conn.close()

    def func_SelectSalaryData():
        conn = psycopg2.connect(
            host="127.0.0.1",
            database='Project-Test',
            user='postgres',
            password='123qw123'
        )
        
        try:
            player_fname = player_fname_select.get()
            player_lname= player_lname_select.get()
            player_name= player_fname+"-"+player_lname
            if player_fname == "" or player_lname=="":
                MessageBox.showerror("Error", "Please enter a valid first and last name to be selected")
            else:
                cursor = conn.cursor()
                DATA = player_name
                QUERY = "SELECT p.player_id,team_id,player_name,Base_Salary,p.Season_ID,Position,Goals,GuaranteedCompensation from player p,salaries s where p.player_id = s.player_id and Player_Name=%s;"
                cursor.execute(QUERY, (DATA,))
                records = cursor.fetchall()
                for label in tabsalary.grid_slaves():
                    if int(label.grid_info()["row"]) > 14:
                        label.grid_forget()
                Label(tabsalary,text="Player_ID").grid(row=15,column=0)
                Label(tabsalary,text="Team_ID").grid(row=15,column=1)
                Label(tabsalary,text="Player-Name").grid(row=15,column=2)
                Label(tabsalary,text="Base-Salary").grid(row=15,column=3)
                Label(tabsalary,text="Season-ID").grid(row=15,column=4)
                Label(tabsalary,text="Position").grid(row=15,column=5,padx=4)
                Label(tabsalary,text="Goals").grid(row=15,column=6,padx=4)
                Label(tabsalary,text="Guaranteed Comp").grid(row=15,column=7,padx=4)
                for x in range(len(records)):
                    Label(tabsalary,text=records[x][0]).grid(row=x+16,column=0)
                    Label(tabsalary,text=records[x][1]).grid(row=x+16,column=1)
                    Label(tabsalary,text=records[x][2]).grid(row=x+16,column=2)
                    Label(tabsalary,text=records[x][3]).grid(row=x+16,column=3)
                    Label(tabsalary,text=records[x][4]).grid(row=x+16,column=4)
                    Label(tabsalary,text=records[x][5]).grid(row=x+16,column=5)
                    Label(tabsalary,text=records[x][6]).grid(row=x+16,column=6)
                    Label(tabsalary,text=records[x][7]).grid(row=x+16,column=7)
            
            conn.commit()
        
        except Exception:
            traceback.print_exc()
            MessageBox.showinfo("ALERT", "Something went wrong.")
        
        finally:
            conn.close()

    def func_UpdateSalaryData():
        conn = psycopg2.connect(
            host="127.0.0.1",
            database='Project-Test',
            user='postgres',
            password='123qw123'
        )
        
        try:
            player_id = player_id_update.get()
            base_salary = base_salary_update.get()
            guaranteed_compensation = guaranteed_compensation_update.get()
            season_id = season_update.get()
            
            if player_id == "":
                MessageBox.showerror("Error", "Please enter a Player ID to be updated")
            else:
                cursor = conn.cursor()
                DATA = (float(base_salary), float(guaranteed_compensation), int(season_id), player_id)
                QUERY = "UPDATE Salaries SET Base_Salary = %s, GuaranteedCompensation = %s, season_id=%s WHERE Player_ID = %s"
                cursor.execute(QUERY, DATA)
                MessageBox.showinfo("Success", "Data was updated")
                conn.commit()
        
        except Exception:
            traceback.print_exc()
            MessageBox.showinfo("ALERT", "Something went wrong.")
        
        finally:
            conn.close()

    def func_DeleteSalaryData():
        conn = psycopg2.connect(
            host="127.0.0.1",
            database='Project-Test',
            user='postgres',
            password='123qw123'
        )
        
        try:
            player_id = player_id_delete.get()
            
            if player_id == "":
                MessageBox.showerror("Error", "Please enter a Player ID to be deleted")
            else:
                cursor = conn.cursor()
                DATA = (player_id,)
                QUERY = "DELETE FROM Salaries WHERE Player_ID = %s"
                cursor.execute(QUERY, DATA)
                MessageBox.showinfo("Success", "Data was deleted")
            
            conn.commit()
        
        except Exception:
            traceback.print_exc()
            MessageBox.showinfo("ALERT", "Something went wrong.")
        
        finally:
            conn.close()






    # Create an Entry widget to accept User Input for Salaries
    Create_l = Label(tabsalary, text="Insert Into Salaries")
    Create_l.grid(row=0, column=1, pady=30, padx=30)

    L1 = Label(tabsalary, text="Player_ID")
    L1.grid(row=1, column=0)
    player_id_entry = Entry(tabsalary, bd=5)
    player_id_entry.focus_set()
    player_id_entry.grid(row=1, column=1)

    L2 = Label(tabsalary, text="Base Salary")
    L2.grid(row=2, column=0)
    base_salary_entry = Entry(tabsalary, bd=5)
    base_salary_entry.focus_set()
    base_salary_entry.grid(row=2, column=1)

    L3 = Label(tabsalary, text="Guaranteed Compensation")
    L3.grid(row=3, column=0)
    guaranteed_comp_entry = Entry(tabsalary, bd=5)
    guaranteed_comp_entry.focus_set()
    guaranteed_comp_entry.grid(row=3, column=1)

    L3 = Label(tabsalary, text="Season")
    L3.grid(row=4, column=0)
    season_entry = Entry(tabsalary, bd=5)
    season_entry.focus_set()
    season_entry.grid(row=4, column=1)


    Button(tabsalary, text="INSERT", width=20, command=lambda: func_InsertSalaryData()).grid(row=5, column=1)

    # Select Widget
    Create_l = Label(tabsalary, text="Select a Player's Salary")
    Create_l.grid(row=6, column=2, pady=30, padx=30)

    L4 = Label(tabsalary, text="First Name")
    L4.grid(row=7, column=2)
    player_fname_select = Entry(tabsalary, bd=5)
    player_fname_select.focus_set()
    player_fname_select.grid(row=8, column=2)
    L4 = Label(tabsalary, text="Last Name")
    L4.grid(row=7, column=3)
    player_lname_select = Entry(tabsalary, bd=5)
    player_lname_select.focus_set()
    player_lname_select.grid(row=8, column=3)

    Button(tabsalary, text="Select", width=20, command=lambda: func_SelectSalaryData()).grid(row=9, column=2)

    # Update an Entry widget to accept User Input for Salaries
    Update_l = Label(tabsalary, text="Update a Player's Salary")
    Update_l.grid(row=6, column=1, pady=30, padx=30)

    Label(tabsalary, text="Player_Name").grid(row=7, column=0)
    player_id_update = Entry(tabsalary, bd=5)
    player_id_update.focus_set()
    player_id_update.grid(row=7, column=1)

    L2 = Label(tabsalary, text="Base Salary")
    L2.grid(row=8, column=0)
    base_salary_update = Entry(tabsalary, bd=5)
    base_salary_update.focus_set()
    base_salary_update.grid(row=8, column=1)

    L3 = Label(tabsalary, text="Guaranteed Compensation")
    L3.grid(row=9, column=0)
    guaranteed_compensation_update = Entry(tabsalary, bd=5)
    guaranteed_compensation_update.focus_set()
    guaranteed_compensation_update.grid(row=9, column=1)

    L3 = Label(tabsalary, text="Season")
    L3.grid(row=10, column=0)
    season_update = Entry(tabsalary, bd=5)
    season_update.focus_set()
    season_update.grid(row=10, column=1)


    Button(tabsalary, text="SUBMIT", width=20, command=lambda: func_UpdateSalaryData()).grid(row=11, column=1)

    # Delete Widget
    Create_l = Label(tabsalary, text="Select a Player's Salary to be deleted")
    Create_l.grid(row=0, column=2, pady=30, padx=30)

    L4 = Label(tabsalary, text="Player_ID")
    L4.grid(row=1, column=2)
    player_id_delete = Entry(tabsalary, bd=5)
    player_id_delete.focus_set()
    player_id_delete.grid(row=2, column=2)

    Button(tabsalary, text="Delete", width=20, command=lambda: func_DeleteSalaryData()).grid(row=3, column=2)









