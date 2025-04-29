# Atividade 03:
# Tabuada de um Número:
# Faça um programa que solicite um número ao usuário e use
# um laço while para exibir a tabuada desse número (de 1 a 10).

cont = 0
resu = 0
n = int(input('Digite um numero: '))
while cont <= 9:
  cont += 1
  resu = cont * n
  print(f'{cont} x {n} = {resu}')