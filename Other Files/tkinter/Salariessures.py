
def func_InsertSalaryData():
    conn = psycopg2.connect(
        host="127.0.0.1",
        database='Project-Test',
        user='postgres',
        password='123qw123'
    )
    
    try:
        player_id = int(player_id_entry.get())
        base_salary = float(base_salary_entry.get())
        guaranteed_compensation = float(guaranteed_comp_entry.get())
        
        cursor = conn.cursor()
        QUERY = "INSERT INTO Salaries (Player_ID, Base_Salary, GuaranteedCompensation) VALUES (%s, %s, %s);"
        DATA = (player_id, base_salary, guaranteed_compensation)
        cursor.execute(QUERY, DATA)
        
        conn.commit()
        messagebox.showinfo("OK", "Data Successfully Inserted")
    
    except:
        messagebox.showerror("OPS", "Something went wrong. Please check the data")
    
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
        player_id = player_id_select.get()
        if player_id == "":
            messagebox.showerror("Error", "Please enter a Player ID to be selected")
        else:
            cursor = conn.cursor()
            DATA = int(player_id)
            QUERY = "SELECT * FROM Salaries WHERE Player_ID = %s"
            cursor.execute(QUERY, (DATA,))
            row = cursor.fetchall()
            
            Label(tabsalary, text="Base Salary").grid(row=2, column=2)
            LBaseSalary = Label(tabsalary, text=row[0][1])
            LBaseSalary.grid(row=2, column=3)
            Label(tabsalary, text="Guaranteed Compensation").grid(row=3, column=2)
            LGuaranteedComp = Label(tabsalary, text=row[0][2])
            LGuaranteedComp.grid(row=3, column=3)
        
        conn.commit()
    
    except:
        messagebox.showinfo("ALERT", "Something went wrong.")
    
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
        
        if player_id == "":
            messagebox.showerror("Error", "Please enter a Player ID to be updated")
        else:
            cursor = conn.cursor()
            DATA = (base_salary, guaranteed_compensation, int(player_id))
            QUERY = "UPDATE Salaries SET Base_Salary = %s, GuaranteedCompensation = %s WHERE Player_ID = %s"
            cursor.execute(QUERY, DATA)
            messagebox.showinfo("Success", "Data was updated")
    
    except:
        messagebox.showinfo("ALERT", "Something went wrong.")
    
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
            messagebox.showerror("Error", "Please enter a Player ID to be deleted")
        else:
            cursor = conn.cursor()
            DATA = (int(player_id),)
            QUERY = "DELETE FROM Salaries WHERE Player_ID = %s"
            cursor.execute(QUERY, DATA)
            messagebox.showinfo("Success", "Data was deleted")
        
        conn.commit()
    
    except:
        messagebox.showinfo("ALERT", "Something went wrong.")
    
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

Button(tabsalary, text="INSERT", width=20, command=lambda: func_InsertSalaryData()).grid(row=4, column=1)

# Select Widget
Create_l = Label(tabsalary, text="Select a Player's Salary")
Create_l.grid(row=0, column=2, pady=30, padx=30)

L4 = Label(tabsalary, text="Player_ID")
L4.grid(row=1, column=2)
player_id_select = Entry(tabsalary, bd=5)
player_id_select.focus_set()
player_id_select.grid(row=1, column=2)
Label(tabsalary, text="DATA").grid(row=1, column=3)

Button(tabsalary, text="Select", width=20, command=lambda: func_SelectSalaryData()).grid(row=4, column=2)

# Update an Entry widget to accept User Input for Salaries
Update_l = Label(tabsalary, text="Update a Player's Salary")
Update_l.grid(row=5, column=1, pady=30, padx=30)

Label(tabsalary, text="Player_ID").grid(row=6, column=0)
player_id_update = Entry(tabsalary, bd=5)
player_id_update.focus_set()
player_id_update.grid(row=6, column=1)

L2 = Label(tabsalary, text="Base Salary")
L2.grid(row=7, column=0)
base_salary_update = Entry(tabsalary, bd=5)
base_salary_update.focus_set()
base_salary_update.grid(row=7, column=1)

L3 = Label(tabsalary, text="Guaranteed Compensation")
L3.grid(row=8, column=0)
guaranteed_compensation_update = Entry(tabsalary, bd=5)
guaranteed_compensation_update.focus_set()
guaranteed_compensation_update.grid(row=8, column=1)

Button(tabsalary, text="SUBMIT", width=20, command=lambda: func_UpdateSalaryData()).grid(row=9, column=1)

# Delete Widget
Create_l = Label(tabsalary, text="Select a Player's Salary to be deleted")
Create_l.grid(row=5, column=2, pady=30, padx=30)

L4 = Label(tabsalary, text="Player_ID")
L4.grid(row=6, column=2)
player_id_delete = Entry(tabsalary, bd=5)
player_id_delete.focus_set()
player_id_delete.grid(row=6, column=2)

Button(tabsalary, text="Delete", width=20, command=lambda: func_DeleteSalaryData()).grid(row=9, column=2)


