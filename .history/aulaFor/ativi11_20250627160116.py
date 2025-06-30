# Atividade 12:
# Soma de Números com Desconto: Peça ao usuário para inserir 5 preços de produtos. Use um laço for para
# calcular o total. Aplique um desconto de 10% se o total ultrapassar 100 e
# interrompa o loop com break.

prf = 0
pr = 0
soma = 0
tx = 10

for i in range(5):
  pr = float(input('Valor do produto: R$'))
  soma += pr
  if soma > 100:
    break
if soma >= 100:
  prf = (soma / 100) * 90
  print(f'Valor final: R${prf:.2f}')


print(f'Valor a pagar: R${soma.:2f}')