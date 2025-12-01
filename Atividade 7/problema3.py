import os
#leia o arquivo exemplo.txt
def ler_e_exibir_arquivo():
    """
    Solicita um nome de arquivo ao usuário e exibe seu conteúdo, linha por linha.
    Trata o erro caso o arquivo não seja encontrado.
    """
    
    
    nome_arquivo = input("Digite o nome do arquivo que deseja ler (ex: texto.txt): ")
    
    print("-" * 35)
    
    
    try:
        
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            
            print(f"Conteúdo do arquivo '{nome_arquivo}':\n")
            
            
            for numero_linha, linha in enumerate(arquivo, 1):
                
                print(f"Linha {numero_linha}: {linha.strip()}")
                
    
    except FileNotFoundError:
        print(f"ERRO: O arquivo '{nome_arquivo}' não foi encontrado.")
        print("Certifique-se de que o arquivo está no mesmo diretório do script ou forneça o caminho completo.")
        
    
    except Exception as e:
        print(f"Ocorreu um erro inesperado ao ler o arquivo: {e}")
        
    print("-" * 35)


ler_e_exibir_arquivo()