-- 1. Create a database MOVIE_DATABASE.
CREATE database MOVIE_DATABASE;

-- In MOVIE_DATABASE,
USE MOVIE_DATABASE;

-- a) Create a table MOVIE with below columns:
-- Movie_ID with fixed length of 5
-- Movie_Name with variable length of 50
-- Type to store the type of movie with variable length of 20
-- Release_Date to store the release date.
-- Production_cost as integer to store the production cost in dollar.
-- Collection as integer to store the total collection in dollar.
-- Review as of type variable length string of 200, make the column to not allow null values.
CREATE TABLE MOVIE (
    Movie_ID CHAR(5),
    Movie_Name VARCHAR(50),
    Type VARCHAR(20),
    Release_Date DATE,
    Production_Cost INT,
    Collection INT,
    Review VARCHAR(200) NOT NULL
);

-- b) After creating table make movie_id as primary key.
ALTER TABLE MOVIE ADD PRIMARY KEY (Movie_ID);

-- c) Delete the column review of the table.
ALTER TABLE MOVIE DROP COLUMN Review;

-- d) Insert values in the Movie table to make table look like below table.
-- Movie_ID   Movie_Name        Type        Release_Date   Production_Cost   Collection
-- M001       Oppenheimer       Biography   2023/07/21     100000000         951227645
-- M002       Swades            Drama       2004/11/07     240000            2000000
-- M003       The Dark Knight   Action      2008/07/18     185000000         1110000000
-- M004       Kung Fu Panda     Animation   2008/07/11     632000000         130000000
-- M005       Iron Man          Action      2008/05/01     585000000         140000000
-- M006       City of God       Action      2002/08/30     30000000          3000000
INSERT INTO MOVIE VALUES
    ('M001', 'Oppenheimer', 'Biography', '2023-07-21', 100000000, 951227645),
    ('M002', 'Swades', 'Drama', '2004-11-07', 240000, 2000000),
    ('M003', 'The Dark Knight', 'Action', '2008-07-18', 185000000, 1110000000),
    ('M004', 'Kung Fu Panda', 'Animation', '2008-07-11', 632000000, 130000000),
    ('M005', 'Iron Man', 'Action', '2008-05-01', 585000000, 140000000),
    ('M006', 'City of God', 'Action', '2002-08-30', 30000000, 3000000);


-- 2. Consider the MOVIE table and write the SQL queries based on it.
--    i. Display all information from movie.
SELECT * FROM MOVIE;

--   ii. Display the type of movies.
SELECT DISTINCT Type FROM MOVIE;

--  iii. Display movieid, moviename, total_earning by showing the business done by the movies.
--       Calculate the profit earned by movie using the difference of collection and production cost.
SELECT Movie_ID, Movie_Name, (Collection - Production_Cost) AS Profit FROM MOVIE;

--   iv. Display movieid, moviename and productioncost for all movies with productioncost 
--       greater than 135,000,000 and less than 960,000,000
SELECT Movie_ID, Movie_Name, Production_Cost FROM MOVIE
WHERE Production_Cost BETWEEN 135000000 AND 960000000;

--    v. Display the movie of type action and drama.
SELECT * FROM MOVIE WHERE Type IN ('Action', 'Drama');

--   vi. Display the list of movies which were released in May and July of year 2008
SELECT * FROM MOVIE
WHERE (MONTH(Release_Date) = 5 OR MONTH(Release_Date) = 7) AND YEAR(Release_Date) = 2008;


-- 3. Consider the MOVIE table and write query based on it.
--    i. Display the Year and maximum collection done among all the movies in that year.
SELECT YEAR(Release_Date) AS Year, MAX(Collection) AS Max_Collection
FROM MOVIE GROUP BY YEAR(Release_Date);

--   ii. Display type of the movie and total production cost of those types.
SELECT Type, SUM(Production_Cost) AS Total_Production_Cost
FROM MOVIE GROUP BY Type;

--  iii. Display the year and total movie released in those years.
SELECT YEAR(Release_Date) AS Year, COUNT(*) AS Total_Movies
FROM MOVIE GROUP BY YEAR(Release_Date);

--   iv. Display the maximum collection done by any movie in the database.
SELECT MAX(Collection) AS Max_Collection FROM MOVIE;


-- 4. Consider the movie table and write query based on it.
--    i. Change the movie_id of the all movies in lower case and which were released in year 2008
UPDATE MOVIE SET Movie_ID = LOWER(Movie_ID) WHERE YEAR(Release_Date) = 2008;

--   ii. Insert any new upcoming movie details in a new row providing all required 
--       values, this movie has not yet any collection value.
INSERT INTO MOVIE VALUES
    ('M007', 'Deadpool 3', 'Action', '2024-07-26', 250000000, NULL);

--  iii. Change the Collection column of all the movies to 100000 where collection is null.
UPDATE MOVIE SET Collection = 100000 WHERE Collection IS NULL;

--   iv. Delete all the movies whose name ends with ‘a’ and were released in 2008
DELETE FROM MOVIE WHERE YEAR(Release_Date) = 2008 AND RIGHT(Movie_Name, 1) = 'a';


-- 5. Consider the below Review table, write query based on Review and Movie Table.
-- Movie_ID(CHAR(5))   Rating(INT(2)   Total_Votes(INT)
-- M001                8               10000
-- M002                8               31000
-- M003                9               17000
-- M004                7               40000
-- M005                7               12000
-- M006                6               26000

--    i. Display the name and Rating of the movies which have got rating more than 7
SELECT M.Movie_Name, R.Rating
FROM Movie M JOIN Review R ON M.Movie_ID = R.Movie_ID
WHERE R.Rating > 7;

--   ii. Find out the rating and movie id of the movies which have collection more than 130000000
SELECT R.Movie_ID, R.Rating
FROM Review R JOIN Movie M ON R.Movie_ID = M.Movie_ID
WHERE M.Collection > 130000000;

--  iii. Find out the total collection of movies which have got rating more than 5 and
--       which were released after 2006
SELECT SUM(M.Collection) AS Total_Collection
FROM Movie M JOIN Review R ON M.Movie_ID = R.Movie_ID
WHERE R.Rating > 5 AND YEAR(M.Release_Date) > 2006;

--   iv. Find out all the rating and total collection of movies which got those ratings.
SELECT R.Rating, SUM(M.Collection) AS Total_Collection
FROM Review R JOIN Movie M ON R.Movie_ID = M.Movie_ID
GROUP BY R.Rating;
