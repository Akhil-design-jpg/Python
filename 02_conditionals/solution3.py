student_grade_str = input("Enter student grade: ")

student_grade = int(student_grade_str)


if 90 <= student_grade<= 100:
    print("Grade A")

elif 80 <= student_grade <= 90:
    print("Grade B")

elif 70 <= student_grade <= 80:
    print("Grade C")

elif 60 <= student_grade <= 70:
    print("Grade D")

elif student_grade < 60:
    print("Grade F")

else:
    print("Wrong grading")
    exit()