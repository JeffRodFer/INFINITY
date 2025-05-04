# Atividade 11:
# Verificar Múltiplos de 5 e Parar:
# Escreva um programa que use um laço for para imprimir números de 1 a 30.
# Use uma condicional para verificar se um número é múltiplo de 5 e outro
# para verificar se é maior que 20 e interromper o loop com break.
c = 0
n = 0
ts = 0
kg = 0
for i in range(30):
  if i % 5 == 0 and i > 20:
    ts += 1
    print(f'Twice status.')
  else:
    
    print('Keep  going!')
print
  