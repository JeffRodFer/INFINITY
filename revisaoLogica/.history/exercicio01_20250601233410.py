soma = 0

ini = int(input('Numero inicial: '))
fim = int(input('Numero final: '))

if fim < ini:
  print
  break

for i in range(ini, fim):
  if i % 2 == 0:
    soma += i
else:
  print(f'Não há numeros pares no intervalo.{soma}')
  print(ini)
  print(fim)


print(soma)