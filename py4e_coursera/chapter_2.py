"""
Exercicios link:
https://www.py4e.com/html3/02-variables
"""



# Exercise 2: Write a program that uses input to prompt 
# a user for their name and then welcomes them
name = input("Enter your name: ")
print("Hello {}".format(name))


# Exercise 3: Write a program to prompt 
# the user for hours and rate per hour to 
# compute gross pay.

hours = float(input("Enter Hours: "))
rate = float(input("Enter Rate: "))
pay = hours * rate
print("Pay: {}".format(round(pay,2)))

# Exercise 4: Assume that we execute the 
# following assignment statements:


width = 17
height = 12.0

width//2 # retorna o quociente da divisao
width/2.0
height/3
1 + 2 * 5

# Exercise 5: Write a program which prompts the user for 
# a Celsius temperature, convert the temperature to Fahrenheit, 
# and print out the converted temperature.

celsius = float(input("Enter a temperature in Celsius: "))
fahrenheit = 1.8*celsius + 32 
print("{}C is {}F".format(celsius, fahrenheit))