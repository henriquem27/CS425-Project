-- Create the Player table
CREATE TABLE Player (
    Player_ID INT PRIMARY KEY,
    Team_ID VARCHAR(4) REFERENCES Teams (Team_ID),
    Season_ID INT REFERENCES Season(Season_ID),
    Player_Name VARCHAR(255),
    Position VARCHAR(255),
    Minutes INT,
    Shots INT,
    ShotsOnGoal INT,
    Goals INT
);

-- Create the Teams table
CREATE TABLE Teams (
    Team_ID VARCHAR(4) PRIMARY KEY,
    Season_ID INT REFERENCES Season(Season_ID),
    GamesPlayed INT,
    ShotsFor INT,
    ShotsAgainst INT,
    GoalsFor INT,
    GoalsAgainst INT,
    Points INT
);

-- Create the Games table home team id
CREATE TABLE Games (
    GameID SERIAL Primary KEY,
    Date DATE,
    Home_Team_ID VARCHAR(4) REFERENCES Teams (Team_ID),
    HomeGoals INT,
    Away_team_ID VARCHAR(4) REFERENCES Teams (Team_ID),
    AwayGoals INT
);

-- Create the GoalKeepers table
CREATE TABLE GoalKeepers (
    GK_ID INT PRIMARY KEY,
    Team_ID VARCHAR(4) REFERENCES Teams (Team_ID),
    Season_ID INT REFERENCES Season(Season_ID),
    GK_Name VARCHAR(255),
    Minutes INT,
    ShotsFaced INT,
    GoalsConceded INT,
    Saves INT
);

-- Create the Season table
CREATE TABLE Season (
    Season_ID INT PRIMARY KEY,
    Start_date DATE,
    End_date DATE
);

-- Create the Salaries table
CREATE TABLE Salaries (
    Player_ID INT PRIMARY KEY REFERENCES Player (Player_ID),
    Base_Salary DECIMAL(10, 2),
    Season_ID INT REFERENCES Season(Season_ID),
    GuaranteedCompensation DECIMAL(10, 2)
);

-- Create the Passes table
CREATE TABLE Passes (
    Player_ID INT REFERENCES Player (Player_ID),
    Season_ID INT REFERENCES Season(Season_ID),
    Minute INT,
    Passes INT, SCORE DECIMAL(10,2),
    Distance DECIMAL(10, 2),
    Vertical DECIMAL(10, 2)
);


INSERT INTO season(Season_ID, Start_date, End_date) VALUES (2022,'2022-01-01','2022-12-31');

SELECT * FROM Teams;
---- Indexes


--- C.R.U.D


----Create

---Read

--- update

--- Delete


--- Create View

---- temporary tables ( Create and drop)

--- store procedure easily store values

--- function