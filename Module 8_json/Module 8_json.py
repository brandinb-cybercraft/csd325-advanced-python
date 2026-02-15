# Brandi Butler
# CSD-325 Module 8 - JSON Practice
# Date: 02/15/2026


import json


# Function to print student list
def print_students(student_list):
    """
    Loops through the student list and prints each student
    in formatted output.
    """

    for student in student_list:
        print(f"{student['L_Name']}, {student['F_Name']} : "
              f"ID = {student['Student_ID']} , "
              f"Email = {student['Email']}")
    print()  # blank line for readability


# Load JSON file
with open("Student.json", "r") as file:
    students = json.load(file)


# Display original list
print("Original Student List:")
print_students(students)


# Append new student
new_student = {
    "F_Name": "Brandi",
    "L_Name": "Butler",
    "Student_ID": 99999,
    "Email": "bbutler@example.com"
}

students.append(new_student)


# Display updated list
print("Updated Student List:")
print_students(students)


# Write updated list back to JSON file
with open("Student.json", "w") as file:
    json.dump(students, file, indent=4)


print("The student.json file was successfully updated.")
