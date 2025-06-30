text = 'Programação em Python'
cont_vogais = 0
cont_cons = 0
for caract in text:
  if caract.lower() in 'aeiou':
    cont_vogais += 1
  elif caract.lower() in 'bcdfghjklmnpqrstvxywz':
    cont_cons += 1
print('Na frase: Programação em Python')
print(f'Numero de vogais é {cont_vogais}')
print(f'Numero de consoantes é {cont_cons}')
print()