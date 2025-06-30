dicionarios = {
  'Instituição':'MP4/4',
  'Serviços':'Automação',
  'Ramo':'Web',
  'Tipo':'Manutenção'
}
print(dicionarios)
print(type(dicionarios)) # Mostra o tipo do dicionario
print(f'Tamanho: {len(dicionarios)}') # Tamanho do dicionario
print(f'Lista chaves: {list(dicionarios)}') # Mostra todas as chaves do dicionario
print(dicionarios['Ramo']) # Escolhe a chave a ser exibida
dicionarios['Ramo'] = 'HTML' # Altera o valor da chave
print(dicionarios['Ramo']) # Escolhe a chave a ser exibida
print(iter(dicionarios))
print('Arrecadação' not in dicionarios) # Verifica se a chave citada não está no dicionario
copia_dicionario = dicionario.copy() # Copia o dicionario como copia
print(copia_dicionario)
