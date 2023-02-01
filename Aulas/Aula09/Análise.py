# ANÁLISE
# A análise, como o nome diz, irá analisar a string e dar informações sobre ela.

frase = 'Curso de Python'

# len(frase) → Irá mostrar a quantidade de caracteres da frase: 15 caracteres;
print(len(frase))

# frase.count('o')  → Conta quantas vezes o ‘o’ minúsculo aparece: 2 vezes (índice 4 e 13):
print(frase.count('o'))

# frase.count('o', 0, 7) → Conta quantos 'o' tem entre o índice 0 até o 7: aparece 1 vez (índice 4);
print(frase.count('o', 0, 7))

# frase.find('de') → Mostra em qual índice o 'de' está localizado: índice 6 e 7 (aparece apenas o índice 6);
print(frase.find('de'))
# frase.rfind('de') procura o 'de' começando da direita para a esquerda, ou seja, do final da frase para o começo.
print(frase.rfind('de'))

# frase.find('Android') → Quando coloca uma string que não existe no find, ele retorna o valor -1 (ou seja, não existe).
print(frase.find('Android'))

# urso’ in frase → Verifica se existe a palavra ‘Curso’ na variável frase: retorna true
# (Não é funcionalidade e sim operador);
print('Curso' in frase)
