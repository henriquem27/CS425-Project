-- Create the Player table
CREATE TABLE Player (
    Player_ID SERIAL PRIMARY KEY,
    Team_ID INT REFERENCES Teams (Team_ID),
    Player_Name VARCHAR(255),
    Position VARCHAR(255),
    Minutes INT,
    Shots INT,
    ShotsOnGoal INT,
    Goals INT
);

-- Create the Teams table
CREATE TABLE Teams (
    Team_ID SERIAL PRIMARY KEY,
    Games INT,
    ShotsFor INT,
    ShotsAgainst INT,
    GoalsFor INT,
    GoalsAgainst INT
);

-- Create the Games table
CREATE TABLE Games (
    GameID SERIAL Primary KEY,
    Date DATE,
    Team_ID INT REFERENCES Teams (Team_ID),
    HomeTeam VARCHAR(255),
    HomeGoals INT,
    Away VARCHAR(255),
    AwayGoals INT
);

-- Create the GoalKeepers table
CREATE TABLE GoalKeepers (
    Player_ID SERIAL PRIMARY KEY,
    Team_ID INT REFERENCES Teams (Team_ID),
    Player_Name VARCHAR(255),
    Season VARCHAR(255),
    Minutes INT,
    ShotsFaced INT,
    GoalsConceded INT,
    Saves INT
);

-- Create the Season table
CREATE TABLE Season (
    Season_ID SERIAL PRIMARY KEY,
    Team_ID INT REFERENCES Teams (Team_ID),
    Season VARCHAR(255),
    Start_date DATE,
    End_date DATE
);

-- Create the Salaries table
CREATE TABLE Salaries (
    Player_ID INT PRIMARY KEY REFERENCES Player (Player_ID),
    Base_Salary DECIMAL(10, 2),
    GuaranteedCompensation DECIMAL(10, 2)
);

-- Create the Passes table
CREATE TABLE Passes (
    Player_ID INT REFERENCES Player (Player_ID),
    Minute INT,
    Passes INT,
    Distance DECIMAL(10, 2),
    Vertical DECIMAL(10, 2)
);

-- Create the Goals table
CREATE TABLE Goals (
    Player_ID INT PRIMARY KEY REFERENCES Player (Player_ID),
    AssistingPlayerName VARCHAR(255),
    Scorer_Name VARCHAR(255),
    GoalKeeper_Name VARCHAR(255)
);
--- C.R.U.D


----Create

---Read

--- update

--- Delete


--- Create View



