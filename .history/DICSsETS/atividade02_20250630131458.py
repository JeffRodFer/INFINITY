valor = 0
valor_maior = 0
valor_menor = 0
c = 0
while c < 3:
  valor = int(input('Digite um numero: '))
  c += 1
  if valor > valor:
    valor_maior = valor
  elif valor > valor_maior:
    valor_maior = valor
  elif valor < valor_maior:
    valor_menor = valor

print(f'Maior valor é: {valor_maior} ')
print(f'Menor valor é: {valor_menor} ')
