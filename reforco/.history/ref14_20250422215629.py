print('------------ CONSULTA PREÇO CONVERTIDO -------------')
preco = float(input('Insira o valor do produto: '))
dollar = float(5.85)
if preco <= 5:
  print(f'Valor R${preco} Produto barato')
  print(f'No dollar atual custa ${preco / dollar}')
elif preco >= 10 and preco <= 15
