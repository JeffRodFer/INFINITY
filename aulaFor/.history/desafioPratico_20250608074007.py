medias = []
classifica = []
times = [
  ('Jeff',[10, 12, 9]),
  ('Rodr', [11, 9, 13])
]
for equipes, pontuacao in times:
  media = sum(pontuacao) / len(pontuacao)
  medias.append((pontuacao, media))
  medias = sorted(medias:.2f)


print(medias)
print(equipes)
print(pontuacao)