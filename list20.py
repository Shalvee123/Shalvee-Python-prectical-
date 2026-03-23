#Programmed by- Shalvee Yadav
#Roll No.-60
#Practical No-20
#A cricket player scored runs in 6 matches.
'''Example: [45, 60, 10, 80, 55, 90]
Find:

Total runs

Highest score'''
# Runs scored in 6 matches
runs = [45, 60, 10, 80, 55, 90]

# Calculate total runs
total = 0
for r in runs:
    total += r

# Find highest score
highest = runs[0]
for r in runs:
    if r > highest:
        highest = r

print("Total Runs:", total)
print("Highest Score:", highest)