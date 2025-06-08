medias = []
classifica = []
times = [
  ('Jeff',[11, 12, 14]),
  ('Rodr', [11, 9, 15])
]
for equipes, pontuacao in times:
  media = sum(pontuacao) / len(pontuacao)
  medias.append((equipes, media))
  medias.sort(medias)


print(medias)
print(equipes)
print(pontuacao)