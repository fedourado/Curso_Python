# Aula 09 — DESAFIO 24
# Crie um programa que leia o nome de uma cidade e diga se ela ou não começa com a palavra “São”

cidade = input('Escreva o nome da sua cidade: ').strip().title()

print(cidade)

# 'São' possui 3 letras, vai do índice 0 até o 2, portanto para saber se começa com 'São' é preciso fazer o fatiamento
# [:3] antes dis dois pontos o nada significa que começa do primeiro índice e depois dos dois pontos é onde deve parar
# de ler, nesse caso 'São' mesmo terminando no índice 2 é preciso colocar até o 3, pois ele lê até o 2 e para no 3.
print(cidade[:3] == 'São')
