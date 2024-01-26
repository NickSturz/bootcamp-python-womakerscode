'''Desenvolver um programa que solicite a idade do usuário e identifique se
ele é uma criança, um adolescente, adulto ou idoso'''

age = int(input('Quantos anos da pessoa em questão? '))

if age <=1:
    print ('Baby')
elif age < 13:  
    print ('Kiddo')
elif age < 19:
    print ('Teenager')
elif age < 60:
    print ('Adult')
elif age < 80:
    print ('Elderly')
else:
    print ("Advanced in age")
