#Programmed by- Shalvee Yadav
#Roll No.-60
#Practical No-10
#Given a list of 10 student marks, count how many students scored above 40.
# List of 10 student marks
marks = [35, 67, 45, 20, 80, 55, 39, 90, 42, 10]

# Count students who scored above 40
count = 0

for m in marks:
    if m > 40:
        count += 1

print("Number of students scoring above 40:", count)