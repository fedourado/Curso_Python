# Faça um programa que leia 3 números e mostre qual é o maior e qual o menor

print('Vamos comparar números? Digite 3 números e iremos dizer qual é o maior e qual é o menor.')
n1 = str(input('Digite o primeiro número: '))
n2 = str(input('Digite o segundo número: '))
n3 = str(input('Digite o terceiro número: '))

n1 = float(n1.replace(',','.'))
n2 = float(n2.replace(',','.'))
n3 = float(n3.replace(',','.'))

print('\n')

if n1 > n2 and n1 > n3:
    print(f'{n1} é o maior número.')
elif n2 > n1 and n2 > n3:
    print(f'{n2} é o maior número.')
else:
    print(f'{n3} é o maior número.')


if n1 < n2 and n1 < n3:
    print(f'{n1} é o menor número.')
elif n2 < n3 and n2 < n1:
    print(f'{n2} é o menor número.')
else:
    print(f'{n3} é o menor número.')


