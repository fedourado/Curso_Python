# DIVISÃO
# Irá dividir strings


frase = 'Curso de Python'

# frase.split() → Vai ocorrer uma divisão através dos espaços.
# Cada caractere recebe um índice novo e as palavras são numeradas.
# |C|U|R|S|O| |D|E| |P|Y|T|H|O|N|
# |0 1 2 3 4| |0 1| |0 1 2 3 4 5| --> índices
#       0       1         2       --> numeração das palavras
print(frase.split())
# Resultado: ['Curso', 'de', 'Python']

# '-'.join(frase) → As palavras irão se juntar e no lugar do espaço irá ter ‘ - ’
# |C| |U| |R| |S| |O| | | |D| |E| | | |P| |Y| |T| |H| |O| |N|
#  0   1   2   3   4   5   6   7   8   9   10  11  12  13  14 --> índices
print('-'.join(frase))
# Resultado: C-u-r-s-o- -d-e- -P-y-t-h-o-n

# Para colocar os traços apenas nos espaços utiliza os dois métodos juntods, pois ao usar o split as palavras viram
# blocos como se fossem algo único e com o join apenas esses blocos serão separados
print('-'.join(frase.split()))
# Resultado: Curso-de-Python
