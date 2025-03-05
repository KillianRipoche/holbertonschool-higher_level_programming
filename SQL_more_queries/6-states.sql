-- Create the database hbtn_0d_usa if it doesn't already exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Select the database hbtn_0d_usa
USE hbtn_0d_usa;

-- Create the table states if it doesn't already exist with an auto-generated, non-null, unique primary key for id
CREATE TABLE IF NOT EXISTS states (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
