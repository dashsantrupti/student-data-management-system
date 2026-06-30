-- Table to store student records
CREATE TABLE students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    course TEXT NOT NULL,
    marks INTEGER
);

-- Sample data for testing the system
INSERT INTO students (name, course, marks) VALUES ('Aman', 'Python', 85);
INSERT INTO students (name, course, marks) VALUES ('Riya', 'SQL', 90);
