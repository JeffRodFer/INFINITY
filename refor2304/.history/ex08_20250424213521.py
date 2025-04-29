n = 0
soma = 0

while nt >= 0:
  nt = float(int('Digite a nota: '))
  if nt >= 0:
    media += nt
  else:
    print('Nota invalida!')
    
print(f'Média da notas {media}')