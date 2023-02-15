# Aula 10 — DESAFIO 35
# Programa que lê o comprimento de três retas e diga ao usuário se eles podem ou não formar um triângulo.

print('Descubra se as retas podem formar um triângulo.')
r1 = str(input('Digite o comprimenton da primeira reta: '))
r2 = str(input('Digite o comprimenton da primeira reta: '))
r3 = str(input('Digite o comprimenton da primeira reta: '))

r1 = float(r1.replace(',','.'))
r2 = float(r2.replace(',','.'))
r3 = float(r3.replace(',','.'))

soma1 = r1 + r2
soma2 = r1 + r3
soma3 = r2 + r3

if soma1 > r3 and soma2 > r2 and soma3 > r1:
    print('É possível formar um triângulo com essas medidas.')
else:
    print('Não é possível formar um triângulo com essas medidas.')