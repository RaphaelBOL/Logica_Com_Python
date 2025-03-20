# Solicitar o valor da dívida
valor_divida = float(input("Digite o valor da dívida: "))

# Listas com as quantidades de parcelas e os percentuais de juros correspondentes
parcelas = [1, 3, 6, 9, 12]
juros_percentuais = [0, 0.10, 0.15, 0.20, 0.25]

# Exibe a tabela com uma estrutura de repetição
for i in range(len(parcelas)):
    quantidade_parcelas = parcelas[i]
    juros = juros_percentuais[i]

    # Calcula o valor dos juros e o valor total da dívida
    valor_juros = valor_divida * juros
    valor_total = valor_divida + valor_juros

    # Calcula o valor da parcela
    valor_parcela = valor_total / quantidade_parcelas

    # Exibe os resultados
    print(f"Total: R$ {valor_total:.2f} Juros: R$ {valor_juros:.2f} "
          f"Número de parcelas: {quantidade_parcelas} Valor da Parcela: R$ {valor_parcela:.2f}")
