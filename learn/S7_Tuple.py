# Immutable List - Cannot be changed once created.
# you can delete a tuple with del statement

daysOfWeek = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
print(daysOfWeek)

weeks = list(daysOfWeek)
weeks[1] = "TuesdayMaybe"
print(weeks)

print("daysOfWeek type: " + str(type(daysOfWeek)))
print("weeks type: " + str(type(weeks)))

def high_and_low(numbers):
    """Determines the highest and lowest number from a list of numbers."""
    return max(numbers), min(numbers)   

lottery_numbers = [4, 8, 15, 16, 23, 42]
(highest, lowerst) = high_and_low(lottery_numbers)
print("Highest: " + str(highest) + " Lowest: " + str(lowerst))

#Tuple assignment in for loop
contacts = [("Vimal", 1234567890), ("Vijayalakshmi", 9876543210)]
for (name, phone) in contacts:
    print("Name: " + name + " Phone: " + str(phone))

