#Programmed by- Shalvee Yadav
#Roll No.-60
#Practical No-16
#Store marks of 5 students in a list and calculate the average marks.
# List of marks of 5 students
marks = [70, 85, 90, 60, 75]

# Calculate total
total = 0
for m in marks:
    total += m

# Calculate average
average = total / len(marks)

print("Average Marks:", average)