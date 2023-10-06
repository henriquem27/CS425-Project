-- Create the Player table
CREATE TABLE Player (
    Player_ID INT AUTO_INCREMENT PRIMARY KEY,
    Team_ID INT,
    Player_Name VARCHAR(255),
    Position VARCHAR(255),
    Minutes INT,
    Shots INT,
    ShotsOnGoal INT,
    Goal INT
)

-- Create the Teams table
CREATE TABLE Teams (
    Team_ID INT AUTINCREMENT PRIMARY KEY,
    Player_Id INT,
    Games INT,
    ShotsFor INT,
    ShotsAgainst INT,
    GoalsFor INT,
    GoalsAgainst INT
)

-- Create the Games table
CREATE TABLE Games (
    date DATE,
    Team_ID INT,
    Hometeam VARCHAR(255),
    HomeGoals INT,
    Away VARCHAR(255),
    AwayGoals INT
);

-- Create the GoalKeepers table
CREATE TABLE GoalKeepers (
    Player_ID INT PRIMARY KEY,
    Team_ID INT,
    Player_Name VARCHAR(255),
    Season VARCHAR(255),
    Minutes INT,
    ShotsFaced INT,
    GoalConceded INT,
    Saves INT
);

-- Create the Season table
CREATE TABLE Season (
    Season_ID INT AUTO_INCREMENT PRIMARY KEY,
    Team_ID INT,
    Season VARCHAR(255),
    Start_date DATE,
    End_date DATE,
    teams TEXT -- You might want to provide more details on this field
)

-- Create the Salaries table
CREATE TABLE Salaries (
    Player_ID INT,
    Base_Salary DECIMAL(10, 2), -- Adjust the data type as needed
    GuaranteedCompensation DECIMAL(10, 2) -- Adjust the data type as needed
);

-- Create the Passes table
CREATE TABLE Passes (
    Player_ID INT,
    Minute INT,
    Passes INT,
    Distance DECIMAL(8, 2), -- Adjust the data type as needed
    Vertical DECIMAL(8, 2) -- Adjust the data type as needed
);

-- Create the Goals table
CREATE TABLE Goals (
    Player_ID INT,
    AssistingPlayerName VARCHAR(255),
    Scorer_Name VARCHAR(255),
    GoalKeeper_Name VARCHAR(255)
);
