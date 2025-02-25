students = [("Alice", 20, 85), ("Bob", 22, 90), ("Charlie", 21, 80)]

for i in range(len(students)):
    for j in range(i + 1, len(students)):
        if students[i][2] > students[j][2]:
            students[i], students[j] = students[j], students[i]

print("Sorted Students by Grade:", students)
