# Aula 09 — DESAFIO 23
# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos:

num = int(input('Digite um número de 0 a 9999: '))
# É preciso dividir o numéro (num)  usando // (divide apenas a parte inteira), por 1, 10, 100 e 1000 respectivamente,
# ou seja, 1 para unidade, 10 para dezena, 100 para centena e 1000 para o milhar e assim com o resultado dessa divisão
# será feita o resto da divisão (%) o número que restar será o utilizado.

# Unidade: divide apenas a parte inteira por 1, depois o resultado divide por 10 e o resto será a unidade do número
u = num // 1 % 10

# Dezena: divide apenas a parte inteira por 10, depois o resultadodivide por 10 e o resto será a dezena do número
d = num // 10 % 10

# Centena: divide apenas a parte inteira por 1, depois o resultadodivide por 100 e o resto será a centena do número
c = num // 100 % 10

# Milhar: divide apenas a parte inteira por 1, depois o resultado divide por 1000 e o resto será o milhar do número
m = num // 1000 % 10

print(f'Analisando o número {num}')
print(f'Unidade: {u}')
print(f'Dezena: {d}')
print(f'Centena: {c}')
print(f'Milhar: {m}')

# OBS: b = f'{a:0>5}', a expressão irá preencher com 0 as casas que faltam. Então se a pessoa digitar 1, irá ser 0001.
