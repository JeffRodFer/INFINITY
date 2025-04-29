# Atividade 03:
# Tabuada de um Número:
# Faça um programa que solicite um número ao usuário e use
# um laço while para exibir a tabuada desse número (de 1 a 10).
x = 0
n = 0
while n < 10:
  x = int(input('Digite um numero: '))
  n += 1
  res = x * n
  print(f'{x} x {n} = {res}')