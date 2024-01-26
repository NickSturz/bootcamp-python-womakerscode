'''Implemente um programa que classifique um aluno com base em sua
pontuação em um exame. O programa deverá solicitar uma nota de 0 a 10. Se
a pontuação for maior ou igual a 7, o aluno é aprovado; caso contrário, é
reprovado.'''

grade = int(input('digite sua nota de 0 a 10: '))

if 10 > grade >= 7 :
    print('Aprovado!!!!')
elif grade <= 6.9 :
    print('Reprovado')
else :
    print('Esta nota não é valida')