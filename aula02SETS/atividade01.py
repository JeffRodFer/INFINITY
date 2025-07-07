# Crie um conjunto vazio chamado frutas e adicione as
# seguintes frutas a ele: 'maçã', 'banana', 'uva', 'laranja', 'morango' em seguida imprima o conjunto

# frutas = set()

# while True:
#   opcao = int(input('Insira: '))
#   if opcao == 1:
#     frutas.update(['maçã', 'banana', 'uva', 'morango'])
#     print(frutas)
#   elif opcao == 11:
#     frutas.update(['abacaxi','mamão'])
#     print(frutas)
#   elif opcao == 111:
#     frutas.pop()
#     print(frutas)

    # 2 Verifique se a fruta 'banana' esta presente no conjunto fruta e imprima o resultado
# cesta = {'maçã', 'uva', 'pera', 'banana'}
# print('banana' in cesta)
# print('--' * 10)
# frutas_vermelhas = set()
# frut_verm = ['morango', 'cereja', 'framboesa']
# # cesta.update(frut_verm)
# # print(cesta)
# # cesta.remove('framboesa')
# print(cesta)
# print(cesta.union(frut_verm))
# 7 Escreva um programa que receba duas listas e calcule
# a união dos elementos únicos dessas listas, usando conjuntos.
# list1 = [1,1,1,2,3,5,6,6,9]
# list2 = [2, 2, 3, 4, 5, 6, 9]
# conj1 = set(list1)
# conj2 = set(list2)

# print(list1)
# print(list2)
# list_unida = conj1 | conj2
# print(list_unida)
# 8 Escreva um programa que EXIBA um dicionário contendo informações de pessoas (nome, idade) e exiba essas informações.
# 9 Escreva um programa que percorra as chaves e valores de um dicionário separadamente e os exiba.
# dic = {}
# dic_pc = {'CPU':'Intel', 'RAM':'16gb'}
# while True:
#   print('Adicione um novo item ou digite "Sair" para encerrar: ')
#   chave = input('Digite o nome: ').strip().lower()
#   if chave == 'sair':
#     break
#   valor = int(input('Digite o valor: '))
#   dic[chave] = valor

# for chaves in dic.keys(): # Ou usar o list ex: print(list(dic))
#   print(chaves)

# for valor in dic.values():
#   print(valor)

# print(dic)
# dic_pc['SSD'] = '480gb' # Adiciona chave e valor ao dicionario citado
# print(dic_pc)
# 10 Desenvolva um programa que recebe um dicionário, uma chave e um valor como entrada e adiciona a chave e o 
# valor ao dicionário, atualizando o valor se a chave já existir.
# dicionario = {
#   'Jeff': 30,
#   'Rodr': 23,
#   'Ferr': 21
# }
# while True:
#   chave = input('Digite a chave: ').strip()
#   valor = int(input('Digite o valor: '))
#   dicionario[chave] = valor
#   print(dicionario)
# 11 Escreva um programa que recebe um dicionário e uma lista de chaves como entrada e verifica se todas as
# chaves da lista existem no dicionário. A função deve retornar True se todas as chaves existirem e False caso contrário.
# dic_um = {'nome': 'jeff', 'idade': 30, 'cidade': 'americana'}
# lista_chaves = ['estado', 'sexo']

# print(f'Dicionario: {dic_um}')
# print(f'Chaves a verificar: {lista_chaves}')

# todas_presentes = True

# for chave in lista_chaves:
#   if chave not in dic_um.keys():
#     todas_presentes = True
#   else:
#     todas_presentes = False

# print(f'Resposta: {todas_presentes}')
 # 12 Crie um programa que simule um sistema de votação. O
# programa deve permitir que os eleitores escolham entre
# opções de eleitores e conte os votos para cada opção.
# Use um dicionário para armazenar os resultados da votação, onde as chaves são as opções e os valores são o número de votos para cada opção. O programa deve permitir que os eleitores votem, encerre a votação e exiba os resultados finais. Use While True e pare o programa somente se o usuário digitar o número 0 e exiba os resultados finais.

# candidatos = {
#   '1--jeff': 0,
#   '2--rodr': 0,
#   '3--ferr': 0
# }
# while True:
#   voto = int(input('Digite o seu voto: '))
#   if voto == 1:
#     candidatos['1--jeff'] += 1
#   elif voto == 2:
#     candidatos['2--rodr'] += 1
#   elif voto == 3:
#     candidatos['3--ferr'] += 1
#   elif voto == 0:
#     print('Votação encerrada.')
#     break
# print(candidatos)

# 13 Crie um dicionário que relacione nomes de alunos às suas notas em uma disciplina. Calcule a média das notas e exiba-a.

# alunos = {
#   'jeff': 8.4,
#   'rodr': 7.6,
#   'ferr': 7.8
# }
# soma_notas = 0.0
# qtd_alunos = 0

# for notas in alunos.values():
#   soma_notas += notas
#   qtd_alunos += 1

# if qtd_alunos > 0:
#   media_notas = soma_notas / qtd_alunos
#   print(f'A média das notas da turma é {media_notas:.2f}')
# else:
#   print('Sem alunos')

# 14 Crie um programa que receba uma lista de números e remova todas as duplicatas usando um conjunto (set). 
# Em seguida, exiba a lista original e a lista sem duplicatas.
# num = [2,3,5,2,6,3,6]
# num1 = set(num)

# print(num)
# print(num1)

# 15 Crie um programa que realize a união de múltiplos
# conjuntos e exiba o conjunto resultante.
# lista1 = {1, 2, 3, 4}
# lista2 = {4, 5, 6}
# lista3 = {6, 7, 4, 1}

# new_num = set(lista1 | lista2 | lista3)
# print(new_num)

# # 16 O programa deve permitir ao usuário
# cadastrar alunos. Cada aluno terá as seguintes
# informações: nome, idade e notas em três disciplinas: Matemática, Ciências e História. Os dados de cada aluno
# devem ser armazenados em um dicionário com as seguintes chaves: 'nome', 'idade', 'notas'. As notas devem ser armazenadas em uma tupla.

lista_alunos = []
while True:
  print('Novo Aluno: ')
  nome = input('Nome: ')
  if nome.lower() == 'fim':
    break

  while True:
    try:
      idade = int(input(f'Digite a idade de {nome}: '))
      if idade <= 0:
        print('A idade deve ser um numero positivo. Tente novamente.')
      else:
        break
    except ValueError:
      print('Idade inválida. Por favor, digite um numero inteiro.')

  notas_disc = []
  disciplinas = ['mat ', 'por ', 'geo ']

  for disciplina in disciplinas:
    while True:
      nota_str = input(f'{nome}: {disciplinas} ')
      nota = float(nota_str)
      if nota >= 0 and nota <= 10:
        notas_disc.append(nota)
        break
      else:
        print('Nota invalida')

  aluno = {
        'nome': nome,
        'idade': idade,
        'notas': tuple(notas_disc)
  }

  lista_alunos.append(aluno)
  # print(f'\n {aluno} cadastrado com sucesso.')

if not lista_alunos:
  print('Nenhum cadastrado!')
else:
  for aluno_cadastrado in lista_alunos:
      print(f'{nome} : {idade}')
      print(f'Notas (Matemática, Português e Geografia): {aluno_cadastrado['notas']}')
      print('--' * 6)