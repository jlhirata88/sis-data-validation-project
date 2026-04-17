import sqlite3

# Connect to database (creates school.db if it does not exist)
conn = sqlite3.connect("school.db")
cursor = conn.cursor()

# Drop tables if they already exist so you can re-run this script cleanly
cursor.execute("DROP TABLE IF EXISTS enrollments")
cursor.execute("DROP TABLE IF EXISTS students")
cursor.execute("DROP TABLE IF EXISTS courses")

# Create students table
cursor.execute("""
CREATE TABLE students (
    student_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    grade_level INTEGER,
    email TEXT
)
""")

# Create courses table
cursor.execute("""
CREATE TABLE courses (
    course_id INTEGER PRIMARY KEY,
    course_name TEXT NOT NULL
)
""")

# Create enrollments table
cursor.execute("""
CREATE TABLE enrollments (
    enrollment_id INTEGER PRIMARY KEY,
    student_id INTEGER,
    course_id INTEGER,
    grade_score INTEGER,
    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (course_id) REFERENCES courses(course_id)
)
""")

# Insert sample student data
students_data = [
    (1, "Alice Johnson", 10, "alice@email.com"),
    (2, "Bob Smith", 11, None),  # Missing email
    (3, "Charlie Brown", 10, "charlie@email.com"),
    (4, "Alice Johnson", 10, "duplicate@email.com"),  # Duplicate name
    (5, "Diana Prince", 12, "diana@email.com")
]

cursor.executemany("""
INSERT INTO students (student_id, name, grade_level, email)
VALUES (?, ?, ?, ?)
""", students_data)

# Insert sample course data
courses_data = [
    (1, "Math"),
    (2, "Science"),
    (3, "English")
]

cursor.executemany("""
INSERT INTO courses (course_id, course_name)
VALUES (?, ?)
""", courses_data)

# Insert sample enrollment data
enrollments_data = [
    (1, 1, 1, 85),
    (2, 2, 1, None),   # Missing grade
    (3, 3, 2, 90),
    (4, 4, 1, 70),
    (5, 5, 3, 95)
]

cursor.executemany("""
INSERT INTO enrollments (enrollment_id, student_id, course_id, grade_score)
VALUES (?, ?, ?, ?)
""", enrollments_data)

conn.commit()
conn.close()

print("Database created successfully as school.db")