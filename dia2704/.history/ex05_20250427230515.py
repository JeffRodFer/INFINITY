# Atividade 05:
# Contagem até o Número Inserido:
# Crie um programa que solicite um número ao usuário e use
# um laço while para contar de 1 até o número inserido,
# exibindo apenas os números ímpares.
cont = 0
n = int(input('Digite um numero acima de 20: '))
while cont > n:
  if cont % 2 == 1:
    cont += 1
    print(cont)
