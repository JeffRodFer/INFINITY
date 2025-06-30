# Atividade 07:
# Contagem de Vogais em uma Palavra:
# Crie um programa que solicite uma palavra ao usuário e use um laço for com
# uma condicional para contar quantas vogais (a, e, i, o, u) a palavra contém.


word =  'Patati caiu e o Patata voou!'
v = 0
c = 0

for letter in word:
  if letter.lower() in 'aeiou':
    v += 1
  else:
    c += 1
    
print('Na frase: Patati caiu e o Patata voou!')
print(f'existem {v} vogais.')
print(f'existem {v} vogais.')