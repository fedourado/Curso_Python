# Crie um programa que leia o nome completo da pessoa: - O nome com todas as letras maiúsculas.
#  O nome com todas as letras minúsculas;
#  Quantas letras ao todo (sem considerar espaços);
#  Quantas letras tem o primeiro nome.

# Quando coloca o método depois do input, ele irá excluir os espaços desnecessários
nome = input('Digite seu nome completo: ').strip()

print('\nAnalisando seu nome...')

print('Seu nome em maiúsculo é',nome.upper()+'.')

print('Seu nome em minúsculo é',nome.lower()+'.')

# total_no_space = nome.replace(' ','')
print('Seu nome tem',len(nome.replace(' ','')),'letras.')

first_name = nome.split()
print('Seu primeiro nome é',first_name[0],'e ele tem',len(first_name[0]),'letras.')





