from math import ceil

print('Bem-Vindo ao sistema de notas do colégio Bio-Bio\n')

n1 = (input('Digite a nota de portguês do aluno: '))
n2 = (input('Digite a nota de matemática do aluno: '))
n3 = (input('Digite a nota de biologia do aluno: '))
n4 = (input('Digite a nota de história do aluno: '))

n1 = float(n1.replace(',','.'))
n2 = float(n2.replace(',','.'))
n3 = float(n3.replace(',','.'))
n4 = float(n4.replace(',','.'))

media = (n1+n2+n3+n4) / 4

print(f'A média do aluno é {media:.2F}\n')

if media >=6:
    print('Status: aluno aprovado!')
else:
    print('Status: aluno reprovado')
