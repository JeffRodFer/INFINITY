# 7 - Algoritmo de Conversão de Tempo:
# Desenvolva um algoritmo que converta uma quantidade de
# segundos fornecida pelo usuário em horas, minutos e segundos.
# h = 3.600   m = 60   s = 1
h = 0
cm = 0
s = 1
t = 0

s = int(input('Quantidade de segundos: '))
s = s / 60
if s > 60:
  m += 1
  m = (s * 60) 
print(s)
print(m)

240