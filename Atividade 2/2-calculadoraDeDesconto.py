
produto = "Camiseta"
preco_original = 50.00
desconto_percentual = 20

desconto = preco_original * (desconto_percentual / 100)
preco_final = preco_original - desconto

print("=== Calculadora de Desconto ===")
print(f"Produto: {produto}")
print(f"Preço original: R$ {preco_original:.2f}")
print(f"Desconto aplicado: {desconto_percentual}%")
print(f"Valor do desconto: R$ {desconto:.2f}")
print(f"Preço final: R$ {preco_final:.2f}")
