# Atividade 12:
# Senha Correta:
# Desenvolva um programa que peça ao usuário para digitar uma
# senha e continue pedindo até que a senha correta (previamente
# definida) seja inserida.

senha = '12qwer'
chance  = 0
while chance != senha:
  chance = input('Digite a senha')
  if chance != senha:
    print('Errou.')
  else:
    print('--- ACERTOU ---')