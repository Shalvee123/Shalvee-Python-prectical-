#Programmed by- Shalvee Yadav
#Roll No.-60
#Practical No-17
#Store temperatures of 7 days in a list and find the highest temperature.
temps = [32, 36, 38, 34, 37, 30, 39]

# Find highest temperature
highest = temps[0]

for t in temps:
    if t > highest:
        highest = t

print("Highest Temperature:", highest)