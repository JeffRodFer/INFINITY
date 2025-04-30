# Desenvolva um programa que solicite um número ao usuário
# e use um laço while para calcular o fatorial desse número.
# 4 - Fatorial de um Número:

v = 0
fat = 1
v = int(input('Digite um numero pra saber o fatorial: '))
while v > 1:
  fat = fat * v
  v = v - 1
  print
  print(v)
print(f'O fatorial de {v} é {fat}')