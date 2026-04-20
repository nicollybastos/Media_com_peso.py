print("-" * 45)
print("SEJA BEM-VINDO AO CALCULO DA MÉDIA DA SUA SALA")
print("-" * 45)

nome = input("Digite o nome do aluno: ")
qtd_disciplinas = int(input("Digite a quantidade de disciplinas: "))


soma_notas_com_peso = 0
soma_dos_pesos = 0

for i in range(qtd_disciplinas):
    print(f"\nDisciplina {i+1}:")
    nome_disciplina = input("Nome da disciplina: ")
    nota = float(input(f"Nota do aluno em {nome_disciplina}: "))
    
    peso_input = input(f"Peso para {nome_disciplina} (Pressione Enter para peso 1): ")
    
    # Se o usuário não digitar nada, o peso padrão é 1
    if peso_input == "":
        peso = 1.0
    else:
        peso = float(peso_input)
  
    soma_notas_com_peso += (nota * peso)
    soma_dos_pesos += peso

# Cálculo final da média
if soma_dos_pesos > 0:
    media_final = soma_notas_com_peso / soma_dos_pesos
else:
    media_final = 0

# Verificação de aprovação
if media_final >= 5.0:
    resultado = "APROVADO"
else:
    resultado = "REPROVADO"

print("\n" + "="*30)
print("       RESULTADO FINAL")
print("="*30)
print(f"Nome do aluno: {nome}")
print(f"Média do aluno: {media_final:.1f}")
print(f"Resultado: {resultado}")
print("="*30)
