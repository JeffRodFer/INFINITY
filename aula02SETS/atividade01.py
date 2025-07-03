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
dic_um = {'nome': 'jeff', 'idade': 30, 'cidade': 'americana'}
lista_chaves = ['estado', 'nome']
todas_presentes = True

print(f'Dicionario: {dic_um}')
print(f'Chaves a verificar: {lista_chaves}')

for chave in lista_chaves:
  if chave not in dic_um:
    todas_presentes = True
    break
  else:
    todas_presentes = False

print(f'Resposta: {todas_presentes}')
 