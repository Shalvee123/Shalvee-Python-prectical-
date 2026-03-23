
#Programmed by- Shalvee Yadav
#Roll No.-60
#Practical No-09
#Write a program that takes a list of names and a "search_name" from the user. Print the index where the name is found, or "Not Found."
# List of names
names = ["Aman", "Riya", "Sohan", "Neha", "Kunal"]

# Take input from user
search_name = input("Enter name to search: ")

# Check and print index
if search_name in names:
    print("Found at index:", names.index(search_name))
else:
    print("Not Found")