#Programmed by- Shalvee Yadav
#Roll No.-60
#Practical No-23
''' 
 	
Marks of students are stored in a list.

marks = [78, 35, 90, 40, 55]

Write a program to:

Print PASS if marks ≥ 40

Print FAIL if marks < 40

Count how many students passed'''
# List of marks
marks = [78, 35, 90, 40, 55]

# Counter for passed students
pass_count = 0

# Check each mark
for m in marks:
    if m >= 40:
        print(m, "- PASS")
        pass_count += 1
    else:
        print(m, "- FAIL")

print("Number of students passed:", pass_count)