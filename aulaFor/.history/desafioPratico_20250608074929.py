medias = []
classificacao = []
times = [
  ('Jeff',[11, 12, 14]),
  ('Rodr', [11, 9, 15])
]
for equipes, pontuacao in times:
  media = sum(pontuacao) / len(pontuacao)
  medias.append((equipes, media))
  medias.sort(key=lambda item: item[1], reverse=True)


print(medias)
print(equipes)
print(pontuacao)