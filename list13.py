#Programmed by- Shalvee Yadav
#Roll No.-60
#Practical No-13
#Create a list of ages. Create two new lists: minors (under 18) and adults (18 and above)
# List of ages
ages = [12, 25, 17, 18, 30, 15, 22]

# Create two lists
minors = []
adults = []

# Separate ages
for age in ages:
    if age < 18:
        minors.append(age)
    else:
        adults.append(age)

print("Minors:", minors)
print("Adults:", adults)
