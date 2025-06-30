medias = []

times = [
    ('sport', [10, 20]),
    ('cruz', [13, 18])
    ]

valor1 = times[0][1][0]
valor2 = times[0][1][1]

soma1 = valor1 + valor2
media1 = soma1 / 2

valor3 = times[1][1][0]
valor4 = times[1][1][1]

soma2 = valor3 + valor4
media2 = soma2 / 2

medias.append(media2)
medias.append(media1)
print(medias)

if media1 > media2:
    print(media2, media1)
else:
    print(media1, media2)