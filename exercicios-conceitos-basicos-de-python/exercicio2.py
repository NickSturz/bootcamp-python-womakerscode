'''Peça ao usuário para informar o ano de nascimento. Em seguida,
calcule e imprima a idade atual.
'''
import datetime

birthdayYear = int(input('Digite em que ano você nasceu: '))

actualYear = datetime.date.today().year

age = actualYear-birthdayYear

print(f'Parabéns você fez ou vai fazer {age} anos, neste ano!')