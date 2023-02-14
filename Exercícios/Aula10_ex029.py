# Aula 10 — DESAFIO 29
# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80 km/h,
# mostrar uma mensagem dizendo que ele foi multado.

print('Radar Online, melhor lugar para identificar uma infração na trânsito e multar')

velocidade = int(input('Indique a velocidade do veículo: '))
multa = (velocidade - 80) * 7

if velocidade > 80:
    print(f'\nVocê ultrapassou o limite de velocidade e será multado em R${multa} (reais).')
else:
    print('Você está dentro do limite de velocidade!')
