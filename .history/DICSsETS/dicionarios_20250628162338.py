dicionarios = {
  'Instituição':'MP4/4',
  'Serviços':'Automação',
  'Ramo':'Web'
}
print(dicionarios)
print(type(dicionarios))
print(f'Tamanho: {len(dicionarios)}')
print(f'Lista chaves: {list(dicionarios)}') 
print(dicionarios['Ramo']) # Escolhe a chave a ser exibida
dicionarios['Ramo'] = 'HTML' # Aletra o valor da chave
print(dicionarios)