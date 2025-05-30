# 7 - Algoritmo de Conversão de Tempo:
# Desenvolva um algoritmo que converta uma quantidade de
# segundos fornecida pelo usuário em horas, minutos e segundos.
# h = 3.600   m = 60   s = 1

s = int(input('Insira:  '))
h = s // 3600
res = s % 3600
min = res // 60
s = res % 60

print(f'{h} horas {min} min {s}segundos'):