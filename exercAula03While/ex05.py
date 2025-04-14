# Atividade 05:
# Contagem até o Número Inserido:
# Crie um programa que solicite um número ao usuário e use
# um laço while para contar de 1 até o número inserido,
# exibindo apenas os números ímpares.


exib = 0
num = int(input("Enter a number: "))
cont = 0
while cont < num:
  cont += 1
  if cont % 2 == 1:
    print(cont)