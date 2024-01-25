'''Faça um Programa que peça dois números, realize as principais
operações soma, subtração, multiplicação, divisão

'''
numero1 = int(input('Digite seu primeiro número: '))
numero2 = int(input('Digite seu segundo número: '))
print(f'Esses são os números escolhidos {numero1}, {numero2}')

soma = numero1+numero2
print(f'O resultado da soma dos numeros é: {soma}') 

subtrair = numero1-numero2
print(f'O resultado da subtração dos numeros é: {subtrair}') 

multiplicar = numero1*numero2
print(f'O resultado da multiplicação dos seus números é: {multiplicar}')

divisaoComum = numero1/numero2
print(f'O resultado da divisão comum dos seus números é: {divisaoComum}')

divisaoInteira = numero1//numero2
print(f'O resultado da divisão com resultados inteiros dos seus números é: {divisaoInteira}')