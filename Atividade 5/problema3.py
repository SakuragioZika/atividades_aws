#Crie um programa que serve para calcular o preço final de um produto após aplicar um desconto percentual.
#a - Cálculo de desconto: Calcula o valor do desconto baseado em uma porcentagem.
#b - Preço final: Determina o novo preço após o desconto.
#c - Formatação: Arredonda o resultado para 2 casas decimais (centavos).
#d - Interação com usuário: Pede os valores necessários e mostra o resultado formatado.

def calcular_desconto(preco_original, porcentagem):
    """
    Realiza os cálculos de desconto e preço final.
    Retorna uma tupla: (valor_do_desconto, preco_final)
    """
    
    valor_do_desconto = preco_original * (porcentagem / 100)
    
    
    preco_final = preco_original - valor_do_desconto
    
    return valor_do_desconto, preco_final

def main():
    print("--- Calculadora de Preço com Desconto ---")
    
    
    while True:
        try:
            entrada_preco = input("Digite o valor do produto (R$): ")
            entrada_porcentagem = input("Digite a porcentagem de desconto (%): ")
            
            
            preco = float(entrada_preco.replace(',', '.'))
            taxa = float(entrada_porcentagem.replace(',', '.'))
            
            break 
        except ValueError:
            print("Erro: Digite apenas números válidos (ex: 150.00 ou 10).\n")

    
    desconto, final = calcular_desconto(preco, taxa)

    
    print("\n" + "="*30)
    print(f"Preço Original:  R$ {preco:.2f}")
    print(f"Desconto ({taxa}%): -R$ {desconto:.2f}")
    print("-" * 30)
    print(f"PREÇO FINAL:     R$ {final:.2f}")
    print("="*30)

if __name__ == "__main__":
    main()