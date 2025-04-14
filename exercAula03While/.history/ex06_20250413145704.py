# Atividade 06:
# Soma de Números Positivos:
# Escreva um programa que solicite números ao usuário até
# que ele digite um número negativo, somando apenas os
# números positivos inseridos.
num = int(input("Enter a number: "))
soma = 0
while num > 0:
  if num > 0:
    num += 1
  print(soma)