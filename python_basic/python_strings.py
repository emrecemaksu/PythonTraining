#String decleration
car = 'Toyota'
print(car[1])

#Slicing strings
fruit = "Banana"
print(fruit[2:5])

#Iterating trough a string
for letter in fruit:
    print(letter, end= " ")

print(" ")
#String length
print(len(fruit), end= "\n")

#String methods
text = " Try something new"
print("new" in text)
print("old" not in text)

if "Try" in text:
    print("Yes, 'Try' is found in the text", end= " ")

print(" ")
print(f"{car} {fruit}")
print(text.strip()) #removes whitespace from the beginning and the end