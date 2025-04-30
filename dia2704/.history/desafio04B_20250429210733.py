# 4 - Sequência de Collatz:
# Crie um programa que solicite um número ao usuário e use um
# laço while para gerar e exibir a sequência de Collatz até chegar
# ao número 1.
s  = 0
ss = 0
n = float(input('Digite um numero: '))
while n > 1:
  n += 1
  if n % 2 == 0:
    s = n + (n / 2)
    print(f'{s} par')
  ele