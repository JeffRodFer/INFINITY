media = []
times = [
  ('Jeff',[10, 12]),
  ('Rodr', [9, 9]),
  ('Ferr', [11, 8]),
  ('Leoo', [12, 10])
]
for i, j in times:
  media = sum(j) / len(j)
  media.append(i, media)



print(media)