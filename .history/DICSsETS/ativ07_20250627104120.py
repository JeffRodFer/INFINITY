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
computador['Placa video']= 'Gforce'
print(computador)
print(len(computador))
print('Placa video' in computador)
print(iter(computador))
print(list(iter(computador)))
sistema_computacional = computador.copy()
print(sistema_computacional)
# print(computador.get('CPU'))
# print(computador.get('Pmae'))
# print(computador.get('Pvideo','RAM'))
# print(dict.fromkeys(computador))

