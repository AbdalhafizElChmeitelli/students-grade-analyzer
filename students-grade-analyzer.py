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

def get_heighest_grade(grades, num_students):
    if num_students == 0:
        return None
    highest = 0
    for i in range(num_students):
        if grades[i] > highest:
            highest = grades[i]
    return highest


def count_passed(passed, num_students):
    count = 0
    for i in range(num_students):
        if passed[i] >= 60:
            count += 1
    return count


display_student_summary()
get_avg_grade(grades, num_students)
get_heighest_grade(grades, num_students)
highest = get_heighest_grade(grades, num_students)
for i in range(num_students):
    if grades[i] == highest:
        print("Student with highest grade: " + student[i] + " with grade: " + str(highest))
count_passed(grades, num_students)
print("Number of students who passed: " + str(count_passed(grades, num_students)))