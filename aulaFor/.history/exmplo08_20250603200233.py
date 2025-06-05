for n in range(1, 20):
  if n % 2 == 0:
    continue
  if n % 3 == 0:
    print(f'Numero {n} é o primeiro divisivel por 3 (e não é divisivel por 2')
    break
  print(f'Numero não divisivel por 2 {n}')