import sqlite3

# Connect to SQLite database (creates file if it doesn't exist)
conn = sqlite3.connect("students.db")
cursor = conn.cursor()

# Create table to store student records if not already present
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    course TEXT NOT NULL,
    marks INTEGER
)
""")

conn.commit()


# Function to add a new student record
def add_student(name, course, marks):
    cursor.execute(
        "INSERT INTO students (name, course, marks) VALUES (?, ?, ?)",
        (name, course, marks)
    )
    conn.commit()
    print("Student added successfully")


# Function to display all student records
def view_students():
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()

    # Loop through and print each record
    for row in rows:
        print(row)


# Function to update student marks using ID
def update_marks(student_id, marks):
    cursor.execute(
        "UPDATE students SET marks=? WHERE id=?",
        (marks, student_id)
    )
    conn.commit()
    print("Student updated successfully")


# Function to delete a student record using ID
def delete_student(student_id):
    cursor.execute("DELETE FROM students WHERE id=?", (student_id,))
    conn.commit()
    print("Student deleted successfully")


# ---------------- MAIN MENU ----------------
# Simple CLI menu for user interaction
while True:
    print("\n--- Student Data Management System ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Marks")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter Name: ")
        course = input("Enter Course: ")
        marks = int(input("Enter Marks: "))
        add_student(name, course, marks)

    elif choice == "2":
        view_students()

    elif choice == "3":
        student_id = int(input("Enter Student ID: "))
        marks = int(input("Enter New Marks: "))
        update_marks(student_id, marks)

    elif choice == "4":
        student_id = int(input("Enter Student ID: "))
        delete_student(student_id)

    elif choice == "5":
        print("Exiting system...")
        break

    else:
        print("Invalid choice. Please try again.")

# Close database connection when program ends
conn.close()
