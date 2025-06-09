student = []
grades = []
num_students = int(input("Enter the number of students: "))

def display_student_summary():
    for i in range(num_students):
        name = input("Enter student name: ")  
        grade = float(input("Enter student grade: "))
        if grade < 0 or grade > 100:
                print("Invalid grade. Please enter a grade between 0 and 100.")
        else:
            student.append(name)
            grades.append(grade)
        
    for j in range(num_students):
        
     print(student[j] + ": " + str(grades[j]))

def get_avg_grade(grades, num_students):
    x = 0
    for i in range(num_students):
        x += grades[i]
    y = x / num_students if num_students > 0 else 0
    print("Average grade: " + str(y))


display_student_summary()
get_avg_grade(grades, num_students)