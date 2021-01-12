

# Exercise 2

    # get a file from prompt
filename = input("Enter the file name: ")

try:
    fil = open(filename)
except:
    print('Bad file: ', filename)
    exit()

count = 0
spams = 0
for line in fil:
    if line.startswith('X-DSPAM-Confidence:'):
        number = line[line.find(':')+1:].rstrip()
        spams = spams + float(number)
        count = count + 1
        avg_spam = spams / count
print('Average spam confidence: {}'.format(avg_spam))

'''
str = 'X-DSPAM-Confidence: 0.8475 '
# print(str.index(':'))
print(str.find(':')) # index e find estao fazendo a mesma coisa
numero = str[str.index(':')+1:].rstrip()
print(type(numero))
print(float(numero))
'''