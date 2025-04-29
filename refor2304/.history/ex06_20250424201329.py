# Atividade 06:
# Soma de Números Positivos:
# Escreva um programa que solicite números ao usuário até
# que ele digite um número negativo, somando apenas os
# números positivos inseridos.
soma = 0
n = 1
while n >= 0:
  n = int(input('Digite um numero: '))
  if n >= 0:
    n = n += n
  else:
    print(f'A soma é {soma}')