# Atividade 12:
# Soma de Números com Desconto: Peça ao usuário para inserir 5 preços de produtos. Use um laço for para
# calcular o total. Aplique um desconto de 10% se o total ultrapassar 100 e
# interrompa o loop com break.

prf = 0
pr = 0
soma = 0

for i in range(5):
  pr = float(input('Valor do produto: '))
  soma += pr
  