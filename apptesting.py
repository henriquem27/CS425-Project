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
from analytics import *

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
tabControl.add(tabanalytics, text='Explore the Database')

Label(tabhome, text="Major League Soccer Database GUI",
      font=('Arial', 30)).pack(padx=30, pady=10)
Label(tabhome, text="This GUI is connected to a Major league Soccer and Allows for C.R.U.D Operations",
      font=('Arial', 15)).pack(padx=30, pady=20)

# Usage Guidelines for the Home tab
usage_guidelines = """
Tabs Usage Guidelines (Scroll throw for details):\n
--> Seasons, Players, Goalkeepers, Teams, Salaries: CRUD operations for the respective tables.\n\n
--> Explore the Database: The GUI is organized into different sections such as "Data Exploration," "Team Section," 
  and "Player Section." Navigate through these sections to access various features.\n\n
--> Interacting with Listboxes: Use the listboxes for team and season selection. Click on items to select or deselect them. 
Employ the "Select All" and "Clear All Selections" buttons for convenience.\n\n
--> Executing Queries: Click on specific buttons like "Total Points by Season," "Team Budget," "Top Scorers," etc.,
to execute corresponding queries and view the results. Each button corresponds to a specific analytical feature.\n\n
--> Viewing Query Results: After clicking a button, a new window will pop up displaying the results of the executed query.
Explore the data presented in tables, allowing for easy analysis.\n\n
--> Error Handling: If an error occurs during the execution of a query, an error message will be displayed.
Ensure that you have made valid selections in the listboxes before running queries.\n\n
--> Closing Query Result Windows: Close the pop-up windows displaying query results after reviewing the information.
You can launch multiple windows simultaneously for different analyses.\n\n
--> Understanding Labels: Labels provide context for each section and button, helping you understand the purpose
of different elements in the GUI.\n\n
--> Preconditions: Ensure that the application is connected to the required database with relevant tables and data.
Consult documentation for any specific prerequisites.\n\n
--> Closing the Application: Close the application when finished by clicking the appropriate close or exit button.
This ensures proper termination of the application.
"""

text_widget = Text(tabhome, wrap="word", font=(
    'Arial', 12), height=100, width=100,relief='raised')
text_widget.pack(padx=30, pady=10)

# Bold subheadings
for line in usage_guidelines.split('\n'):
    if ':' in line:
        parts = line.split(':')
        text_widget.insert('end', parts[0] + ':', 'bold')
        if len(parts) > 1:
            text_widget.insert('end', parts[1] + '\n')
    else:
        text_widget.insert('end', line + '\n')

# Tag configuration for bold
text_widget.tag_configure('bold', font=('Arial', 12, 'bold'))

tabControl.pack(expand=1, fill="both")










generate_teamsanalytics(tabanalytics,root)





# call function to fill salary tab
generate_salary(tabsalary)


# call function to fill salary tab
generate_season(tabseason)

generate_player(tabplayer)

generate_gk(tabgk)

generate_teams(tabteams)

root.mainloop()
