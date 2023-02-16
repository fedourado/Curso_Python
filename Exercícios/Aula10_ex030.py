# Aula 08 — DESAFIO 30
# Crie um programa que leia um número inteiro qualquer e mostre na tela se ele é PAR ou ÍMPAR.

print('Par ou ímpar? Esse program te ajudará a descobrir se um número pertence ao grupo dos pares ou dos ímpares. ')

num = int(input('\nDigite um número inteiro (sem casas decimais): '))
par = num % 2

if par == 0:
    print(f'O número {num} é \033[1;34mpar\033[m.')
else:
    print(f'O número {num} é \033[1;34mímpar\033[m.')
