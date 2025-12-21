#String decleration
car = 'Toyota'
print(car[1])

#Slicing strings
fruit = "Banana"
print(fruit[2:5])

#Iterating trough a string
for letter in fruit:
    print(letter)

#String length
print(len(fruit))

#String methods
text = " Try something new"
print("new" in text)
print("old" not in text)

if "Try" in text:
    print("Yes, 'Try' is found in the text")