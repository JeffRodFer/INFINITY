# 9 - Categoria de Idade:
# Desenvolva um programa que peça a idade do usuário e
# informe se ele é criança, adolescente, adulto ou idoso.
i = 0

while True:
  i = int(input('Digie a sua idade: '))
if i <= 12:
  print(f'Criança.')
elif i >= 13 and i <= 17:
  print(f'Adolescente.')
elif i >= 18 and i <= 29:
  print(f'Adulto novo.')
elif i >= 30 and i <= 50:
  print(f'Adulto maduro.')
else:
  print(f'Idoso Completo.')
