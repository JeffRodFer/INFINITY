dicionarios = {
  'Instituição':'MP4/4',
  'Serviços':'Automação',
  'Ramo':'Web'
}
print(dicionarios)
print(type(dicionarios))
print(f'Tamanho: {len(dicionarios)}') # Tamanho d
print(f'Lista chaves: {list(dicionarios)}') # Mostra as chaves da lista
print(dicionarios['Ramo']) # Escolhe a chave a ser exibida
dicionarios['Ramo'] = 'HTML' # Aletra o valor da chave
print(dicionarios)