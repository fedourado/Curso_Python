# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.

print('Calculadora de ajuste salarial.')

sal = str(input('Digite o valor do salário para ter o reajuste: '))
sal = float(sal.replace(',','.'))
print('\n')

if sal > 1250:
    print(f'O salário de R${sal} com o reajuste ficará R${(sal*0.10)+sal:.2f} ')
else:
    print(f'O salário de R${sal} com o reajuste ficará R${(sal*0.15)+sal:.2f}')
