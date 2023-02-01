# FATIAMENTO
# Irá identificar dentro da cadeia de caracter (string) a letra no índice indicado:

# Antes dos dois pontos indica em qual índice começa, depois dos dois pontos em qual índice termina e se tiver mais
# dois pontos e algum número indica que irá pular letras.
# frase[índice_começo:índice_final:quantidade_de_letras_para_pular]
# frase[índice_começo:índice_final]

frase = 'Curso de Python'

# frase[9]: Nesse caso a letra P
print(frase[9])

# frase[9:14]: Nesse caso da letra P até a letra O (ele exclui o índice 13, ou seja, o indicado pelo código);
print(frase[9:14])

# frase[9:15] → Nesse caso do P até o N (Python);
print(frase[9:15])

# frase[9:15:2] → Nesse caso ele imprime até a letra N, porém pula de 2 em 2. Então o que será impresso será: P T O
print(frase[9:15:2])

# frase[:5] → Quando não se coloca o índice de início ele começa no caractere índice 0 e irá até a letra do índice
# depois dos dois pontos, nesse caso índice 5 e letra C até O (CURSO)
print(frase[:5])

# frase[9:] → Quando só indica o início e ele irá fatiar do índice indicado até o final.
# Nesse caso, de P até N (PYTHON).
print(frase[9:])

# frase[9::3] → Neste exemplo começa no índice 9 e irá até o final, pois não há nada depois dos dois pontos,
# porém irá pular de 3 em 3. Irá ser impresso: P H
print(frase[9::3])

# frase[:5]→ Nesse exemplo o fatiamento vai do índice 0 até o 4, pois irá fatiar 5 índices. Irá ser impresso: C U R S O;
print(frase[:5])

# frase[9::3] → Vai começar no índice 9 e vai até o final (pois não tem nada depois dos dois pontos)
# e o :3 vai pular de 3 em 3. Irá ser impresso: P H
print(frase[9::3])
