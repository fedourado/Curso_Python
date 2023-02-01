# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo,
# calcula e mostre o comprimento da hipotenusa.

import math

print('Utilize esse programa para calcular a hipotenusa')

ca = input('Digite o valor do cateto adjacente: ')
co = input('Digite o valor do cateto oposto: ')
co = co.replace(',','.')
ca = ca.replace(',','.')

ca = float(ca)
co = float(co)

hipo = math.hypot(ca,co)

print(f'Um triângulo retângulo com cateto adjacente {ca} e cateto oposto {co}, tem a hipotenusa igual a {hipo}')