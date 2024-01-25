'''Receba do usuário a quantidade de litros de combustível consumidos e
a distância percorrida. Calcule e imprima o consumo médio em km/l.'''

traveledKm= float(input('Digite aqui quantos kms foi percorrido: '))
fuelLiters= float(input('Digite aqui quantos litros de combustível foram gastos: '))

averageConsumption = traveledKm/fuelLiters

print(f'Seu veículo andou {averageConsumption} quilômetros por litro')