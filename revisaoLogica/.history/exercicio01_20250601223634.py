soma = 0

ini = int(input('Numero inicial: '))
fim = int(input('Numero final: '))

if fim > ini:
  ini = fim

for i in ranfe(fim, 1):
  if i % 2 == 0:
    