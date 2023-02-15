# Aula 10 — DESAFIO 28
# Escreve um programa que faça o computador “pensar” num número entre 0 e 5 e peça para o usuário tentar descobrir
# qual foi o número escolhido pelo computador.


from random import choice
import emoji
from time import sleep
import playsound

lista = [0,1,2,3,4,5]
num_escolhido = choice(lista)
# comp = randint(0, 5) --> faz a variável amarzenar um número random entre 0 e 5 (outro método de fazer)

print('-=-' * 41)  # Faz o "-=-" ser repetido 10 vezes
print('Bem-Vindo ao meu novo jogo, acerte o número.')
print('O jogo consiste em escolher um número entre 0 e 5. Se você acertar o número que eu pensei, você ganha. '
      'Se não, você perde.')
print('VAMOS JOGAR!')
print('-=-' * 41)

num_usuario = int(input('Eu já escolhi o número. Agora,você escolhe um número entre 0 e 5 e vamos ver se tem sorte: '))
print('PROCESSANDO...')
# sleep(1) -- Essa função irá fazer com que a próxima frase demora 2s para aparecer na tela

if num_usuario == num_escolhido:
    playsound.playsound('D:/Feh/pythonProjects/Exercícios/Fausto_acertou.mp3')
    print(emoji.emojize('PARABÉNS :grinning_face_with_smiling_eyes:! você escolheu o número certo e venceu o jogo!'))
else:
    playsound.playsound('D:/Feh/pythonProjects/Exercícios/Fausto_Errou.mp3')
    print(emoji.emojize(f'É uma pena você perdeu :slightly_frowning_face:! O número era o {num_escolhido}.'))
