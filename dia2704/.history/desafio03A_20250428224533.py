# Faça um programa que use um laço while para exibir os
# primeiros 20 termos da sequência de Fibonacci.
# 3 - Sequência de Fibonacci:

a = 1
b = 1
n = 0
f = 0
cont = 0

while cont < 20:
  if cont < 20:
    n += 1
    f = a + b
    n += f
    print(f)