#Programmed by- Shalvee Yadav
#Roll No.-60
#Practical No-05
#Create a list of 10 random integers. Use a for loop to print each number multiplied by 2.
import random

numbers = [random.randint(1, 100) for _ in range(10)]

for num in numbers:
 print(num * 2)