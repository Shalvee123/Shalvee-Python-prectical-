#Programmed by- Shalvee Yadav
#Roll No.-60
#Practical No-11
#Take a list like [-5, 3, -2, 8]. Create a new list where all negative numbers are converted to positive.
# List of 10 student marks
# Given list
numbers = [-5, 3, -2, 8]

# Convert all negative numbers to positive
positive_numbers = [abs(num) for num in numbers]

print(positive_numbers)
