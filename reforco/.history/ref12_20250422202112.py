nt = float(input('Insira uma nota: '))
if nt >= 0 and nt <= 4:
  print(f'Nota {nt} = Reprovado.')
elif nt >= 5 and nt <= 6:
  print(f'Nota {nt} = Recuperaçãp')
elif nt >= 7 and nt <= 10:
  print(f'Nota {nt} = Aprovado.')
else:
  print(f'Nota Inválida! Refaça o prcesso.')
