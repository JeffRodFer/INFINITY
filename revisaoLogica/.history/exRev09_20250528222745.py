# 9 - Verificar Signo:
# Escreva um programa que peça o dia e o mês de
# nascimento do usuário e informe o signo correspondente.

d = 0
m = 1
d = int(input('Insira o dia do nascimento: '))
m = input('Mês do nascimento: ')
if m == 1 and (d >= 1 and d <= 20):
  print('Áries')
elif m == 2 and (d > 21 and d <= 20):
  print('Touro')
elif m == 3 (d > 21 and d < 20):
  print('Cancer')
elif m == 4 and (d > 21 and d < 20):
  print('Gemeos')
elif m == 5 and (d > 21 and d < 20):
  print('Leão')
elif m == 6 (d > 20 and d < 21):
  print('Virgem')
elif m == 7:
  print('Jul')
elif m == 8:
  print('Ago')
elif m == 9:
  print('Set')
elif m == 10:
  print('Out')
elif m == 11:
  print('Nov')
else:
  print('Dez')