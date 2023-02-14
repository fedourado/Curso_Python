# Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO

print('Descubra se um ano é bissexto ou não')
ano = int(input('\nDigite o ano que deseja saber e deixe o resto com a gente: '))

bissexto = ano % 4

if bissexto == 0:
    print(f'O ano {ano} é bissexto.')
else:
    print(f'O ano {ano} não é bissexto.')
