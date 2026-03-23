#Programmed by- Shalvee Yadav
#Roll No.-60
#Practical No-08
#Given a list of numbers 1-20, create a new list that contains only the even numbers.
# List of numbers from 1 to 20
numbers = list(range(1, 21))

# Create a new list with only even numbers
even_numbers = [num for num in numbers if num % 2 == 0]

print(even_numbers)