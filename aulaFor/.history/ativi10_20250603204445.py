# Atividade 10:
# Contar Números Positivos e Negativos: Peça ao usuário para inserir 10 números. Use um laço for com condicionais para contar quantos
# são positivos e quantos são negativos. Pare o loop se o número 0 for inserido, usando break.


po = 0
ne = 0
for i in range(10):
  n = int(input('Numero: '))
  if i > 0:
    po += 1
  if i < 0:
    ne += 1

    