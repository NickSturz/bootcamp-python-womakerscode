'''Faça um Programa que peça a quantidade de quilômetros, transforme
em metros, centímetros e milímetros.
'''

km = float(input('Digite aqui quantos kms quer converter: '))

meters = km*1000
cm = meters*100
mm = cm*10

print(f'Você quis converter {km} kms, que é equivalente a {meters} metros, ou {cm} centímetros, ou {mm} milímitros')