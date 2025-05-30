# 7 - Algoritmo de Conversão de Tempo:
# Desenvolva um algoritmo que converta uma quantidade de
# segundos fornecida pelo usuário em horas, minutos e segundos.
# h = 3.600   m = 60   s = 1

h = 3600
m = 60
s = 1

t = int(input('Insira os segundos: '))
h = t / 3600
m = (h - 3600) 

print(h)
print(m)
print(s)