# Exibe as opções de investimento
print("Escolha o tipo de investimento:")
print("1. CDB")
print("2. LCI")
print("3. LCA")

# Capturaa escolha do usuário
tipo_investimento = int(input("Digite o tipo de investimento (1, 2 ou 3): "))

# Verifica se o tipo de investimento é válido
if tipo_investimento not in [1, 2, 3]:
    print("Tipo de investimento inválido.")
else:
    # Se o tipo de investimento for válido, solicitamos o valor e o número de dias
    valor_resgate = float(input("Digite o valor a ser resgatado: "))
    dias_investidos = int(input("Digite o número de dias que o valor permaneceu investido: "))

    # Verifica o tipo de investimento
    if tipo_investimento == 1:  # CDB
        # Aplica as alíquotas de IR com base no número de dias investidos
        if dias_investidos <= 180:
            aliquota_ir = 0.225  # 22,5% de IR
        elif 181 <= dias_investidos <= 360:
            aliquota_ir = 0.20  # 20% de IR
        elif 361 <= dias_investidos <= 720:
            aliquota_ir = 0.175  # 17,5% de IR
        else:
            aliquota_ir = 0.15  # 15% de IR

        # Calcula o valor do imposto de renda
        valor_ir = valor_resgate * aliquota_ir
        print(f"O valor do imposto de renda a ser pago é de: R$ {valor_ir:.2f}")

    elif tipo_investimento in [2, 3]:  # LCI e LCA são isentos de IR
        print("Investimentos em LCI e LCA são isentos de imposto de renda.")
