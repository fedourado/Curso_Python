# Faça um programa que ajude um professor a sortear um dos 4 alunos, lendo o nome deles e escrevendo o nome escolhido.

import random

print('Sorteador de alunos.')

n1 = input('Digite o nome do primeiro aluno: ')
n2 = input('Digite o nome do segundo aluno: ')
n3 = input('Digite o nome do terceiro aluno: ')
n4 = input('Digite o nome do quarto aluno: ')

lista = [n1,n2,n3,n4]
seq = random.choice(lista)

print(f'O aluno(a) sorteado(a) foi {seq}')