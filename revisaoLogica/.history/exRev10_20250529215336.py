# 10 - Classificação de Notas:
# Crie um programa que solicite uma nota de 0 a 100
# e informe o conceito (A, B, C, D, F) com base na nota.


while True:
  n = intInput('Digite a nota: ')
  if n < 20:
    print('F')
  elif n > 21 and n < 40:
    print('D')
  elif n > 41 and n < 60:
    print('C')
  elif n > 61 and n < 80:
    print('B')
  elif n > 81 and n < 100:
    print('A')
  else: