# Atividade 07:
# Tabuada com Condicional:
# Faça um programa que solicite um número ao usuário e use
# um laço while para exibir a tabuada desse número (de 1 a 10),
# mas apenas para os resultados que forem múltiplos de 3.
cont = 0
resultado = 0
num = int(input("Enter a number: "))

  cont += 1
  resultado = num * cont
  print(f'{num} x {cont} = {resultado}')