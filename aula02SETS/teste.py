# Lista principal para armazenar todos os dicionários de alunos
lista_de_alunos = []

print("--- Cadastro de Alunos ---")

# Loop para permitir o cadastro de múltiplos alunos
while True:
    print("\n--- Novo Aluno ---")

    # 1. Coletar o nome do aluno
    nome_aluno = input("Digite o nome do aluno (ou 'fim' para sair): ")
    if nome_aluno.lower() == 'fim':
        break # Sai do loop se o usuário digitar 'fim'

    # 2. Coletar a idade do aluno
    # Usamos um loop para garantir que a idade seja um número válido
    while True:
        try:
            idade_aluno_str = input(f"Digite a idade de {nome_aluno}: ")
            idade_aluno = int(idade_aluno_str) # Tenta converter para inteiro
            if idade_aluno <= 0:
                print("A idade deve ser um número positivo. Tente novamente.")
            else:
                break # Sai do loop de idade se for um número válido e positivo
        except ValueError:
            print("Entrada inválida para idade. Por favor, digite um número inteiro.")

    # 3. Coletar as notas nas três disciplinas
    # Vamos usar loops para garantir que as notas sejam números válidos
    notas_disciplinas = []
    disciplinas = ["Matemática", "Ciências", "História"]

    for disciplina in disciplinas:
        while True:
            try:
                nota_str = input(f"Digite a nota de {nome_aluno} em {disciplina}: ")
                nota = float(nota_str) # Tenta converter para float (número decimal)
                if 0 <= nota <= 10: # Valida se a nota está entre 0 e 10
                    notas_disciplinas.append(nota)
                    break # Sai do loop da nota se for válida
                else:
                    print("A nota deve ser entre 0 e 10. Tente novamente.")
            except ValueError:
                print("Entrada inválida para a nota. Por favor, digite um número.")

    # 4. Criar o dicionário para o aluno atual
    # As notas são convertidas em uma tupla, como pedido na atividade
    aluno = {
        'nome': nome_aluno,
        'idade': idade_aluno,
        'notas': tuple(notas_disciplinas) # Converte a lista de notas para uma tupla
    }

    # 5. Adicionar o dicionário do aluno à lista principal
    lista_de_alunos.append(aluno)
    print(f"\nAluno '{nome_aluno}' cadastrado com sucesso!")

# --- Exibir todos os alunos cadastrados ---
print("\n--- Alunos Cadastrados ---")
if not lista_de_alunos: # Verifica se a lista está vazia
    print("Nenhum aluno foi cadastrado.")
else:
    for aluno_cadastrado in lista_de_alunos:
        print(f"Nome: {aluno_cadastrado['nome']}")
        print(f"Idade: {aluno_cadastrado['idade']}")
        print(f"Notas (Matemática, Ciências, História): {aluno_cadastrado['notas']}")
        print("-" * 30) # Linha divisória para melhor visualização