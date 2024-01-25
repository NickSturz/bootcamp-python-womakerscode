'''Faça um Programa que pergunte quanto você ganha por hora e o
número de horas trabalhadas no mês.Calcule e mostre o total do seu
salário no referido mês'''

hourSalary= float(input('Digite aqui seu salário por hora trabalhada: '))
hourWorked= float(input('Digite aqui as horas trabalhadas no mês: '))

monthSalary = hourSalary*hourWorked

print(f'Você deverá receber {monthSalary} BRL de salário')