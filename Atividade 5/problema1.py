#Crie uma função que calcule a gorjeta a ser deixada em um restaurante, baseada no valor total da conta e na porcentagem de
#gorjeta desejada. Calcula o valor da gorjeta baseado no total da conta e na porcentagem desejada.
#Parâmetros:
#a - valor_conta (float): O valor total da conta
#b - porcentagem_gorjeta (float): A porcentagem da gorjeta (ex: 10 para 10%)
#c - retorna: float: O valor da gorjeta calculada

def calcular_gorjeta(valor_conta, porcentagem_gorjeta):
    """
    Calcula o valor da gorjeta baseado no total da conta e na porcentagem desejada.

    Parâmetros:
    a - valor_conta (float): O valor total da conta
    b - porcentagem_gorjeta (float): A porcentagem da gorjeta (ex: 10 para 10%)
    
    Retorna:
    c - float: O valor da gorjeta calculada
    """
    
    
    if valor_conta < 0 or porcentagem_gorjeta < 0:
        return 0.0

    gorjeta = valor_conta * (porcentagem_gorjeta / 100)
    return gorjeta

def main():
    print("--- Calculadora de Gorjeta ---")
    
    try:
        
        valor = float(input("Digite o valor total da conta (R$): "))
        porcentagem = float(input("Digite a porcentagem da gorjeta (ex: 10): "))

        
        valor_da_gorjeta = calcular_gorjeta(valor, porcentagem)
        
        
        total_final = valor + valor_da_gorjeta

        
        print("-" * 30)
        print(f"Valor da conta:     R$ {valor:.2f}")
        print(f"Porcentagem:        {porcentagem}%")
        print(f"Valor da gorjeta:   R$ {valor_da_gorjeta:.2f}")
        print("-" * 30)
        print(f"TOTAL A PAGAR:      R$ {total_final:.2f}")

    except ValueError:
        print("\nErro: Por favor, digite apenas números válidos (use ponto para decimais).")

if __name__ == "__main__":
    main()