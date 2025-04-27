nt1 = float(input('Insira a nota1: '))
nt2 = float(input('Insira a nota2: '))
nt3 = float(input('Insira a nota3: '))
md = (n1 + n2 + n3) /3

if md >= 0 and nt <= 4:
  print(f'Nota {nt} = Reprovado.')
elif nt >= 5 and nt <= 6:
  print(f'Nota {nt} = Recuperaçãp')
elif nt >= 7 and nt <= 10:
  print(f'Nota {nt} = Aprovado.')
else:
  print(f'Nota Inválida! Refaça o processo.')
