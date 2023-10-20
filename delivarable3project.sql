CREATE TABLE Player (
    Player_ID INT PRIMARY KEY,
    Team_ID VARCHAR(4) REFERENCES Teams (Team_ID),
    Season_ID INT REFERENCES Seasons(Season_ID),
    Player_Name VARCHAR(45),
    Position VARCHAR(4),
    Minutes INT,
    Shots INT,
    ShotsOnGoal INT,
    Goals INT
);

SELECT * FROM Passes LIMIT 20;
-- Create the Teams table
CREATE TABLE Teams (
    Team_ID VARCHAR(4) PRIMARY KEY,
    Season_ID INT REFERENCES Seasons(Season_ID),
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
    Season_ID INT REFERENCES Seasons(Season_ID),
    GK_Name VARCHAR(45),
    Minutes INT,
    ShotsFaced INT,
    GoalsConceded INT,
    Saves INT
);

-- Create the Season table
CREATE TABLE Seasons (
    Season_ID INT PRIMARY KEY,
    Start_date DATE,
    End_date DATE
);

-- Create the Salaries table
CREATE TABLE Salaries (
    Player_ID INT PRIMARY KEY REFERENCES Player (Player_ID),
    Base_Salary DECIMAL(20, 2),
    Season_ID INT REFERENCES Seasons(Season_ID),
    GuaranteedCompensation DECIMAL(20, 2)
);

-- Create the Passes table
CREATE TABLE Passes (
    Player_ID INT REFERENCES Player (Player_ID),
    Season_ID INT REFERENCES Seasons(Season_ID),
    Minute INT,
    Passes INT, SCORE DECIMAL(10,2),
    Distance DECIMAL(10, 2),
    Vertical DECIMAL(10, 2)
);


