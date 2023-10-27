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


---- Top 10 goalkeepers in the league all time;

SELECT GK_Name,Season_ID,concat(round(cast(Saves as DECIMAL)/cast(ShotsFaced as decimal)*100),'%') as RATIO_GOALSSAVED from goalkeepers WHERE ShotsFaced>100 GROUP BY Season_ID, concat(round(cast(Saves as DECIMAL)/cast(ShotsFaced as decimal)*100),'%'), GK_Name ORDER BY RATIO_GOALSSAVED DESC LIMIT 10;


---- Top 10 Strikers in 2022 based on goals/shotsongoal;

SELECT Player_Name,ShotsOnGoal,Goals
     ,concat(round(cast(goals as decimal)/cast(shotsongoal as decimal)*100,2),'%') AS Ratio_GoalsVSShotsonGoal FROM player WHERE Season_ID=2022 AND minutes>1000 AND Position='ST' order by Ratio_GoalsVSShotsonGoal DESC limit 10;

---- Best scoring positions
SELECT Position,CONCAT(ROUND(cast(percent_rank() OVER (ORDER BY SUM(Goals)) as DECIMAL),2)*100,'%') as Position_Rank FROM Player WHERE NOT Position='GK' GROUP BY Position;

---- 2021 Nonscorers Percentage

Select concat(ROUND(cast(count(*) as DECIMAL)*100/(Select cast(count(*) as decimal)from Player WHERE Season_ID=2021),2),'%') as
NONSCORERS from Player where Goals=0 AND Season_ID=2021;

---- Top team score from the past seasons
SELECT Season_ID,MAX(Points) as Max,Team FROM teams GROUP BY Season_ID,Team_ID order by Max DESC LIMIT 3;

---

SELECT team,season_id,Team_Budget,SUM(Team_Budget) OVER (partition by team ORDER BY season_id) as RunningTotalBudget FROM team_budget;


-- Cumulative distribution

SELECT Position, cume_dist() OVER (ORDER BY AVG(Score)) as AVG_CUME_DIST_PASSING_SCORE FROM Player,Passes where Passes.Player_ID=Player.Player_ID group by Position;

-- Highest Aggregate Score games
SELECT Home_Team_ID,Away_team_ID,MAX(HomeGoals+AwayGoals) as Total_Goals_Scored FROM Games GROUP BY Home_Team_ID, Away_team_ID ORDER BY Total_Goals_Scored DESC LIMIT 15 ;

--- Biggest Home Supporter Disapointment
SELECT Home_Team_ID,HomeGoals,AwayGoals,Games.HomeGoals-Games.AwayGoals as GoalDif FROM games WHERE AwayGoals>HomeGoals order by GoalDif LIMIT 1;

--- Lowest points scored in a Season

SELECT Team,Season_ID,MIN(Points) as points FROM Teams GROUP BY Team, Season_ID order by points LIMIT 1;

----- Least minutes played vs Most minutes played

SELECT MIN(Minutes) as Least_Played, MAX(minutes) as Most_Played From player;


SELECT  cast(MIN(Base_Salary) as money) as Lowest_Salary, cast(MAX(Base_Salary) as money) as Highest_Salary From salaries;


--- MOVING AVG

SELECT date,homegoals+games.awaygoals as Total_Goals,AVG(homegoals+games.awaygoals) OVER (ORDER BY Date ROWS BETWEEN 3 PRECEDING AND 3 FOLLOWING) as Moving_AVG_7_Day FROM Games LIMIT 20;



SELECT * FROM Seasons;
