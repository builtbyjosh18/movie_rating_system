# Today we will be building a Student Grades Tracker
students={"Alice":85,"John":56,"Bob":72,"Myers":56,
          "Alejandro":79
}

#Loop that allows new entries for grades
addStudent= False
while not addStudent:
    new_student= input("Please enter the name of the student you "
                      "want to add:")
    if new_student == "Stop":
        addStudent= True
    else:
        new_grade = int(input(f"Please enter {new_student}'s grade: "))
        students.update({new_student: new_grade})

#Function to print each student and their grade
def grade_printer():
    for student, grade in students.items():
          print(f" The student's name is {student}"
              f" and their grade is {grade}.")

#Function to calculate and print the average grade
def average_grade():
    total=0
    for g in students.values():
        total += g
    average = total/len(students)
    return average

#Testing the function
Grades= grade_printer()
print(Grades)

Avg=average_grade()
print(Avg)
