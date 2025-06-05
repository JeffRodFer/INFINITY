num_alunos = int(input("Digite o número de alunos: "))
media_turma_total = 0

print("-" * 30)

for i in range(1, num_alunos + 1):
    print(f"\nAluno {i}:")
    nome = input("Digite o nome do aluno: ")
    
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))
    
    media_aluno = (nota1 + nota2 + nota3) / 3
    media_turma_total += media_aluno
    
    print(f"\nNotas de {nome}: {nota1}, {nota2}, {nota3}")
    print(f"Média de {nome}: {media_aluno:.2f}")
    
    if media_aluno >= 7.0:
        print(f"{nome} está APROVADO(A)!")
    else:
        print(f"{nome} está REPROVADO(A)!")
    
    print("-" * 30)

media_geral_turma = media_turma_total / num_alunos
print(f"\nMédia geral da turma: {media_geral_turma:.2f}")