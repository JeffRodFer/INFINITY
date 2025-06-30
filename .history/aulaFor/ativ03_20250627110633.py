# Atividade 03:
# Caractere por Caractere:
# Escreva um programa que solicite uma palavra ao usuário e use um
# laço for para exibir cada caractere da palavra em uma linha separada.
while True:
  word = input('Digite uma palavra: ')
  for letter in word:
    print(letter)