# 6 - Algoritmo de Cálculo de Desconto:
# Desenvolva um algoritmo que calcule o preço de um produto
# após aplicar um desconto. Solicite o preço original e o percentual
# de desconto.


pre_fin = 0
porc_desc = 0

pre_ini = float(input('Preço do produto: '))
if pre_ini < 99:
  desc = 0
elif pre_ini > 100:
  desc = 5
elif pre_ini > 200:
  desc =  7
elif pre_ini > 350:
  desc = 10
else:
  desc = 12

pre_fin = pre_ini - ((pre_ini)  desc )    

