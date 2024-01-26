'''Utilizando listas faça um programa que faça 5 perguntas para uma
pessoa sobre um crime.
As perguntas são:
""Telefonou para a vítima?""
""Esteve no local do crime?""
""Mora perto da vítima?""
""Devia para a vítima?""
""Já trabalhou com a vítima?""
O programa deve no final emitir uma classificação sobre a participação
da pessoa no crime.
Se a pessoa responder positivamente a 2 questões ela deve ser
classificada como ""Suspeita"", entre 3 e 4 como ""Cúmplice"" e 5 como
""Assassino"".
Caso contrário,ele será classificado como""Inocente"".
'''

listAnswers = []

question = input('Responda apenas com sim ou não: Telefonou para a vítima? ')
listAnswers.append(question)
question = input('Responda apenas com sim ou não: Esteve no local do crime? ')
listAnswers.append(question)
question = input('Responda apenas com sim ou não: Mora perto da vítima? ')
listAnswers.append(question)
question = input('Responda apenas com sim ou não: Devia para a vítima? ')
listAnswers.append(question)
question = input('Responda apenas com sim ou não: Já trabalhou com a vítima? ')
listAnswers.append(question)

print(listAnswers)

yesAnswers = 0
noAnswers = 0

for question in listAnswers:
    if question == 'sim' :
        yesAnswers = yesAnswers + 1
    elif question == 'não' :
        noAnswers = noAnswers + 1
    else :
        print('valores incorretos computados')
if yesAnswers >= 5 :
    print('Assassino')
elif yesAnswers >= 3 :
    print('Cumplice do crime')
elif yesAnswers >= 2 :
    print('Suspeita do crime')
else :
    print('Testemunha liberada')