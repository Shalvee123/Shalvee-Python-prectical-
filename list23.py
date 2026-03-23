#Programmed by- Shalvee Yadav
#Roll No.-60
#Practical No-23
'''A cricket player scored runs in 6 matches.
Example: [45, 60, 10, 80, 55, 90]

Write a program to:

Find total runs

Find highest score

Count how many matches player scored more than 50 runs'''
# Runs scored in 6 matches
runs = [45, 60, 10, 80, 55, 90]

# Total runs
total = 0
for r in runs:
    total += r

# Highest score
highest = runs[0]
for r in runs:
    if r > highest:
        highest = r

# Count matches with more than 50 runs
count = 0
for r in runs:
    if r > 50:
        count += 1

print("Total Runs:", total)
print("Highest Score:", highest)
print("Matches with >50 runs:", count)