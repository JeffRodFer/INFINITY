# Atividade 07:
# Tabuada com Condicional:
# Faça um programa que solicite um número ao usuário e use
# um laço while para exibir a tabuada desse número (de 1 a 10),
# mas apenas para os resultados que forem múltiplos de 3.
res = 0
n = 0
while n < 11:
  n += 1
  res = n * n
print(f'{n}x{n}={res}')