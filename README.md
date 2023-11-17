
# Major League Soccer Database

Data on players, teams, goalkeepers, wages, seasons, etc. are all included in the database. It can be managed via an Interactive User Interface (UI) that can accomplish both basic CRUD operations and sophisticated OLAP procedures on the database.

Every table has its own CRUD on a designated tab, and the analytics tab may be used to carry out sophisticated SQL operations and analytics.




## Database

The database schemas are provided in `database.sql`, below is a demonstration for creating the Tables using the provided schemas.

#### Seasons Table

```http
CREATE TABLE Seasons ( Season_ID INT PRIMARY KEY, Start_date DATE, End_date DATE );
```

| Season_ID | Start_date     | End_date                |
| :-------- | :-------       | :---------------------- |
| `INT`     | `DATE`         | `DATE`                  |


## File Structure

```
CS425-Project
│   README.md
│   file001.txt    
│
└───folder1
│   │   file011.txt
│   │   file012.txt
│   │
│   └───subfolder1
│       │   file111.txt
│       │   file112.txt
│       │   ...
│   
└───folder2
    │   file021.txt
    │   file022.txt
```

## Environment Variables

To run this project, you will need to Setup the Database and add the Database Name, Username and Password of your Database in the `connection.py`

`database='Project-Test'`

`user='User_name'`

`password='Password'`


## Running the GUI

After setting up the database, run the following command in the terminal to open and use the GUI.

```python
python3 MLS.py
```


## GUI

![Seasons Tab](https://via.placeholder.com/468x300?text=App+Screenshot+Here)

![Analytics Tab](https://via.placeholder.com/468x300?text=App+Screenshot+Here)
## Demo

Insert gif or link to demo

