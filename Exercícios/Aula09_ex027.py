# Aula 09 — DESAFIO 27
# Faça um programa que leia o nome completo de uma pessoa e mostre em seguida o
# primeiro nome e último nome separadamente

nome = input('Digite seu primeiro nome completo: ').strip().title()
print(f'Prazer, {nome}, vamos analisar o seu nome?')
n = nome.split()
print(nome)
print(f'Seu primeiro nome é: {n[0]}')
# n[índice] irá imprimir a palavra, ou letra, dentro desse índice. O len(n) irá contar a quantidade de caracteres
# ou palavras numa frase. Ao usar o len(n) dentro do n[índice] e subtrair 1 -- n[len(n)-1) -- está sendo solicitado
# que o programa imprima a palavra que se encontra na posição n-1 encontrada pelo len.
# Exemplo: se o nome for Maria das Graças ele terá 3 palavras, ao subtrair esse número por 1 (3-1=2), o programa irá
# ler o índice 2, que é o último nome.
print(f'Seu último nome é: {n[len(n)-1]}')
