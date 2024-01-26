'''Faça um Programa que peça as quatro notas de 5 alunos, calcule
e armazene numa lista a média de cada aluno, imprima o número
de alunos com média maior ou igual a 7.0'''

dictionaryStudents = {}

for n in range(0, 5):
    student = input('Digite seu nome: ')
    nota1 = float(input('Digite a primeira nota: '))
    nota2 = float(input('Digite a segunda nota: '))
    nota3 = float(input('Digite a terceira nota: '))
    nota4 = float(input('Digite a quarta nota: '))

    media = (nota1+nota2+nota3+nota4)/4

    dictionaryStudents.update({f'{student}': f'{media}'})

    print(dictionaryStudents)
    for media in dictionaryStudents.values() :
        if media > 7:
            mediaAlta = dictionaryStudents.get.values
            print(f'Alunos com nota a partir de 7; ')





