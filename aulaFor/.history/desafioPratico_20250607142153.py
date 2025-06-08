medias = []
classifica = []
times = [
  (['Jeff'],[10, 12]),
  (['Rodr'], [9, 9]),
  (['Ferr'], [11, 8]),
  (['Leoo'], [13, 10])
]
for i, j in times:
  media = sum(j) / len(j)
  medias.append((j, media))
  medias = sorted(medias)

for media in medias:
  # if media in medias:
    # continue
  classifica.append(medias)

print(times, i, medias)
print(reversed(medias))
print(classifica)