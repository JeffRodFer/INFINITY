# 3 - Imprimir números pares: Peça ao usuário um número inteiro positivo N. Use um while para imprimir todos os números pares de 0 até N (inclusive, se for pares.

n = int(input('Digite um numero: '))
while n != 0:
  if n % 2 == 0:
    n -= 1

