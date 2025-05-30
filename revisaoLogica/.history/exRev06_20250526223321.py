# 6 - Algoritmo de Cálculo de Desconto:
# Desenvolva um algoritmo que calcule o preço de um produto
# após aplicar um desconto. Solicite o preço original e o percentual
# de desconto.


pre_fin = 0
porc_desc = 0

pre_ini = float(input('Preço do produto: '))
if pre_ini < 99:
  desc = 0
elif pre_ini >= 100 and pre_ini < 199:
  desc = 5
elif pre_ini >= 200 and pre_ini < 349:
  desc =  7
elif pre_ini > 350 and pre_ini < 499:
  desc = 10
else:
  desc = 12

pre_fin = pre_ini - (pre_ini * (desc / 100))

print(f'produto com desconto R${pre_fin} ')

