medias = []
classifica = []
times = [
  ('Jeff',[10, 12, 9]),
  ('Rodr', [11, 9, 13])
]
for equipes, pontua in times:
  media = sum(j) / len(j)
  medias.append((j, media))
  medias = sorted(medias)


print(medias)
print(i)
print(j)