'''Faça um programa que peça uma nota, entre zero e dez. Mostre uma
mensagem caso o valor seja inválido e continue pedindo até que o usuário
informe um valor válido'''

grade = int(input('digite uma nota de 0 a 10: '))

while grade < 0 or grade > 10 :
    print('Ops valor incorreto! Tente novamente.')
    grade = input('digite uma nota de 0 a 10: ')


