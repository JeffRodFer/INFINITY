# 17 - Verificação de Palíndromo:
# Escreva um programa que solicite uma palavra ao usuário e
# use um laço while para verificar se a palavra é um palíndromo
# (lê-se da mesma forma de trás para frente).

palavra = ''
word = input('Word: ')
while palavra != word:
  palavra = input('Digite a palavra: ')
  if palavra == word:
    print('Acertou!')
  
for palavra in word:
  print(palavra)

for palavra in len(pala)