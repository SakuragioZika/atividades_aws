import json
import os


NOME_ARQUIVO_JSON = 'dados_pessoa.json'

def manipular_arquivo_json():
    """
    Cria um dicionário, salva-o em um arquivo JSON e depois lê o arquivo,
    exibindo os dados ou uma mensagem de erro em caso de falha.
    """
    
    
    dados_pessoa = {
        'nome': 'Júlia Santos',
        'idade': 30,
        'cidade': 'Porto Alegre'
    }
    
    print("--- 💾 SALVANDO DADOS NO JSON ---")
    
    
    try:
        
        with open(NOME_ARQUIVO_JSON, 'w', encoding='utf-8') as arquivo:
            
            json.dump(dados_pessoa, arquivo, indent=4)
            
        print(f"✅ Sucesso! Os dados foram salvos em '{NOME_ARQUIVO_JSON}'.")
        
    except Exception as e:
        print(f"❌ FALHA ao salvar o arquivo '{NOME_ARQUIVO_JSON}'.")
        print(f"Detalhes do erro: {e}")
        
        return 
        
    print("\n--- 🔎 LENDO DADOS DO JSON ---")
    
    
    dados_lidos = None
    try:
        
        with open(NOME_ARQUIVO_JSON, 'r', encoding='utf-8') as arquivo:
            
            dados_lidos = json.load(arquivo)
            
        print(f"✅ Sucesso! Dados lidos do arquivo '{NOME_ARQUIVO_JSON}':")
        
        
        print("-" * 35)
        print(f"Nome: {dados_lidos.get('nome', 'N/A')}")
        print(f"Idade: {dados_lidos.get('idade', 'N/A')}")
        print(f"Cidade: {dados_lidos.get('cidade', 'N/A')}")
        print("-" * 35)

    except FileNotFoundError:
        
        print(f"ERRO: O arquivo '{NOME_ARQUIVO_JSON}' não foi encontrado para leitura.")
        
    except json.JSONDecodeError:
        print(f"ERRO: O arquivo '{NOME_ARQUIVO_JSON}' está corrompido ou não está em formato JSON válido.")
        
    except Exception as e:
        print(f"Ocorreu um erro inesperado ao ler o arquivo: {e}")


manipular_arquivo_json()