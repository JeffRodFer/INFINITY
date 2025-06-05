# Atividade 11:
# Verificar Múltiplos de 5 e Parar:
# Escreva um programa que use um laço for para imprimir números de 1 a 30.
# Use uma condicional para verificar se um número é múltiplo de 5 e outro
# para verificar se é maior que 20 e interromper o loop com break.

s = 0
n = int(input('Digite o local da trava: '))
for i in range(1, 20):
  if i % 3 == 0:
    s += i
    print(f'{i} Multiplo de 3')
  if i == n:
    print(f'{i} trava.')
    break

print(f'{s}')