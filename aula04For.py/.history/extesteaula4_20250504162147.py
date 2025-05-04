# Você está desenvolvendo um programa em Python para calcular a soma dos números pares dentro de um intervalo determinado pelo usuário. O programa deve solicitar ao usuário que insira dois números inteiros, representando o início e o fim do intervalo (inclusive).

# Utilize um loop 'for' para iterar sobre todos os números no intervalo e somar apenas os números pares. Implemente a estrutura 'else' para exibir uma mensagem indicando que não há números pares no intervalo, caso seja o caso.

ini = int(input('Digite o inicio: '))
fim = int(input('digite o fina: '))
if fim >= ini:
  ini = fim + 20

for i in range(fim, ini):
  if i % 2 == 0:
    

  print(i)
