# Faça um programa que leia uma frase pelo teclado:
# Quantas vezes aparece a letra “A”;
# Em que posição ela aparece a primeira vez;
# Em que posição ela aparece a pela última vez;

frase = input('Digite uma frase da sua escolha: ').strip().upper()

print('A letra "A" aparece',frase.count('A'), 'vezes na frase.')
print('A letra "A" aparece pela primeira vez na posição',frase.find('A') + 1)
# O string.rfind() irá procurar da direita para a esquerda
print('A letra "A" aparece pela última vez na posição',frase.rfind('A') + 1)