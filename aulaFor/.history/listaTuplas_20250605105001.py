for num in range(2, 20):
  for i in range(2, num):
    if num % i == 0:
      break
  else:
    print(f'{i} é um numero primo.')
