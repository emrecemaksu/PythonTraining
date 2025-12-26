if('emre' == 'EMRE'):
    print("Equal")
elif('emre'!= 'EMRE'):
    print("Not Equal")

count = 3

message = 'Equal ' if 'emre' == 'EMRE' else 'Not Equal'
print(message)

high_income = True
good_credit = True
student = False

if high_income and good_credit and not student:
    print("Eligible for loan")
else:
    print("Not eligible for loan") 

age = 25
if 18 < age < 65:
    print("Oy Kullan") 