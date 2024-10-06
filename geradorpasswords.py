import random
chars = '!#123456789@ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz' 
password = ''
lengthPW = int(input('Que tamanho que queres para tua password: '))
for _ in range(lengthPW):
	password += random.choice(chars)
print(password)
