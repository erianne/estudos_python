
"""
    Exercise 1: Write a while loop that starts
    at the last character in the string and works
    its way backwards to the first character in the string,
    sprinting each letter on a separate line, except backwards
"""

fruit = "banana"
index = -1
while index >= -(len(fruit)):
    letter = fruit[index]
    print(letter)
    index = index - 1


# Exercise 2
print(fruit[:])

# Exercise 3

def count(word, letter):
    count = 0
    for l in word:
        if l == letter:
            count = count+1
    print(count)

count('banana', 'a')

# Exercise 4
palavra = 'laranja'
print(palavra.count('a')) # metodo .count() conta quantas vezes uma substring aparece na string
print(palavra.count('a',0,3))


# Exercise 5

str = 'X-DSPAM-Confidence: 0.8475 '
# print(str.index(':'))
print(str.find(':')) # index e find estao fazendo a mesma coisa
numero = str[str.index(':')+1:].rstrip()
print(type(numero))
print(float(numero))
