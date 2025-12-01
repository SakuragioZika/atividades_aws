import csv
import os

def criar_e_salvar_csv():
    """
    Cria uma lista de dados de pessoas e salva em um arquivo CSV 
    cujo nome é fornecido pelo usuário.
    """
    
    
    cabecalho = ['Nome', 'Idade', 'Cidade']
    
    
    dados_pessoas = [
        ['Ana Silva', 28, 'São Paulo'],
        ['Bruno Costa', 35, 'Rio de Janeiro'],
        ['Carla Souza', 22, 'Belo Horizonte'],
        ['Daniel Lima', 40, 'Curitiba']
    ]
    
    print("Dados a serem salvos (Formato Tabular):")
    print("-" * 30)
    print(f"| {cabecalho[0]:<15} | {cabecalho[1]:<5} | {cabecalho[2]:<10} |")
    print("-" * 30)
    for linha in dados_pessoas:
         print(f"| {linha[0]:<15} | {linha[1]:<5} | {linha[2]:<10} |")
    print("-" * 30)
    
    
    
    nome_arquivo = input("\n Digite o nome do arquivo CSV para salvar (ex: pessoas.csv): ")
    
    
    if not nome_arquivo.lower().endswith('.csv'):
        nome_arquivo += '.csv'
        
    
    
    try:
        
        with open(nome_arquivo, 'w', newline='', encoding='utf-8') as arquivo_csv:
            
            
            writer = csv.writer(arquivo_csv)
            
            
            writer.writerow(cabecalho)
            
           
            writer.writerows(dados_pessoas)
            
        
        print(f"\n SUCESSO! Os dados foram salvos em: '{os.path.abspath(nome_arquivo)}'")
        
    except Exception as e:
        
        print(f"\nFALHA ao salvar o arquivo: {nome_arquivo}")
        print(f"Detalhes do erro: {e}")

criar_e_salvar_csv()