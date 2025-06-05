#  Você está desenvolvendo um programa em Python para calcular a soma dos números pares dentro de um intervalo determinado pelo usuário. O programa deve solicitar ao usuário que insira dois números inteiros, representando o início e o fim do intervalo (inclusive).

# Utilize um loop 'for' para iterar sobre todos os números no intervalo e somar apenas os números pares. Implemente a estrutura 'else' para exibir uma mensagem indicando que não há números pares no intervalo, caso seja o caso.

# Ao final, exiba a soma dos números pares encontrados.

s = 0
ini = int(input('Numero inicial: '))
fin = int(input('Numero final: '))
if ini > fin:
  ini, fin = fin, ini
for i in range(ini, fin + 1):
  if i % 2 == 0:
    s = i
    print(i)

if s > 1:
  print('temos numeros pares')
else:
  print('Não há números pares no intervalo')

print('-----------------------------')
print(f'{s} é a soma dos pares')