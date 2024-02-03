print("Sistema de classificação de Notas")
nota = float(input("Digite sua nota: "))

if nota > 100 or nota < 0:
    print("Nota inválida")
elif nota >= 90:
    print("Nota A")
elif nota >= 80:
    print("Nota B")
elif nota >= 70:
    print("Nota C")
elif nota >= 60:
    print("Nota D")
else:
    print("Nota F")