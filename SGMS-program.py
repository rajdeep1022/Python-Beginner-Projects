# Student Grade Management System

def calculate_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 75:
        return "B"
    elif avg >= 60:
        return "C"
    elif avg >= 40:
        return "D"
    else:
        return "F"

print("Student Grade Management System")

name = input("Enter student name: ")

marks = []
for i in range(1, 6):
    mark = int(input(f"Enter marks for subject {i}: "))
    marks.append(mark)

average = sum(marks) / len(marks)
grade = calculate_grade(average)

print("\nStudent Report")
print("Name:", name)
print("Average Marks:", average)
print("Grade:", grade)
