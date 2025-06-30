# Atividade 07:
# Contagem de Vogais em uma Palavra:
# Crie um programa que solicite uma palavra ao usuário e use um laço for com
# uma condicional para contar quantas vogais (a, e, i, o, u) a palavra contém.


# word =  'Patati caiu e o Patata voou!'
v = 0
c = 0
word = input('Insira a frase: ')
for letter in word:
  if letter.lower() in 'aeiou':
    v += 1
  elif letter.lower() in 'bcdfghjklmnpqrstvxyz':
    c += 1
    
print(f'Na frase: {word}')
print(f'existem {v} vogais.')
print(f'existem {c} consoantes.')