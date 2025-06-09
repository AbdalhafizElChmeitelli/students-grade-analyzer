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

display_student_summary()