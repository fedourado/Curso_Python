# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math

print('Esse programa dá o valor do seno, cosseno e da tangente por meio de um ângulo')

ang = input('Digite um ângulo: ')
ang1 = ang.replace(',','.')
ang1 = float(ang)
ang1 = math.radians(ang1)

cos = math.cos(ang1)
seno = math.sin(ang1)
tang = math.tan(ang1)

print(f'O ângulo {ang}º tem o seno igual a {seno:.2f}')
print(f'O ângulo de {ang}º tem o cosseno igual a {cos:.2f}')
print(f'O ângulo de {ang}º tem a tangente igual a {tang:.2f}')

