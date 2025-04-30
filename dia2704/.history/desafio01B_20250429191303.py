# 1 - Números Pares em um Intervalo:
# Crie um programa que solicite dois números ao usuário,
# representando um intervalo. Use um laço while para exibir
# todos os números pares dentro desse intervalo.

n = int(input('Digite um numero: '))
v = int(input('Digite outro numero: '))

while n != v:
  
  n += 1
  if n % 2 == 0:
    print(n)