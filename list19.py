#Programmed by- Shalvee Yadav
#Roll No.-60
#Practical No-19
# A teacher stored attendance of students in a list (1 = present, 0 = absent).
#Example: [1,1,0,1,0,1,1]
#Write a program to:
#Count total present
#Count total absent
#Print attendance percentage
attendance=[1,1,0,1,0,1,1]
present=attendance.count(1)
abssent=attendance.count(0)
persentage=present/len(attendance)*100
print(present)
print(abssent)
print(persentage)
