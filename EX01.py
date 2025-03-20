# Captura o número de colaboradores
num_colaboradores = int(input("Informe o número de colaboradores: "))

# Inicializa contadores para os dias da semana
votos_segunda = 0
votos_terca = 0
votos_quarta = 0
votos_quinta = 0
votos_sexta = 0

# Coleta os votos de cada colaborador
for i in range(1, num_colaboradores + 1):
    voto = input(
        "Informe o dia da sua preferência (segunda-feira, terça-feira, quarta-feira, quinta-feira, sexta-feira): ").lower()

    # Contabiliza os votos de acordo com o dia escolhido
    if voto == "segunda-feira":
        votos_segunda += 1
    elif voto == "terça-feira":
        votos_terca += 1
    elif voto == "quarta-feira":
        votos_quarta += 1
    elif voto == "quinta-feira":
        votos_quinta += 1
    elif voto == "sexta-feira":
        votos_sexta += 1
    else:
        print("Dia inválido, vote novamente.")
        i -= 1  # Reverte a iteração para corrigir o voto inválido

# Verifica qual dia teve mais votos
maior_voto = max(votos_segunda, votos_terca, votos_quarta, votos_quinta, votos_sexta)

# Identifica quais dias têm o maior número de votos
dias_empate = []
if votos_segunda == maior_voto:
    dias_empate.append(("segunda-feira", votos_segunda))
if votos_terca == maior_voto:
    dias_empate.append(("terça-feira", votos_terca))
if votos_quarta == maior_voto:
    dias_empate.append(("quarta-feira", votos_quarta))
if votos_quinta == maior_voto:
    dias_empate.append(("quinta-feira", votos_quinta))
if votos_sexta == maior_voto:
    dias_empate.append(("sexta-feira", votos_sexta))

# Resultado
if len(dias_empate) > 1:
    print("Houve um empate entre os seguintes dias:")
    for dia, votos in dias_empate:
        print(f"{dia.capitalize()} com {votos} votos.")
else:
    print(f"O dia escolhido pelos colaboradores é: {dias_empate[0][0]} com {dias_empate[0][1]} votos.")
