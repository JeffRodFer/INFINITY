# 7 - Algoritmo de Conversão de Tempo:
# Desenvolva um algoritmo que converta uma quantidade de
# segundos fornecida pelo usuário em horas, minutos e segundos.
# 
h = 3.600
m = 60
s = 1
t = 0

s = int(input('Quantidade de segundos: '))
while True:
  t = int(input('Insira o tempo: '))
  if t % 60 == 0:
    m += 1
