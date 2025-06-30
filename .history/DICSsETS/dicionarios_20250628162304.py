dicionarios = {
  'Instituição':'MP4/4',
  'Serviços':'Automação',
  'Ramo':'Web'
}
print(dicionarios)
print(type(dicionarios))
print(f'Tamanho: {len(dicionarios)}')
print(f'Lista chaves: {list(dicionarios)}')
print(dicionarios['Ramo']) # Escol
dicionarios['Ramo'] = 'HTML'
print(dicionarios)