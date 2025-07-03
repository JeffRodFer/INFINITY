print("--- Exemplo 1: Todas as chaves existem ---")
dados_usuario = {"nome": "Maria", "idade": 25, "cidade": "Recife"}
chaves_obrigatorias_1 = ["nome", "sexo"]
todas_presentes_1 = True # Começamos assumindo que todas as chaves estão presentes

print(f"Dicionário: {dados_usuario}")
print(f"Chaves a verificar: {chaves_obrigatorias_1}")

for chave in chaves_obrigatorias_1:
    if chave not in dados_usuario:
        todas_presentes_1 = False # Encontramos uma chave que não está, então mudamos para False
        break # Não precisamos verificar as outras, já sabemos que não são todas
        
print(f"Todas as chaves existem? {todas_presentes_1}\n")