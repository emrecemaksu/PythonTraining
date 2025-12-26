def erkek(): #Erkek() def is different from erkek. You cannot use -.
    name = input('Enter your name: ')
    print('Hello Mr.' + name)

#erkek()

def fahrenheit_to_celcius(fahrenheit):
    celcius = (fahrenheit - 32) * 5.0 / 9.0
    return celcius

print(fahrenheit_to_celcius(212))

#Functions definitios cannot be empty. We use pass keyword to avoid errors.
def fahrenheit_to_kelvin(fahrenheit):
    pass