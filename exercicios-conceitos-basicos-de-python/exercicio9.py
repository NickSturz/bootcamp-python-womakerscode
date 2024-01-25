'''Solicite ao usuário o número de horas de exercício físico por semana.
Calcule o total de calorias queimadas em um mês, considerando uma
média de 5 calorias por minuto de exercício'''

workoutHour= int(input('Digite aqui quantas horas de exercício você fez: '))

lostCalories = (workoutHour*60)/5

print(f'Você gastou {lostCalories} calorias')