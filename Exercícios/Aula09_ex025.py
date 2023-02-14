# Aula 09 — DESAFIO 25
# Crie um programa que leia o nome de uma pessoa e diga se ela tem “Silva” no nome

nome = input('Digite seu nome inteiro: ').strip().title()

print(nome)
# o in é um operador
print('Seu nome tem Silva?','Silva' in nome)