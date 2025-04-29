# Atividade 06:
# Soma de Números Positivos:
# Escreva um programa que solicite números ao usuário até
# que ele digite um número negativo, somando apenas os
# números positivos inseridos.
cont = 0
soma = 0
n = 0
while n >= 0:
  n = int(input('Digite um numero: '))
  if n > 0:
    cont += 1
    soma += n
print(f'{soma) 
  