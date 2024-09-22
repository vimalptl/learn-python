#Dictionary is similar to a JSON Object but not the same.
# Key / Value pair - key cannot be repeated.

"""
JSON Object example: [
                      {name: Vimal, phone: 1234567890}, 
                      {name:Vijayalakshmi, phone: 9876543210}
                     ]

Dictioary example: { "Vimal": { "phone": 1234567890, city: "Los angeles" }, 
                     "Vijayalakshmi": { "phone": 9876543210, city: "Manhattan Beach" }                  
                    }   
"""

contact = {}

#Add item in dictionary
contact['name'] = 'Vimal'   
contact['phone'] = 1234567890

contact['name'] = 'Vijayalakshmi'
contact['phone'] = [1234567890, 9876543210]

print(contact)

#Accessing values
print("Name: " + contact['name'])

#Delete item in dictionary
del contact['phone']
print(contact)
  