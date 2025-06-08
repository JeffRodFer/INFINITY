medias = []
times = [
  (['Jeff'],[10, 12]),
  ('Rodr', [9, 9]),
  ('Ferr', [11, 8]),
  ('Leoo', [13, 10])
]
for i, j in times:
  media = sum(j) / len(j)
  medias.append((j, media))
  medias



print(times[0][0], media)
print(sorted(medias))
print(medias[::-1])
print(sorted(medias[::-2]))
print(sorted(medias[::-3]))
# print(sorted(medias[::-4]))
