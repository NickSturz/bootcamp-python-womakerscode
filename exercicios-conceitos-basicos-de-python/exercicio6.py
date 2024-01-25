'''Escreva um programa que calcule o tempo de uma viagem. Faça um
comparativo do mesmo percurso de avião, carro e ônibus.
Levando em consideração:
● avião = 600 km/h
● carro = 100 km/h
● ônibus = 80 km/h
'''

distance = float(input('Digite aqui a distancia do local em km: '))

airplane = (distance/600)*60

car = (distance/100)*60

bus = (distance/80)*60

print(f'Para percorrer esse trajeto você demorará: \n {airplane} mitutos para ir de avião. \n {car} mitutos para ir de carro. \n {bus} mitutos para ir de ônibus.')