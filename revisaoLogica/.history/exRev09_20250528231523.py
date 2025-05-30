# 9 - Verificar Signo:
# Escreva um programa que peça o dia e o mês de
# nascimento do usuário e informe o signo correspondente.

d = 0
m = 1
while True:
d = int(input('Insira o dia do nascimento: '))
m = int(input('Mês do nascimento: '))
  if (d >= 21 and m == 3) or (d <= 20 and m == 4):
    print('Áries')
  elif (d >= 21 and m == 4) or (d <= 20 and m == 5):
    print('Touro')
  elif (d >= 21 and m == 5) or (d <= 20 and m == 6):
    print('Cancer')
  elif (d >= 21 and m == 6) or (d <= 22 and m == 7):
    print('Gemeos')
  elif (d >= 23 and m == 7) or (d <= 22 and m == 8):
    print('Leão')
  elif (d >= 23 and m == 8) or (d <= 22 and m == 9):
    print('Virgem')
  elif (d >= 23 and m == 9) or (d <= 22 and m == 10):
    print('Libra')
elif (d >= 23 and m == 10) or (d <= 21 and m == 11):
  print('Escorpião')
elif (d >= 22 and m == 11) or (d <= 21 and m == 12):
  print('Sagitário')
elif (d >= 22 and m == 12) or (d <= 19 and m == 1):
  print('Aquário')
elif (d >= 20 and m == 1) or (d <= 18 and m == 2):
  print('Capricórnio')
elif (d >= 19 and m == 2) or (d <= 20 and m == 3):
  print('Peixes')
else:
  print('Data invalida.')