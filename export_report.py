import sqlite3
import csv

conn = sqlite3.connect("school.db")
cursor = conn.cursor()

cursor.execute("""
SELECT s.name, c.course_name, e.grade_score
FROM students s
JOIN enrollments e ON s.student_id = e.student_id
JOIN courses c ON e.course_id = c.course_id
""")

rows = cursor.fetchall()

with open("student_performance_report.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Student Name", "Course Name", "Grade Score"])
    writer.writerows(rows)

conn.close()

print("CSV report exported successfully.")