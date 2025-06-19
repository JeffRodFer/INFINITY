dic_info = {
  'nome': 'Jeff',
  'idade': 30,
  'sexo': 'M',
  'estado': 'casado',
  'profissao': 'autonomo'
}
print(dic_info['nome'])
print(dic_info['sexo'])
print(list(dic_info))
print(dic_info['estado'])
computador = {'CPU': 'Intel', 'RAM': '16gb', 'SSD': '480'}
computador['Pvideo']= 'Gforce'
print(computador)
print(len(computador))
print('Pvideo' in computador)
print(iter(computador))
print(list(iter(computador)))
sistema_computacional = computador.copy()
print(sistema_computacional)
print(computador.get('CPU'))
print(computador.get('Pmae'))
