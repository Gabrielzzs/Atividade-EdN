print("Unidades disponíveis: C, F, K")

temp = float(input("Digite a temperatura: "))
origem = input("Converter de (C/F/K): ").upper()
destino = input("Converter para (C/F/K): ").upper()

# Primeiro convertemos tudo para Celsius
if origem == "C":
    celsius = temp
elif origem == "F":
    celsius = (temp - 32) * 5/9
elif origem == "K":
    celsius = temp - 273.15
else:
    print("Unidade de origem inválida!")
    exit()

if destino == "C":
    resultado = celsius
elif destino == "F":
    resultado = (celsius * 9/5) + 32
elif destino == "K":
    resultado = celsius + 273.15
else:
    print("Unidade de destino inválida!")
    exit()

print(f"Resultado: {resultado:.2f}°{destino}")
