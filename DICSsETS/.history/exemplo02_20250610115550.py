set1 = {1, 2, 3}
set2 = {'a', 'b', 'c'}
convidados = {'Jeff', 'Rod', 'Ferr'}
convidados2 = {'Jeff', 'Rodrigo', 'Ferreira'}
convidados3 = {'Rod', 'Jefferson', 'Ferreira'}
convidados2.intersection_update(convidados3)
print(convidados.intersection(convidados2))
print(convidados3)
print(set1.union(set2))
print(set2 | set1)