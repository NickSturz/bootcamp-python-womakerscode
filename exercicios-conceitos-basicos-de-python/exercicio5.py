'''Escreva um programa que calcule o salário líquido. Lembrando de
declarar o salário bruto e o percentual de desconto do Imposto de
Renda.
● Renda até R$ 1.903,98: isento de imposto de renda;
● Renda entre R$ 1.903,99 e R$ 2.826,65: alíquota de 7,5%;
● Renda entre R$ 2.826,66 e R$ 3.751,05: alíquota de 15%;
● Renda entre R$ 3.751,06 e R$ 4.664,68: alíquota de 22,5%;
● Renda acima de R$ 4.664,68: alíquota máxima de 27,5%.
'''
salary = float(input('Qual é o seu salário? '))
if salary <= 1903.98 :
    print(f'Seu salário não tem desconto de imposto de renda, portanto receberá {salary} do valor inteiro.')
elif 1903.99 <= salary <= 2826.65 :
    liquidSalary = salary-(salary*0.075)
    print(f'Seu salário líquido é {liquidSalary} BRL, pois teve 7,5% de imposto de renda.')
elif 2826.66 <= salary <= 3751.05 :
    liquidSalary = salary-(salary*0.15)
    print(f'Seu salário líquido é {liquidSalary} BRL, pois teve 15% de imposto de renda.')
elif 3751.06 <= salary <=  4664.68 :
    liquidSalary = salary-(salary*0.225)
    print(f'Seu salário líquido é {liquidSalary} BRL, pois teve 22,5% de imposto de renda.')
else :
    liquidSalary = salary-(salary*0.275)
    print(f'Seu salário líquido é {liquidSalary} BRL, pois teve 27,5% de imposto de renda.')

