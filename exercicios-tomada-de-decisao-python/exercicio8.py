'''Criar um programa em Python que solicite três números ao usuário, utilize
estruturas condicionais para determinar o maior entre eles e apresente o
resultado.'''

number1 = int(input('Digite o primeiro número inteiro: '))
number2 = int(input('Digite o segundo número inteiro: '))
number3 = int(input('Digite o terceiro número inteiro: '))

biggest = number1 #supposed this is the biggest

if (number2 > biggest):
    biggest = number2
if (number3 > biggest):
    biggest = number3

print(f'Maior: {biggest}')