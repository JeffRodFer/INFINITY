# acesso = '12qw'
# chance = ''
# cont = 0

# while chance != acesso:
#   chance = input('Digite a chave: ')
#   if chance == acesso:
#     print('---- Seja bem-vindo!! ----')
#     break
#   else:
#     print('Errou, tente novamente!')


num_sec = '12qwe'
tentativas = 3
jog1 = 0
jog2 = 0
chances1 = 0
chances2 = 0

while jog1 < tentativas and jog2 <= tentativas:
  jog1 = int(input('Chances jogador1: '))
  jog1 += 1
  if jog1 == num_sec:
    print('Acertou!!')
    break
  else:
    print('Jogador1 tente novamente')

  jog2 = int(input('Chances jogador2: '))
  jog2 += 1
  if jog2 == num_sec:
    print('Acertou!!')
    break
  else:
    print('Jogador2 tente novamente')