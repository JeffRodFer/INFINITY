text = 'Programação em Python'
cont_vogais = 0
for caract in text:
  if caract.lower() in 'aeiou':
    cont_vogais += 1
    