soma = 0
v = 0
ma = 0
me = 0
numeros = [6, 2, 3, 1, 9, 6, 7, 3]

for n in numeros:
  soma += n
  if n > v:
    ma = n
  elif n > ma:
    ma = v
  elif n < ma:
    me = v

print(ma)
print(me)
print