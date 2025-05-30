# 7 - Algoritmo de Conversão de Tempo:
# Desenvolva um algoritmo que converta uma quantidade de
# segundos fornecida pelo usuário em horas, minutos e segundos.
# h = 3.600   m = 60   s = 1


n = int(input('Insira:  '))


seconds = seconds % (24 * 3600)
hour = seconds // 3600
seconds = seconds % 3600
minutes = seconds // 60
seconds = seconds % 60

def convert_to_preferred_format(sec):
   sec = sec % (24 * 3600)
   hour = sec // 3600
   sec %= 3600
   min = sec // 60
   sec %= 60
   print("seconds value in hours:",hour)
   print("seconds value in minutes:",min)
   return "%02d:%02d:%02d" % (hour, min, sec) 

# n = 10000
# print("Time in preferred format :-",convert(n))
    print(n)