print('------------ CONSULTA PREÇO CONVERTIDO -------------')
preco = float(input('Insira o valor do produto: R$ '))
dollar = float(5.85)
if preco <= 5.00:
  print(f'Valor R${preco} Produto barato')
  print(f'No dolar atual custa ${preco / dollar:.2f}')
elif preco > 5.00 and preco <= 15.00:
  print(f'Valor R${preco} Produto de médio valor')
  print(f'No dolar atual custa ${preco / dollar:.2f}')
elif preco >= 15.00 and preco <= 20.00:
  print(f'Valor R${preco} Produto de preço alto.')
  print(f'No dolar atual custa ${preco / dollar:.2f}')
else:
  print(f'Valor R${preco} Produto caro')
  print(f'No dolar atual custa ${preco / dollar:.2f}')