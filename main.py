peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

imc = peso / (altura * altura)

print("Seu IMC é: ", imc)

if imc < 16:
    print("Peso Deficitário Grave")
elif imc < 18.5:
    print("Abaixo do Peso")
elif imc < 25:
    print("Peso Normal")
elif imc < 30:
    print("Acima do Peso")
elif imc < 35:
    print("Obesidade Grau I")
elif imc < 40:
    print("Obesidade Grau II")
else:
    print("Obesidade Grau III")