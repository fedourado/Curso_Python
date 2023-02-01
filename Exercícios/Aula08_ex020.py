# Faça um programa que leia o nome dos 4 alunos e mostre a ordem sorteada.

import random

print('Sorteador com ordem')

n1 = input('Digite o nome do primeiro aluno: ')
n2 = input('Digite o nome do segundo aluno: ')
n3 = input('Digite o nome do terceiro aluno: ')
n4 = input('Digite o nome do quarto aluno: ')

lista = [n1,n2,n3,n4]
random.shuffle(lista)

print(f'A ordem dos alunos sorteados será: {lista}')