# 9 - Verificar Signo:
# Escreva um programa que peça o dia e o mês de
# nascimento do usuário e informe o signo correspondente.

d = 0
m = 1
d = int(input('Insira o dia do nascimento: '))
m = int(input('Mês do nascimento: '))
if m == 1 and (d > 1 and d < 20):
  print('Áries')
elif m == 2 and (d < 21 and d >20):
  print('Touro')
elif m == 3 and (d < 21 and d > 20):
  print('Cancer')
elif m == 4 and (d > 21 and d < 20):
  print('Gemeos')
elif m == 5 and (d > 21 and d < 20):
  print('Leão')
elif m == 6 and (d > 20 and d < 21):
  print('Virgem')
elif m == 7 and (d > 20 and d < 21):
  print('Libra')
elif m == 8 and (d > 20 and d < 21):
  print('Escorpião')
elif m == 9 and (d > 20 and d < 21):
  print('Sagitário')
elif m == 10 and (d > 20 and d < 21):
  print('Aquário')
elif m == 11 and (d > 20 and d < 21):
  print('Capricórnio')
else:
  print('Peixes')