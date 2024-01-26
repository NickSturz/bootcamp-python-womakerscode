'''Faça um programa que lê três números inteiros e os mostra em ordem
crescente'''

numberList = []

number1 = int(input('Digite o primeiro número inteiro: '))
numberList.append(number1)
number2 = int(input('Digite o segundo número inteiro: '))
numberList.append(number2)
number3 = int(input('Digite o terceiro número inteiro: '))
numberList.append(number3)

#print(numberList)

numberList.sort()

print(numberList)

