# Faça um programa que use um laço while para exibir os
# primeiros 20 termos da sequência de Fibonacci.
# 3 - Sequência de Fibonacci:

a = 0
b = 0
n = 0
f = 0
cont = 0

while f < 20:
  print(f)
  f = f + b
  b = f - b

  if b ==