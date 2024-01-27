''' Crie um programa que solicite ao usuário um login e uma senha. O
programa deve permitir o acesso apenas se o usuário for "admin" e a senha
for "admin123", caso contrário imprima uma mensagem de erro'''

user = input('digite seu email: ')
password = input('digite sua senha: ')

if ((user != 'admin') or (password != 'admin1234')):
    print('Ops! você não tem essa permisão')
else :
    print('Login feito com sucesso')