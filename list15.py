#Programmed by- Shalvee Yadav
#Roll No.-60
#Practical No-15
#A week's temperatures are stored in a list. Find how many days were "Hot" (above 35°C)
# List of temperatures for a week
temps = [32, 36, 38, 34, 37, 30, 39]

# Count hot days (above 35°C)
hot_days = 0

for t in temps:
    if t > 35:
        hot_days += 1

print("Number of Hot days:", hot_days)