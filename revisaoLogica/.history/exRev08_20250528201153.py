# 8 - Algoritmo de Conversão de Temperatura:
# Crie um algoritmo que converta uma temperatura de Celsius
# para Fahrenheit. Solicite ao usuário a temperatura em Celsius
# e exiba o resultado em Fahrenheit. F = C x 1,8 + 32.
t = 0
c = 0
f = 0
while True:
  t = int(input('Insera a temperatura em graus Celsius: '))
  f = t * 1.8 + 32
  if f < 40:
    print(f'Frio {f:.1}')
  elif f > 41 and f < 60:
    print(f'Amena {f:.1}')
  else:
    print(f'Calor {f:.1}')