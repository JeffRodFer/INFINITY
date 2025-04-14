# Atividade 07:
# Tabuada com Condicional:
# Faça um programa que solicite um número ao usuário e use
# um laço while para exibir a tabuada desse número (de 1 a 10),
# mas apenas para os resultados que forem múltiplos de 3.

num = int(input("Enter a number: "))
cont = 0
while cont < 10:
  cont += 1
  resultado = num * cont
  print(f'{num} x 