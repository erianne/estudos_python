"""
Exercicios link:
https://www.py4e.com/html3/04-functions
"""

# range() cria sequencias, por padrao em 1 em 1.
# https://docs.python.org/3.8/library/functions.html


"""
    Exercise 1: Run the program on your system
"""
import random

for i in range(10): 
    x = random.random()
    print(x)



"""
    Exercise 6: Rewrite your pay computation with 
    time-and-a-half for overtime and create a 
    function called computepay which takes 
    two parameters (hours and rate).
"""

def computepay(hours, rate):

    if hours > 40:
        pay = (40*rate) + (hours - 40) * (1.5*rate)
    else:
        pay = hours * rate
    
    print("Pay:", round(pay,2))


"""
Exercise 7: Rewrite the grade program from 
the previous chapter using a function called 
computegrade that takes a score as its parameter 
and returns a grade as a string.
"""

def computegrade(score):
    if score > 0.0 and score < 1.0:
        if score >= 0.9:
            print("A")
        elif score >= 0.8:
            print("B")
        elif score >= 0.7:
            print("C")
        elif score >= 0.6:
            print("D")
        elif score < 0.6:
            print("F")
    else:
        print("the score is out of range.")


computegrade(0.7)
computepay(55, 3)