# 9 - Categoria de Idade:
# Desenvolva um programa que peça a idade do usuário e
# informe se ele é criança, adolescente, adulto ou idoso.

i = int(input('Digie a sua idade: '))
if i <= 12:
  print(f'Criança')
elif i >= 13 and <= 17:
  print(f'Adolescente')
elif i >= 18 an d