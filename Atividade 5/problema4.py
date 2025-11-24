#Crie um programa que calcule a quantos dias um individuo está vivo de acordo com a data do dia.

from datetime import datetime
def calcular_dias_vivo(data_nascimento):
    """
    Calcula o número de dias que uma pessoa está viva com base na data de nascimento fornecida.

    Parâmetros:
    data_nascimento (str): Data de nascimento no formato 'DD/MM/AAAA'

    Retorna:
    int: Número de dias vividos
    """
    try:
        # Converter a string de data para um objeto datetime
        nascimento = datetime.strptime(data_nascimento, "%d/%m/%Y")
        
        # Obter a data atual
        hoje = datetime.now()
        
        # Calcular a diferença em dias
        dias_vivo = (hoje - nascimento).days
        
        return dias_vivo
    except ValueError:
        print("Data inválida. Por favor, use o formato DD/MM/AAAA.")
        return None
def main():
    print("--- Calculadora de Dias Vividos ---")
    
    data_nascimento = input("Digite sua data de nascimento (DD/MM/AAAA): ")
    
    dias = calcular_dias_vivo(data_nascimento)
    
    if dias is not None:
        print(f"Você está vivo há {dias} dias!")

if __name__ == "__main__":
    main()
    
    
