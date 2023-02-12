# Num programa sem condições, todos os comandos são executados. Entretanto, um programa na maioria das vezes terá
# condições, ou seja, irá possuir caminhos diferentes que esse programa pode seguir conforme o usuário.
# Um exemplo de condição é o if e else:

# if carro.esquerda():
#    true
# else:
#    false

# Uma variável com pergunta que necessita da entrada de uma resposta do usuário.
tempo = int(input('Quantos anos tem seu carro? '))

# Uma condição que verifica se a resposta da variável tempo é menor ou igual a 3. Caso ela seja true irá ter uma saída
# com a frase "carro novo". Caso contrário a resposta da condição seja false, terá uma saída com a frase "carro velho"
if tempo <= 3:
    print('Carro novo')
else:
    print('Carro velho')
print('--FIM--')

# OBS: Todo comando que estiver alinhado ao lado esquerdo da tela será SEMPRE executado, caso o comando esteja alinhado
# à direita ele poderá ou não ser executado.

# CONDIÇÃO SIMPLIFICADA
# Nesse exemplo a condição é feita em apenas uma linha

tempo = int(input('\nQuantos anos tem seu carro? '))

print('Carro novo'if tempo <=3 else 'Carro velho')
print('--FIM--')