medias = []
classificacao = []
times = [
  ('Jeff',[11, 12, 14, 12]),
  ('Rodr', [11, 9, 15, 12]),
  ('Ferr', [12, 10, 14, 11]),
  ('Leoo', [13, 10,13, 13]),
  ('Cebb',[14, 10, 13, 12])
]
for equipes, pontuacao in times:
  media = sum(pontuacao) / len(pontuacao)
  medias.append((equipes, media))
  medias.sort(key=lambda item: item[1], reverse=True)

  classificacao = medias
print(10 * '--', 'RESULTADO FINAL', '--' * 10)
for i, (equipes, media) in enumerate(classificacao):
  print(f'{i + 1} - {equipes} = {media:.2f}')

