#Programmed by- Shalvee Yadav
#Roll No.-60
#Practical No-14
#Store prices of 5 items in a list. Calculate the total bill and the average price per item.
# List of prices of 5 items
prices = [100, 250, 75, 300, 150]

# Calculate total bill
total = 0
for price in prices:
    total += price

# Calculate average price
average = total / len(prices)

print("Total Bill:", total)
print("Average Price:", average)
