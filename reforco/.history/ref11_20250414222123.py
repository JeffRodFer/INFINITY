print('-----Verificação de faixa etária-----')
nome = input('Digite o seu nome:  ')
idade = int(input('Digite a sua idade:  '))
if idade < 0:
  print('Não nascido')
if idade >= 0 and idade <= 12:
  print(f'{nome} você ainda é uma criança.')
elif idade >= 13 and idade <= 19:
  print(f'{nome} você é adolescente.')
elif idade >= 19 and idade <= 64:
  print(f'{nome} você é um adulto')
else:
  print(f'{nome} você é idoso.')