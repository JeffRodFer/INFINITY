soma = 0

ini = int(input('Numero inicial: '))
fim = int(input('Numero final: '))

if fim > ini:
  ini = fim

for i in range(fim, ini, 1):
  if i % 2 == 0:
    soma += i
  else:
    print(f'Não há numeros pares no intervalo.{soma}')
print(soma)
  print(soma)


print(soma)