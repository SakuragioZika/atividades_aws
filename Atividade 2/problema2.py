#Calculadora de Desconto

nome_do_produto: str = 'Camiseta'
preço_original: float = 50.00
porcentagem_de_desconto: int = 20
#O programa deve calcular o valor do desconto e o preço final, exibindo todos os detalhes.

desconto = preço_original * (porcentagem_de_desconto / 100)
preço_final = preço_original - desconto

print(f"Produto: {nome_do_produto}")
print(f"Preço original: R$ {preço_original:.2f}")
print(f"Desconto ({porcentagem_de_desconto}%): R$ {desconto:.2f}")
print(f"Preço final: R$ {preço_final:.2f}")