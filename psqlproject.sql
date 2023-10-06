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

SELECT * FROM GoalKeepers;

SELECT * FROM Passes;




---- Indexes


--- C.R.U.D


----Create
INSERT INTO season(Season_ID, Start_date, End_date) VALUES (2023,'2023-01-01','2023-12-31');

---Read
SELECT p.Player_Name,ps.Distance FROM player p, passes ps where p.player_id=ps.player_id LIMIT 15;
--- update
UPDATE season SET Start_date=Start_date+15 WHERE Season_ID=2022;
SELECT * FROM Season;
--- Delete
DELETE FROM Season WHERE Season_ID=2023;

--- Create View
CREATE VIEW TOP15PlayerData AS
    SELECT player.Player_Name,player.Position,player.ShotsOnGoal,player.Goals,passes.Passes,Salaries.GuaranteedCompensation
    FROM player,passes,salaries
    where passes.Player_ID=player.Player_ID AND salaries.Player_ID=player.Player_ID AND player.Season_ID=2022
    ORDER BY GuaranteedCompensation DESC LIMIT 15;

SELECT * FROM TOP15PlayerData;


CREATE VIEW TEAM_BUDGET AS SELECT p.Team_ID,CAST(SUM(GuaranteedCompensation) AS money) AS Team_Budget FROM player p, salaries s WHERE s.player_id=p.player_id GROUP BY Team_ID ORDER BY Team_Budget DESC;

SELECT * FROM TEAM_BUDGET;

---- temporary tables ( Create and drop)

--- store procedure easily store values

--- function