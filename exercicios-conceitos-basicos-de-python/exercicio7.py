'''Solicite ao usuário o peso em kg e a altura em metros. Calcule e
imprima o Índice de Massa Corporal (IMC) usando a fórmula:
IMC = peso / (altura x altura).'''

height= float(input('Digite aqui usa altura em metros: '))
weight= float(input('Digite aqui seu peso em quilos: '))

bmi = weight/(height*height)

if bmi > 40: 
    result = 'Obesidade grau 3'
elif 35 <= bmi <= 39.9:
    result = 'Obesidade grau 2'
elif 30 <= bmi <= 34.9:
    result = 'Obesidade grau 1'
elif 25 <= bmi <= 29.9:
    result= 'Sobrepeso'
elif 18.6 <= bmi <= 24.9:
    result = 'Normal'
else:  
    result =  'Abaixo do peso'


print(f'O seu IMC é {bmi}, se enquadrando como {result}.')

