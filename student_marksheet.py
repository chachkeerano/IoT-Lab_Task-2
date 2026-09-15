# Program to create an advanced student marksheet

name = input("Enter student's name: ")
roll_no = input("Enter roll number: ")

subjects = ["Subject 1", "Subject 2", "Subject 3", "Subject 4", "Subject 5"]
marks = []

for subject in subjects:
    m = float(input(f"Enter marks for {subject} (out of 100): "))
    marks.append(m)

total_marks = sum(marks)
percentage = total_marks / len(subjects)

# Determine grade
if percentage >= 80:
    grade = "A+"
elif percentage >= 70:
    grade = "A"
elif percentage >= 60:
    grade = "B"
elif percentage >= 50:
    grade = "C"
elif percentage >= 40:
    grade = "D"
else:
    grade = "F"

# Check fail condition: any subject below 40 marks
failed_subject = any(m < 40 for m in marks)

if failed_subject or percentage < 40:
    result = "FAIL"
else:
    result = "PASS"

# Display marksheet
print("\n================ MARKSHEET ================")
print(f"Name       : {name}")
print(f"Roll No.   : {roll_no}")
print("---------------------------------------------")
for i in range(len(subjects)):
    print(f"{subjects[i]:<12}: {marks[i]}")
print("---------------------------------------------")
print(f"Total Marks : {total_marks} / {len(subjects) * 100}")
print(f"Percentage  : {percentage:.2f}%")
print(f"Grade       : {grade}")
print(f"Result      : {result}")
print("=============================================")
