#Criar um código que serve para analisar números digitados pelo usuário, classificando-os como pares ou ímpares e contabilizando quantos de cada tipo foram inseridos.

def analisar_numeros():
    pares = 0
    impares = 0
    
    print("Digite números inteiros para análise (digite 'sair' para encerrar):")
    
    while True:
        entrada = input("Número: ")
        
        if entrada.lower() == 'sair':
            break
        
        try:
            numero = int(entrada)
            
            if numero % 2 == 0:
                pares += 1
                print(f"{numero} é um número par.")
            else:
                impares += 1
                print(f"{numero} é um número ímpar.")
        
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro ou 'sair' para encerrar.")
    
    print("\nAnálise final:")
    print(f"Números pares inseridos: {pares}")
    print(f"Números ímpares inseridos: {impares}")
    print("Encerrando o programa.")

if __name__ == "__main__":
    analisar_numeros()

