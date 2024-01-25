'''print('Hello World, meu primeiro codigo até que enfim com python')
#comentários em python
''' 
'''
comentário
longo5
com mais linhas em 
python
'''
'''

# INT
numero = int(input('Digite seu numero 1: '))
print(numero)

#Float
numero2 = float(input('Digite seu numero 2: '))
print(numero2)

#String
frase = input('Digite sua frase: ')
print(frase)

#matematica 

numero3 = int(input('Digite seu numero 3: '))
print(numero3)

soma = numero+numero3
print(f'A soma dos numeros é {soma}') #f é o format, para dizer que vc vai trabalhar algum dado

subtrair = numero-numero3
print(subtrair)

multiplicar = numero*numero3
print(multiplicar)

divisaoComum = numero/numero3
print(divisaoComum)

divisaoInteira = numero//numero3
print(divisaoInteira) #para não retornar as casas após a virgula caso a divisão quebre

valor = 5
valor += 1

valor = 5
valor -= 1

#resto
#10%3 = 1 

#ordem de precedencia

calculo = (2+5)*((5+4)*3)
print(calculo)

#operadores relacionais == > >= < <= !=

print('Olá {}, você tem {} anos'.format('Nick',30))

#IF E ELSE
numero = int(input('Digite seu numero 1: '))
if numero > 0 : {
    print(f'{numero} é um número positivo')
} 
else : {
    print(f'{numero} é um número negativo')
}

#WHILE
numero = -1

while numero < 0:
    numero = int(input('Digite seu numero 1: ')) #aspas duplas sempre string, aspas simples para formatar
print('Número positivo inserido com sucesso')


#FOR para cada item da lista ele toma uma decisão

frutas = ['Maçã', 'Banana', 'Uva'] #declaração de lista
#frutas = list() essa tbm é uma declaração de lista
for fruta in frutas: #para cada item na lista fruta é variavel
    print(fruta)

frutas.append('Mamão')
print(frutas)
#print(', '.join(frutas))


#TUPLAS são listas que não podem ser modificadas

tupla = ('Maça', 'Banana', 'Limão')  #a tupla é definida pelo () ao invés do []
print(tupla)


#DICIONARIO adicionar valores e significados

dicionario = {'Chave':'Valor e/ou descrição'}
dicionario['Banana'] = 'É uma fruta'
dicionario['Carro'] = 'É um veículo'
dicionario['Gato'] = 'É um pet'
print(dicionario)

#lista[-1]    para retornar ultimo valor da lista

#### FUNÇÕES

#Declaração da função

def soma():
    calculo = 10+2
    print(f'O resultado da soma é: {calculo}')
    subtracao()  #chamada de função dentro da fun~ção

def subtracao():
    subtrair = 10-2
    print(f'O resultado da subtração é: {subtrair}')
    multiplicacao()

def multiplicacao():
    multiplicar = 10*2
    print(f'O resultado da multiplicacao é: {multiplicar}')

soma()  #chamada da função

def soma(num1,num2):
    calculo = num1+num2
    print(f'O resultado da soma é: {calculo}')
    subtracao(num1,num2)  #chamada de função dentro da fun~ção

def subtracao(num1,num2):
    subtrair = num1-num2
    print(f'O resultado da subtração é: {subtrair}')
    multiplicacao(num1,num2)

def multiplicacao(num1,num2):
    multiplicar = num1*num2
    print(f'O resultado da multiplicacao é: {multiplicar}')

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))

soma(num1,num2) 

def multiplicacao():
    multiplicar = 10*2

    #abertura de arquivo
    file = 'python-basic/arquivo.txt'

    #open para escrita
    arquivo_escrita = open(file, "w") #é preciso avisar que vai escrever, para depois escrever
    arquivo_escrita.write("Texto a ser escrito") #colocar aqui o que escrever
    arquivo_escrita.close()

    #open somente para leitura
    arquivo_leitura = open(file, "r")  #é preciso abrir para ler, para depois o comando de ler
    leitura = arquivo_escrita.read()
    print(leitura) #para ver o que está sendo escrito
    arquivo_leitura.close()

    #open arquivo binario
    arquivo_binario = open(file, "wb")

multiplicacao()


#automatizando processo pegar um resuldado ou conjunto de dados no txt ou arquivo
def multiplicacao():
    multiplicar = 10*2

    #abertura de arquivo
    file = 'python-basic/arquivo.txt'

    #open para escrita
    arquivo_escrita = open(file, "w") #é preciso avisar que vai escrever, para depois escrever
    arquivo_escrita.write(f'O resultado da multiplicacao é: {multiplicar}') #colocar aqui o que escrever
    arquivo_escrita.close()

    #open somente para leitura
    arquivo_leitura = open(file, "r")  #é preciso abrir para ler, para depois o comando de ler
    leitura = arquivo_leitura.read()
    print(leitura) #para ver o que está sendo escrito
    arquivo_leitura.close()

multiplicacao()

'''

#Tratamento de exceções

def divisao(a,b):
    try:
        resultado = a/b
        print(resultado)
    except ZeroDivisionError:  #nomes de tratamentos de erro e gerar mensagem clara
        print("Erro: Impossível dividir por zero")
    except TypeError as e:  # tipo do erro as error (as e) para mapear o erro
        print(f'Erro: O tipo do dado está incorreto. \n Detalhes: {e}')  #\n para quebrar linha
    else:
        print('Deu certo, sem exceções')

divisao(10,'xuxu')

