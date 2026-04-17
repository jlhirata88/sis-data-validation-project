import sqlite3

def print_results(title, rows):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)
    if rows:
        for row in rows:
            print(row)
    else:
        print("No results found.")

conn = sqlite3.connect("school.db")
cursor = conn.cursor()

# 1. Find students with missing emails
cursor.execute("""
SELECT * FROM students
WHERE email IS NULL
""")
missing_emails = cursor.fetchall()
print_results("Students with Missing Emails", missing_emails)

# 2. Find duplicate student names
cursor.execute("""
SELECT name, COUNT(*) as duplicate_count
FROM students
GROUP BY name
HAVING COUNT(*) > 1
""")
duplicate_students = cursor.fetchall()
print_results("Duplicate Student Names", duplicate_students)

# 3. Find missing grade scores
cursor.execute("""
SELECT * FROM enrollments
WHERE grade_score IS NULL
""")
missing_grades = cursor.fetchall()
print_results("Enrollments with Missing Grades", missing_grades)

# 4. Student performance report
cursor.execute("""
SELECT s.name, c.course_name, e.grade_score
FROM students s
JOIN enrollments e ON s.student_id = e.student_id
JOIN courses c ON e.course_id = c.course_id
""")
student_report = cursor.fetchall()
print_results("Student Performance Report", student_report)

# 5. Average grade per student
cursor.execute("""
SELECT s.name, AVG(e.grade_score) as avg_grade
FROM students s
JOIN enrollments e ON s.student_id = e.student_id
GROUP BY s.name
""")
average_grades = cursor.fetchall()
print_results("Average Grade Per Student", average_grades)

conn.close()