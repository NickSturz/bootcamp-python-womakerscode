'''Desenvolva um programa que solicite ao usuário os comprimentos dos três
lados de um triângulo e classifique-o como equilátero, isósceles ou escaleno.
equilátero: todos os lados com o mesmo valor
isósceles: dois lados com o mesmo valor
escaleno: todos os lados com medidas distintas'''

measure1 = int(input('digite o tamanho do lado 1 do triangulo: '))
measure2 = int(input('digite o tamanho do lado 2 do triangulo: '))
measure3 = int(input('digite o tamanho do lado 3 do triangulo: '))

if measure1 == measure2 == measure3 :
    print('Este é um triangulo equilatero')
elif measure1 != measure2 == measure3 :
    print('Este é um triangulo isoceles')
elif measure1 == measure2 != measure3 :
    print('Este é um triangulo isoceles')
elif measure1 == measure3 != measure2 :
    print('Este é um triangulo isoceles')
else :
    print('Este é um triangulo escaleno')
