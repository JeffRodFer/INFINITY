# Atividade 12:
# Soma de Números com Desconto:
# Peça ao usuário para inserir 5 preços de produtos. Use um laço for para
# calcular o total. Aplique um desconto de 10% se o total ultrapassar 100 e
# interrompa o loop com break.
pp = 0
pt = 0
for i in range(5):
  pp = float(input('Preços: '))
  pt += pp
  if pt >= 100:
    pt = pt * 0.1
    print(f'Preço com desconto R${pt:.2f}')
  else:
    print(f'Preço normal R${pt:.}')
