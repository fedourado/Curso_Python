# Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.

# from math import = essa é uma forma de importar somente o método
import math

print('Bem-Vindo(a) ao nosso programa! Ele irá mostrar apenas a porção inteira de um decimal.')

num = input('Escreva um número qualquer (o resultado será melhor se ele for decimal): ')
num = num.replace(',','.')
num = float(num)

print(f'A porção interira do número {num} é {math.trunc(num)}')