# Solicita o preço do carro
preco_carro = float(input("Digite o preço do carro: "))

# Calcula do preço final à vista com desconto de 20%
preco_vista = preco_carro * 0.80
print(f"O preço final à vista com desconto de 20% é: R$ {preco_vista:.2f}")

# Tabela de parcelas e os percentuais de acréscimo
parcelas = [6, 12, 18, 24, 30, 36, 42, 48, 54, 60]
percentuais_acrescimo = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]

# Exibir a tabela de opções parceladas
for i in range(len(parcelas)):
    # Cálculo do preço final com o acréscimo percentual
    acrescimo = percentuais_acrescimo[i] / 100
    preco_final_parcelado = preco_carro * (1 + acrescimo)

    # Cálcula o valor da parcela
    valor_parcela = preco_final_parcelado / parcelas[i]

    # Exibe os resultados
    print(f"O preço final parcelado em {parcelas[i]}x é de R$ {preco_final_parcelado:.2f} "
          f"com parcelas de R$ {valor_parcela:.2f}")
