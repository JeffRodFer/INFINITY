media = 0
cont = 0
nt = 1
while nt >= 0:
  nt = float(input('Digite a nota: '))
  if nt >=0:
    cont += 1
    media += nt
  else:
    print(f'A média é {media / cont}')
    if media <= 4:
      print('Reprovado.')
    elif media >= 5 and media <= 7:
      print('Recuperação.')
    elif media >= 8 and media <= 10:
      print('Aprovado!')
      
