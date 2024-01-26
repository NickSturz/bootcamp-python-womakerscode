'''Faça um Programa que pergunte em que turno você estuda. Peça para
digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom
Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
'''

period = input('Escreva qual desses períodos você estuda? M-matutino ou V-vespertino ou N-noturno :')


if period == 'M-matutino' :
    print('Bom dia flor do diaaaa!')
elif period == 'V-vespertino' :
    print('Boa tarde lindeza!')
elif period == 'N-noturno' :
    print('Boa noite pessoa, só não esquece de nanar!')
else :
    print('Eita, valor inválido, confere se digitou os valores corretamente como os a seguir? M-matutino ou V-vespertino ou N-noturno')