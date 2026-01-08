num_students = int(input("How many students do you want to enter? "))

# Initialize empty lists to store our data
names = []
scores = []

for i in range(num_students):
    name = input("Enter student name: ")

    score = float(input("Enter test score (0-100): "))

    while score < 0 or score > 100:
        print("invalid score. Please enter a value between 0 and 100.")

        score = float(input("Enter test score (0-100)"))

    names.append(name)
    scores.append(score)

average_score = sum(scores) / len(scores)
highest_score = max(scores)
lowest_score = min(scores)

passed_students = []
failed_students = []

for i in range(len(scores)):
    if scores[i] >= 60:
        passed_students.append(names[i])
    else:
        failed_students.append(names[i])

# Getting the total number of students from the user, i.e (Collecting Student Data)

num_students = int(input("How many students do you want to enter? "))

names = []
scores = []

for i in range(num_students):
    print(f"\nStudent {i + 1}")
    name = input("Enter student name: ")

    score = float(input("Enter test score (0-100): "))

    while score < 0 or score > 100:
        print("Invalid score. Please enter a value between 0 and 100.")

        score = float(input("Enter test score (0-100)"))

    names.append(name)
    scores.append(score)

# Calculations
average_score = sum(scores) / len(scores)
highest_score = max(scores)
lowest_score = min(scores)

passed_students = []
failed_students = []

for i in range(len(scores)):
    if scores[i] >= 60:
        passed_students.append(names[i])
    else: 
        failed_students.append(names[i])

# Summary Report
print("\n----- SUMMARY REPORT -----")
print(f"Class Average Score: {average_score:.2f}")
print(f"Highest Score: {highest_score}")
print(f"Lowest Score: {lowest_score}")


print("\nStudents Who Passed:")
for student in passed_students:
    print(student)

print("\nStudents Who Failed:")
for student in failed_students:
    print(student)


