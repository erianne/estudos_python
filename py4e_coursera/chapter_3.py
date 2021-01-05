# Exercise 1: 
# Rewrite your pay computation 
# to give the employee 1.5 times the 
# hourly rate 
# for hours worked above 40 hours.

hours = float(input("Enter Hours: "))
rate = float(input("Enter Rate: "))


if hours > 40:
    # as 40 horas recebem o valor normal
    # o excedente das 40h recebem 1.5 do valor
    pay = (40*rate) + (hours - 40) * (1.5*rate)

    # uma forma alternativa do instrutor
    # as horas total recebem a taxa padrao 1.0
    # as horas excedentes recebem mais 0.5
    # pay = (hours*rate) + (hours - 40) * (0.5*rate)
else:
    pay = hours * rate

print("Pay: {}".format(round(pay,2)))

# Exercise 2: 
# Rewrite your pay program 
# using try and except so that your program 
# handles non-numeric input gracefully by printing a 
# message and exiting the program. 


try:
    hours = float(input("Enter Hours: "))
    rate = float(input("Enter Rate: "))
except:
    print("You entered a invalid number...")
    quit()

if hours > 40:
    pay = (40*rate) + (hours - 40) * (1.5*rate)
else:
    pay = hours * rate
    
print("Pay:", round(pay,2))

# Exercise 3: 
# Write a program to prompt
# for a score between 0.0 and 1.0. Ifthe score is
#  out of range, print an 
# error message. If the score is between 0.0 and 1.0, 
# print a grade using the following table:

try:
    score = float(input("Enter a score: "))
except:
    print("Bad score! You needed a number...")
    quit()


if score > 0.0 and score < 1.0:
    if score < 0.6:
        print("F")
    elif score >= 0.6:
        print("D")
    elif score >= 0.7:
        print("C")
    elif score >= 0.8:
        print("B")
    elif score >= 0.9:
        print("A")
else:
    print("the score is out of range.")