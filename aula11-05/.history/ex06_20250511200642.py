# Atividade 06:
# Soma de Números Positivos:
# Escreva um programa que solicite números ao usuário até
# que ele digite um número negativo, somando apenas os
# números positivos inseridos.
s = 0
n = 0
while n > 0:
  n = int(input('Digite: '))
  if n > 0:
    s = n + n
  

print(f'Soma {s}')