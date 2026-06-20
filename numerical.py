# Teacher enters the correct answer
teacher_answer = float(input("Teacher: Enter the correct answer: "))

# Student enters their answer
student_answer = float(input("Student: Enter your answer: "))

# Round both values to 1 decimal place
teacher_rounded = round(teacher_answer, 1)
student_rounded = round(student_answer, 1)

# Compare
if teacher_rounded == student_rounded:
    print("Correct answer ✅")
else:
    print("Wrong answer ❌")
