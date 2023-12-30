-- Create a database MOVIE_DATABASE
CREATE database MOVIE_DATABASE;

-- In MOVIE_DATABASE,
use MOVIE_DATABASE;

-- a) Create a table MOVIE with below columns
-- Movie_ID with fixed length of 5
-- Movie_Name with variable length of 50
-- Type to store the type of movie with variable length of 20
-- Release_Date to store the release date.
-- Production_cost as integer to store the production cost in dollar.
-- Collection as integer to store the total collection in dollar.
-- Review as of type variable length string of 200, make the column to not allow null values
CREATE TABLE MOVIE (
    Movie_ID CHAR(5) PRIMARY KEY,
    Movie_Name VARCHAR(50),
    Type VARCHAR(20),
    Release_Date DATE,
    Production_Cost INT,
    Collection INT,
    Review VARCHAR(200) NOT NULL
);

-- b) After creating table make movie_id as primary key
ALTER TABLE MOVIE ADD PRIMARY KEY (Movie_ID);

-- c) Delete the column review of the table.
ALTER TABLE MOVIE DROP COLUMN Review;

-- d) Insert values in the Movie table to make table look below table.
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
