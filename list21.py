#Programmed by- Shalvee Yadav
#Roll No.-60
#Practical No -21
'''A teacher stores marks of students in a list

marks = [78, 65, 89, 90, 56]

Write a program to:

Print all marks

Find total marks

Find average marks

Find highest marks

Find lowest marks'''
# List of marks
marks = [78, 65, 89, 90, 56]

# Print all marks
print("All Marks:")
for m in marks:
    print(m)

# Find total marks
total = 0
for m in marks:
    total += m

# Find average marks
average = total / len(marks)

# Find highest marks
highest = marks[0]
for m in marks:
    if m > highest:
        highest = m

# Find lowest marks
lowest = marks[0]
for m in marks:
    if m < lowest:
        lowest = m

print("Total Marks:", total)
print("Average Marks:", average)
print("Highest Marks:", highest)
print("Lowest Marks:", lowest)