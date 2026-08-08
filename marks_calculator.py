# Q1 - Marks Calculator
# Fixed version with input validation

marks = []

for i in range(5):
    while True:
        try:
            mark = int(input(f"Enter marks of student {i + 1}: "))

            if mark < 0 or mark > 100:
                print("Please enter marks between 0 and 100.")
                continue

            marks.append(mark)
            break

        except ValueError:
            print("Invalid input! Please enter a number.")

total = sum(marks)
average = total / len(marks)
highest = max(marks)
lowest = min(marks)

print("\nMarks Result")
print("Total Marks =", total)
print("Average Marks =", average)
print("Highest Marks =", highest)
print("Lowest Marks =", lowest)