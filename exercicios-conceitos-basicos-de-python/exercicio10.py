'''Faça um Programa que utilize 4 variáveis como preferir e no final print
uma mensagem amigável utilizando as variáveis criadas.
Exemplos de variáveis: nome, idade, lugar, profissão ....
Exemplo de retorno: Olá Maria, prazer te conhecer. Sou de São Paulo
também e estou migrando de área'''

name = input('Hi, Whats your name? ')
age = int(input(f'Hey {name}! How old are u? '))
likeToPlay = input('So, what you like to play? ')
movie = input('and what kind of moovies do you like? ')
hasChildren = bool(input('hmmm, If you have Children say so, if not, just enter this question! '))
#print(hasChildren)

if not hasChildren :
    print(f'Hey {name}, I like you! You\'re a {age} yo person, You doing great! Now, get out with your friends to play some {likeToPlay} or whatch some {movie} movies' )
else :
    howManyChildren = int(input('How many children? '))
    #if howManyChildren == 0 :

    if howManyChildren <=1 :
        print(f'Congrats {name}, you are a beautiful {age} yo parent, go play {likeToPlay} or whatch some {movie} movies with your kid you doing great')
    else:
        print(f'Congrats {name}, you are a beautiful {age} yo parent, go play {likeToPlay} or whatch some {movie} movies with your kids you doing great')

