# Faça um programa que use um laço while para exibir os
# primeiros 20 termos da sequência de Fibonacci.
# 3 - Sequência de Fibonacci:

a = 1
b = 1
n = 0
f = 0
cont = 0

while f < 20:
  n += 1
  f = f(n - 1) + f(n - 2)
  print(n)