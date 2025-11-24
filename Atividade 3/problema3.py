#Conversor de Temperatura

#Desenvolva um programa que converta uma temperatura fornecida em graus Celsius para Fahrenheit e Kelvin.
#O usuário deve informar a temperatura, a unidade de origem e a unidade para qual deseja converter.

def converter_temperatura(valor, unidade_origem, unidade_destino):
    """Converte uma temperatura entre Celsius, Fahrenheit e Kelvin."""


    u_origem = unidade_origem.lower()[0]
    u_destino = unidade_destino.lower()[0]

    
    if u_origem not in ('c', 'f', 'k') or u_destino not in ('c', 'f', 'k'):
        return None, "Unidade de origem ou destino inválida. Use C, F ou K."
    
   
    if u_origem == u_destino:
        return valor, f"Unidade de origem e destino são as mesmas ({unidade_origem})."

    
    temp_celsius = 0
    if u_origem == 'c':
        temp_celsius = valor
    elif u_origem == 'f':
        
        temp_celsius = (valor - 32) * (5/9)
    elif u_origem == 'k':
        
        temp_celsius = valor - 273.15

    
    resultado = 0
    if u_destino == 'c':
        resultado = temp_celsius
    elif u_destino == 'f':
        
        resultado = temp_celsius * (9/5) + 32
    elif u_destino == 'k':
        
        resultado = temp_celsius + 273.15
        
    return resultado, None


try:
    
    temperatura = float(input("Digite a temperatura: "))

   
    origem = input("Unidade de origem (C, F ou K): ")

    
    destino = input("Unidade para qual deseja converter (C, F ou K): ")

   
    valor_convertido, erro = converter_temperatura(temperatura, origem, destino)

    
    if erro:
        print(f"\nERRO: {erro}")
    else:
        print("-" * 30)
        print(f"{temperatura:.2f}°{origem.upper()[0]} é igual a:")
        print(f"{valor_convertido:.2f}°{destino.upper()[0]}")
        print("-" * 30)

except ValueError:
    print("\nERRO: Por favor, digite um valor numérico válido para a temperatura.")