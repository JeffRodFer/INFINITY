# 9 - Verificar Signo:
# Escreva um programa que peça o dia e o mês de
# nascimento do usuário e informe o signo correspondente.

d = 0
m = 1
d = int(input('Insira o dia do nascimento: '))
m = int(input('Mês do nascimento: '))
if (d >= 21 and m 3) or (dia <= 20 and m == 4):
  print('Áries')
elif (d >= 21 and m 4) or (dia <= 20 and m == 5):
  print('Touro')
elif (d >= 21 and m 5) or (dia <= 20 and m == 6):
  print('Cancer')
elif (d >= 21 and m 6) or (dia <= 22 and m == 7):
  print('Gemeos')
elif (d >= 21 and m 7) or (dia <= 22 and m == 8):
  print('Leão')
elif (d >= 21 and m 8) or (dia <= 22 and m == 9):
  print('Virgem')
elif (d >= 21 and m 9) or (dia <= 22 and m == 10):
  print('Libra')
elif (d >= 21 and m 10) or (dia <= 21 and m == 11):
  print('Escorpião')
elif (d >= 21 and m 11) or (dia <= 21 and m == 12):
  print('Sagitário')
elif (d >= 21 and m 12) or (dia <= 19 and m == 1):
  print('Aquário')
elif (d >= 21 and 1) or (dia <= 18 and m == 2):
  print('Capricórnio')
elif (d >= 21 and m 2) or (dia <= 20 and m == 3):
  print('Peixes')
else:
  print('Data invalida.')