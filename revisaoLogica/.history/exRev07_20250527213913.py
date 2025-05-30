# 7 - Algoritmo de Conversão de Tempo:
# Desenvolva um algoritmo que converta uma quantidade de
# segundos fornecida pelo usuário em horas, minutos e segundos.
# h = 3.600   m = 60   s = 1

while True:
  entr_seg_str = input('Insira os segundos: ')

  eh_num = True
  if not entr_seg_str.isdigit():
    if len(entr_seg_str) > 1 and entr_seg_str[0] == '-' and entr_seg_str[1:].isdigit():
      eh_num = True
    else:
      eh_num = False

    if eh_num:
      total_seg = int(entr_seg_str)
      if total_seg >= 0:
        break
      else:
        print('A quantidade de segundos não pode ser negativa')
    else:
      print('Entrada invalida.')


h = 0
m = 0
seg_fin = 0

while seg_rest >= 3600:
  h = h + 1
  