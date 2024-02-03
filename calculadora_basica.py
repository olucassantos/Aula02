print("Bem vindo ao CalcExtreme 3499VX Plus")

print("Selecione a operação desejada: ")
print("+ - Soma")
print("- - Subtração")
print("* - Multiplicação")
print("/ - Divisão")

operacao = input("Digite sua opção: ")
numero_um = float(input("Digite o primeiro número: "))
numero_dois = float(input("Digite o segundo número: "))

if operacao == "+":
    print(f"A soma dos numeros é: {numero_um + numero_dois}")
elif operacao == "-":
    print(f"A subtração dos numeros é: {numero_um - numero_dois}")
elif operacao == "*":
    print(f"A multiplicação dos numeros é: {numero_um * numero_dois}")
elif operacao == "/":
    if (numero_dois == 0):
        print("Não é possível dividir por zero")
    else:
        print(f"A divisão dos numeros é: {numero_um / numero_dois}")
else:
    print("Operação inválida")