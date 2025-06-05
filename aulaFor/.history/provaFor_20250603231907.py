#  Você está desenvolvendo um programa em Python para calcular a soma dos números pares dentro de um intervalo determinado pelo usuário. O programa deve solicitar ao usuário que insira dois números inteiros, representando o início e o fim do intervalo (inclusive).

# Utilize um loop 'for' para iterar sobre todos os números no intervalo e somar apenas os números pares. Implemente a estrutura 'else' para exibir uma mensagem indicando que não há números pares no intervalo, caso seja o caso.

# Ao final, exiba a soma dos números pares encontrados.
c = 0
p = 0
s = 0
ini = int(input('Numero inicial: '))
fin = int(input('Numero final: '))
if ini > fin:
  ini, fin = fin, ini
for i in range(ini, fin + 1):
  if ini == 0 and fin == 1:
    print('Sem numeros pares.')

  if i % 2 == 0:
    c += 1
    s = i + i
  # if s >= 2:
  #   print(f'Temos numeros pares.')
else:
  print('Nenhum par')

print('-----------------------------')
print(f'{s} é a soma dos pares')