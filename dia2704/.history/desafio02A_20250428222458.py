# 2 - Números Ímpares de 1 a 50:
# Escreva um programa que use um laço while
# para exibir todos os números ímpares de 1 a 50.

n = 0
res 
while n < 50:
  n = int(input('Digite um numero: '))
  if n % 2 == 1:
    n += 1
    print(n)