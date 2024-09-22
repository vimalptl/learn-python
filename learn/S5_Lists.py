#List
nameList = ["Vimal", "Vijay", "Vijayalakshmi"]
print(nameList)
print("First Name in the List: " + nameList[0])
nameList[0] = "Vimala"
print("Update First Name in the List: " + nameList[0])
nameList.append("Vidhika")
nameList.extend(["Sabri",'Sami'])
print("Appended list, then Extended with 2 Names: {} ".format(nameList))
nameList.insert(0, "James")
print("Inserted James into into List at index 0: {} ".format(nameList)) 

#Slices
#from index 1 to 3, if you are doing first 2 then 0:2 or :2
someNameList = nameList[1:3] 
print ("Sliced List: {} ".format(someNameList))
lastThreeNames = nameList[-3:]
print("Last 3 Names: {} ".format(lastThreeNames))
charfromString = 'Horse'[1:3]
print("Chars from String: {} ".format(charfromString))

#Exception Handling
try :
    nameIndex = nameList.index('Vimala') 
except ValueError:
    print("Index Error: Name not found in list")
else:       
    print("Index: " + str(nameIndex))    


#For Loop thought the list and print names in upper case
for name in nameList:
    print(name.upper())

#While - Print list if not empty
index = 0
while index < len(nameList):
    print(nameList[index])
    index = index + 1

#Sort a list
print("UnSorted List: {}".format(nameList))
sortedNames = sorted(nameList)
print("Sorted List: {}".format(sortedNames))

print("Ranges" + "-"*20)
for number in range(5):
    print(number)

print("Ranges between 2 and 5 but not including 5")
for number in range(2, 5):
    print(number)

print("Range between 1 and 10 with step of 2")
for number in range(1, 10, 2):
    print(number)   


math = 1+10
print(math)







