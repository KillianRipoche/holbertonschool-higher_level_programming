-- Create the table force_name if it doesn't already exist, with id and name columns
CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL
);
