def adicionar(x, y):
    return x + y

def subtrair(x, y):
    return x - y

def multiplicar(x, y):
    return x * y

def dividir(x, y):
    
    if y == 0:
        return "Erro: Divisão por zero!"
    return x / y


def main():
    while True:
        print("\n" + "=" * 30)
        print("    CALCULADORA PYTHON")
        print("=" * 30)
        print("Selecione a operação:")
        print("1. Adição (+)")
        print("2. Subtração (-)")
        print("3. Multiplicação (*)")
        print("4. Divisão (/)")
        print("5. Sair")
        
        escolha = input("Digite a opção (1/2/3/4/5): ")

        
        if escolha == '5':
            print("Obrigado por usar a calculadora. Até mais!")
            break 

        
        if escolha in ('1', '2', '3', '4'):
            try:
                
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))
                
                resultado = None 

                
                if escolha == '1':
                    resultado = adicionar(num1, num2)
                    operacao_simbolo = '+'
                elif escolha == '2':
                    resultado = subtrair(num1, num2)
                    operacao_simbolo = '-'
                elif escolha == '3':
                    resultado = multiplicar(num1, num2)
                    operacao_simbolo = '*'
                elif escolha == '4':
                    resultado = dividir(num1, num2)
                    operacao_simbolo = '/'
                
                
                if isinstance(resultado, str):
                    print(resultado) 
                else:
                    print(f"\nResultado: {num1} {operacao_simbolo} {num2} = {resultado}")

            except ValueError:
                print("\nOpção inválida: Por favor, digite apenas números válidos.")
            
            
            continue 

        else:
            print("\nOpção inválida. Por favor, escolha uma opção entre 1 e 5.")


if __name__ == "__main__":
    main()