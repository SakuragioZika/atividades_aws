#Crie um programa que gere senhas aleatórias com letras, números e símbolos e que o usuário  também escolha o tamanho da senha  para criar senhas seguras automaticamente.

import random
import string

def gerar_senha_segura(tamanho):
    """
    Gera uma senha aleatória contendo letras, números e símbolos.
    """
    
    letras = string.ascii_letters  
    numeros = string.digits        
    simbolos = string.punctuation  

    
    todos_caracteres = letras + numeros + simbolos

    
    if tamanho < 4:
        print("Aviso: Senhas com menos de 4 caracteres são pouco seguras.")

    
    senha = "".join(random.choice(todos_caracteres) for _ in range(tamanho))
    
    return senha

def main():
    print("--- GERADOR DE SENHAS AUTOMÁTICO ---")
    print("Para sair do programa, digite 0.\n")

    while True:
        try:
            
            entrada = input("Digite o tamanho da senha desejada (ex: 12): ")
            
            
            tamanho = int(entrada)

            
            if tamanho == 0:
                print("Encerrando o programa. Até mais!")
                break
            
            
            if tamanho < 0:
                print("Por favor, digite um número positivo.")
                continue

            
            senha_gerada = gerar_senha_segura(tamanho)
            print("-" * 40)
            print(f"Sua nova senha segura: {senha_gerada}")
            print("-" * 40 + "\n")

        except ValueError:
            print("Erro: Por favor, digite apenas números inteiros.\n")

if __name__ == "__main__":
    main()