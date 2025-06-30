# 15 - Soma de Números Pares:
# Crie um programa que use um laço while para somar
# todos os números pares de 1 a 100 e exiba o resultado.


s = 0
c = 0
# n = int(input('Digite um numero: '))
while c <= 100:
  c += 1
  if c % 2 == 0:
    s += c
    print(s)