# Aula 10 — DESAFIO 28
# Escreve um programa que faça o computador “pensar” num número entre 0 e 5 e peça para o usuário tentar descobrir
# qual foi o número escolhido pelo computador.


from random import choice

n1 = 0
n2 = 1
n3 = 2
n4 = 3
n5 = 4
n6 = 5

lista = [n1,n2,n3,n4,n5,n6]
num_escolhido = choice(lista)

print('Bem-Vindo ao meu novo jogo, acerte o número.')
print('O jogo consiste em escolher um número entre 0 e 5. Se você acertar o número que eu pensei, você ganha. '
      'Se não, você perde.')
print('Vamos jogar!\n')

num_usuario = int(input('Eu já escolhi o número. Agora,você escolhe um número entre 0 e 5 e vamos ver se tem sorte: '))

if num_usuario == num_escolhido:
    print('Parabéns, você escolheu o número certo e venceu o jogo!')
else:
    print('É uma pena, mas você perdeu. :(')