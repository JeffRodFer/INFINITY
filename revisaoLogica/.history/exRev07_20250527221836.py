# 7 - Algoritmo de Conversão de Tempo:
# Desenvolva um algoritmo que converta uma quantidade de
# segundos fornecida pelo usuário em horas, minutos e segundos.
# h = 3.600   m = 60   s = 1

seconds = seconds % (24 * 3600)
hour = seconds // 3600
seconds = seconds % 3600
minutes = seconds // 60
seconds = seconds % 60