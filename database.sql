-- Table to store student records
CREATE TABLE students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    course TEXT NOT NULL,
    marks INTEGER
);

-- Sample data for testing the system
INSERT INTO students (name, course, marks) VALUES
('Aman Sharma', 'Python', 85),
('Riya Patel', 'SQL', 90),
('Arjun Singh', 'Java', 78),
('Neha Gupta', 'Data Analytics', 92),
('Rahul Verma', 'Web Development', 88);
