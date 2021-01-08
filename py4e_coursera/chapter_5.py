"""
Exercicios link:
https://www.py4e.com/html3/05-iterations
"""

#Exercicio 1

count = 0
total = 0
try:
    while True:
        inp = input("Enter a number: ")
        if inp == "done":
                break
        total = total + float(inp)
        count = count + 1
        average = total/count
    print(total, count, round(average,1))
except:
    print("bad data")

    
# Exercicio 2

numeros = []
total = 0

try:
    while True:
        inp = input("Enter a number: ")
        if inp == "done":
            break
        numeros.append(float(inp))   
    print(max(numeros),min(numeros))
except:
     print("bad data")

    

