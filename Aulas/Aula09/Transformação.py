# TRANSFORMAÇÃO
# Uma lista de string é imutável, mas é possível mudar por métodos.

frase = 'Curso de Python'

# frase.replace('Python','Android') → Substitui a palavra Python por Android (Uso para trocar ‘.’ por ‘,’ nos decimais);
print(frase.replace('Python','Android'))

# frase.upper() → Deixa todas as letras da variável em maiúsculas: CURSO DE PYTHON;
print(frase.upper())

# frase.lower() → Deixa todas as letras da variável em minúsculo: curso de python;
print(frase.lower())

# frase.capitalize() → Deixa todos os caracteres em minúsculo e somente a primeira letra...
# em maiúsculo: Curso de python;
print(frase.capitalize())

# frase.title() → Analisa quantas palavras tem a string, coloca em maiúscula todas as primeiras letras das palavras
# e deixa as outras letras em minúsculo: Curso De Python (Identifica as palavras pela posição dos espaços).
print(frase.title())

print('----------------------------------------------------------------------')

frase1 = '  Aprenda Python  '

# frase1.strip() → Remove todos os espaços inúteis, no começo e no final da string;
# //APRENDEA PYTHON/]
print('|  Aprenda Python  |')
print(frase1.strip())

# frase1.rstrip() → Remove todos os espaços da direita;
#   APRENDEA PYTHON/
print('\n|  Aprenda Python  |')
print(frase1.rstrip())

# frase1.rstrip() → Remove todos os espaços da direita;
# //APRENDEA PYTHON
print('\n|  Aprenda Python  |')
print(frase1.lstrip())
