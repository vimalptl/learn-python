#booleans
a=True
b=False
print('a==b: {}'.format(a == b))
print('a!=b: {}'.format(a != b))

#Comparators
""" and or not are boolean operators"""
print('37 > 39 and 37 < 40: {}'.format(37 > 39 and 37 < 40))

#Order of operations
print("not and or, () are evaluated first")
#code blocks
#conditional statements

age = input("Type an age between 37 and 50: ")
age = int(age)
if (age < 40): 
    print("{} < 40".format(age))
    print("{} is less than 40".format(age) if age < 40 else "{} is less than 40")
elif (age >= 40 and age <= 45):
    print("{} >= 40 and {} <= 45".format(age, age))
else:
    print("{} > 45".format(age))
    print("{} is greater than 45".format(age))
print("Have a nice day!")

