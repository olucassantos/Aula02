# Apenas compras com mais de 800 reais podem ser parceladas acima de 5x;
# Juros:
    # 1 – 11 vezes: 5% de juros ao mês.
    # 2 – 12 vezes: 6.5% de juros ao mês.
    # 3 – 13 vezes: 7% de juros ao mês.
    # 4 – 14 vezes: 9% de juros ao mês.
    # 5 – 15 vezes: 9.5% de juros ao mês.
    # 6 – 16 vezes: 10% de juros ao mês.
    # 7 – 17 vezes: 11.3% de juros ao mês.
    # 8 – 18 vezes: 12% de juros ao mês. 

print("Bem vinde a loja de roupas!")

# Solicitação de informações do usuário
valor_compra = float(input("Qual o valor da compra?"))

print("Você pode fazer o pagamento à vista ou parcelado.")
print("Compras parceladas podem ser em até 18 vezes, quando acima de 800 reais.")
print("Compras acima de 10 vezes terão juros.")

print("Formas de pagamento:")
print("1 - À vista")
print("2 - Parcelado")
forma_pagamento = input("Informe a forma: ")

if forma_pagamento == "1":
    # Decide a porcentagem de desconto

    if valor_compra > 1000:
        desconto = 20
    elif valor_compra > 500:
        desconto = 15
    else:
        desconto = 10

    # Calcula o valor final
    valor_final = valor_compra - (valor_compra * (desconto / 100))

elif forma_pagamento == "2":
    # Solicita o número de parcelas
    if valor_compra <= 800:
        print("Compras abaixo de R$ 800 podem ser parceladas em até 5x!")

    parcelas = int(input("Informe a quantidade de parcelas: "))

    if valor_compra <= 800 and parcelas > 5:
        print("Compras abaixo de R$ 800 não podem ser parceladas em mais de 5x!")
        # Encerra o programa
        exit()

    if parcelas > 18:
        print("Compras acima de 18 vezes não são permitidas!")
        exit()

    valor_juros = 0
    if parcelas > 10:
        # Aplica o juros!
        if parcelas == 11: juros = 5
        elif parcelas == 12: juros = 6.5
        elif parcelas == 13: juros = 7
        elif parcelas == 14: juros = 9
        elif parcelas == 15: juros = 9.5
        elif parcelas == 16: juros = 10
        elif parcelas == 17: juros = 11.3
        elif parcelas == 18: juros = 12

        # Calcula o valor do juros
        valor_juros = valor_compra * (juros / 100)

    # Calcula o valor final
    valor_parcela = (valor_compra / parcelas) + valor_juros
    valor_final = valor_parcela * parcelas

# Imprime o resultado final
if forma_pagamento == "1":
    print(f"Sua compra teve um desconto de {desconto}%!")
else:
    # Parcelamento
    if parcelas > 10:
        print(f"Sua compra será parcelada em {parcelas} vezes, com juros de {juros}% ao mês!")
    else:
        print(f"Sua compra será parcelada em {parcelas} vezes!")

    print (f"O valor de cada parcela será de R$ {valor_parcela:.2f}")

# Imprime o valor final
print(f"O valor final é de R$ {valor_final:.2f}")