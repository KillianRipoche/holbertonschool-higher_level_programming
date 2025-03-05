-- Create the table unique_id if it doesn't already exist, with id as an INT column with a default value of 1 and a unique constraint
CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);
