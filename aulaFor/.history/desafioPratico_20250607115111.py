medias = []
times = [
  (['Jeff'],[10, 12]),
  ('Rodr', [9, 9]),
  ('Ferr', [11, 8]),
  ('Leoo', [12, 10])
]
for i, j in times:
  media = sum(j) / len(j)
  medias.append((j, media))



print(times[0], media)
# print(medias)