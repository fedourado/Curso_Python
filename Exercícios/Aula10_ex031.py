# Aula 10 — DESAFIO 31
# Desenvolva um programa que pergunte a distância de uma viagem em km. Calcule o preço da passagem,
# cobrando R$0.50 por km para viagens de até 200 km e R$0,45 para viagens mais longas.

print('ViagePlus, o melhor lugar para comprar suas passagens.')
print("""\nPara calcular o valor da passagem é necessário informar a distância da viagem em Km. Segue as informações:
será cobrado R$0,50 por km para viagens de até 200km e R$0,45 para viagens mais longas.""")

distancia = str(input('Distância da viagem (em km): '))
distancia = (distancia.replace(',','.'))
valor = float(distancia)

if valor <= 200:
    print(f'A distância da sua viagem é {distancia}km e o valor cobrado pela passagem será de R${valor * 0.50:.2f}')
else:
    print(f'A distância da sua viagem é {distancia}km e o valor cobrado pela passagem será de R${valor * 0.45:.2f}')
