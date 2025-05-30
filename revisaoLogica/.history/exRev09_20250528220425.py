# 9 - Verificar Signo:
# Escreva um programa que peça o dia e o mês de
# nascimento do usuário e informe o signo correspondente.

d = 0
m = 1
d = int(input('Insira o dia do nascimento: '))
m = input('Mês do nascimento: ')
if m == 1 and (d >= 1 and d <= 20):
  print('')
elif m == 2:
  print('Fev')
elif m == 3:
  print('Mar')
elif m == 4:
  print('Abr')
elif m == 5:
  print('Mai')
elif m == 6:
  print('Jun')
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