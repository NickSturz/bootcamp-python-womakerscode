'''O programa deve calcular e apresentar a quantidade de números pares e
ímpares inseridos. O processo de leitura deve ser encerrado quando o usuário
informar o valor zero. Certifique-se de incluir validações para garantir que
apenas números positivos sejam considerados na contagem e cálculos.
'''
numberList = []

qdtPair = 0

qdtOdd = 0

number = -1
while number != 0 :
    number = int(input('Insira um número inteiro diferente de zero: '))

    if number == 0 :
        break
    elif number < 0 :
        print('Não recebemos números negativos')
    else :
        numberList.append(number)
        if (number % 2) == 0 :
            qdtPair = qdtPair + 1
        else :
            qdtOdd = qdtOdd + 1
        print(numberList, f'\n Você tem {qdtPair} números pares. \n Você tem {qdtOdd} números ímpares')
