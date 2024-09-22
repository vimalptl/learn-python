from datetime import date

# Get today's date
todaysDate = date.today()
# Print today's date
print("Today's date:", todaysDate)

#variable

double = "She said, \"Hello, World!\""
single = 'She said, "Hello, World!"'
print (double)
print (single)

# Len() and print() functions
fruit = "apple"
fruit_length = len(fruit)
print(fruit_length)
print(fruit.upper())

# Concatenation
print("Hello" + " " + "World")

print('-'*10 + 'Python' + ' happy ' *10)

#formatting string
print('{} {} {}'.format('a', 'b', 'c'))
print('{1} {2} {0}'.format('a', 'b', 'c'))

print('{0:8} | {1:8} | {2:>8} | {3:8}'.format('Fruit', 'Color', 'Count', 'Quantity'))
print('{0:8} | {1:8} | {2:8} | {3:<8.2f}'.format('Apple', 'Red', 3, 2.33))

# Input
name = input("Enter your name: ")
print("Hello, " + name)
