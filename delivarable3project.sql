-- Create the Season table
CREATE TABLE Seasons (
    Season_ID INT PRIMARY KEY,
    Start_date DATE,
    End_date DATE
);


-- Create the Teams table
CREATE TABLE Teams (
    Team_ID VARCHAR(30) PRIMARY KEY,
    Season_ID INT REFERENCES Seasons(Season_ID),
    Team VARCHAR(4),
    GamesPlayed INT,
    ShotsFor INT,
    ShotsAgainst INT,
    GoalsFor INT,
    GoalsAgainst INT,
    Points INT
);


CREATE TABLE Player (
    Player_ID VARCHAR(100) PRIMARY KEY,
    Team_ID VARCHAR(30) REFERENCES Teams (Team_ID),
    Season_ID INT REFERENCES Seasons(Season_ID),
    Player_Name VARCHAR(45),
    Position VARCHAR(4),
    Minutes INT,
    Shots INT,
    ShotsOnGoal INT,
    Goals INT
);



-- Create the Games table home team id
CREATE TABLE Games (
    GameID SERIAL Primary KEY,
    Date DATE,
    Home_Team_ID VARCHAR(30) REFERENCES Teams (Team_ID),
    HomeGoals INT,
    Away_team_ID VARCHAR(30) REFERENCES Teams (Team_ID),
    AwayGoals INT
);

-- Create the GoalKeepers table
CREATE TABLE GoalKeepers (
    GK_ID VARCHAR(100) PRIMARY KEY,
    Team_ID VARCHAR(30) REFERENCES Teams (Team_ID),
    Season_ID INT REFERENCES Seasons(Season_ID),
    GK_Name VARCHAR(45),
    Minutes INT,
    ShotsFaced INT,
    GoalsConceded INT,
    Saves INT
);



-- Create the Salaries table
CREATE TABLE Salaries (
    Player_ID VARCHAR(100) PRIMARY KEY REFERENCES Player (Player_ID),
    Base_Salary DECIMAL(20, 2),
    Season_ID INT REFERENCES Seasons(Season_ID),
    GuaranteedCompensation DECIMAL(20, 2)
);

-- Create the Passes table
CREATE TABLE Passes (
    Player_ID VARCHAR(100) REFERENCES Player (Player_ID),
    Season_ID INT REFERENCES Seasons(Season_ID),
    Passes INT, SCORE DECIMAL(10,2),
    Distance DECIMAL(10, 2),
    Vertical DECIMAL(10, 2)
);

INSERT INTO seasons(Season_ID, Start_date, End_date) VALUES (2022,'2022-01-01','2022-12-31');
INSERT INTO seasons(Season_ID, Start_date, End_date) VALUES (2021,'2021-01-01','2021-12-31');
INSERT INTO seasons(Season_ID, Start_date, End_date) VALUES (2023,'2023-01-01','2023-12-31');


--- Team Budget view
CREATE VIEW TEAM_BUDGET AS SELECT t.team,p.Team_ID,p.season_id,CAST(SUM(GuaranteedCompensation) AS money) AS Team_Budget FROM player p, salaries s, teams t WHERE s.player_id=p.player_id AND p.team_id=t.team_id GROUP BY p.Team_ID,p.Season_ID,t.team ORDER BY Team_Budget DESC;

select * from team_budget;
--- Team Budgets by Season with totals
SELECT season_id,team,SUM(team_budget) As Total_Budget from team_budget GROUP BY CUBE(season_id,team) ORDER BY (team,season_id);

SELECT Team,Season_ID,SUM(Points) FROM teams WHERE team IN ('ATL','MIA')GROUP BY ROLLUP(Team,Season_ID) ORDER BY Team,Season_ID;


CREATE VIEW Team_Rosters_By_Season AS SELECT t.team,p.season_id,p.Player_Name FROM player p, salaries s, teams t WHERE s.player_id=p.player_id AND p.team_id=t.team_id ORDER BY Team,Season_ID;

select * from team_rosters_by_season where Team='ATL';

--- Player Rank by Salary
SELECT t.Team, p.Player_Name,dense_rank() OVER (PARTITION BY t.Team ORDER BY s.GuaranteedCompensation DESC) as Dense_Rank  FROM Teams t ,Salaries s ,Player p WHERE s.Season_ID=2022 AND p.Player_ID=S.Player_ID AND p.Team_ID=t.team_id order by Team;

---- HomexAway Perfomance per season for all teams

SELECT x.Team,x.Season_ID as Season,x.HomeAVG,y.AwayAvg, X.HomeAVG-y.AwayAvg as AVG_GOAL_DIFFERENTIAl FROM (SELECT t.team,ROUND(AVG(g.Homegoals),4) as HomeAVG,Season_ID,g.home_team_id FROM teams t,games g WHERE t.team_id=g.home_team_id  GROUP BY t.team_id,g.home_team_id ORDER BY Team_ID) as x,
              (SELECT t.team,ROUND(AVG(g.AwayGoals),4) as AwayAvg,Season_ID,g.away_team_id FROM teams t,games g WHERE t.team_id=g.away_team_id GROUP BY t.team_id,g.away_team_id ORDER BY Team_ID) as y
         WHERE x.Home_Team_ID=y.Away_team_ID;
