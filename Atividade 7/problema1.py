import pandas as pd
import numpy as np
import os

# Defina o nome do arquivo CSV
NOME_ARQUIVO = 'dados_execucao.csv'

def analisar_tempos_execucao(nome_arquivo):
    """
    Lê um arquivo CSV, calcula a média e o desvio padrão da coluna 'tempo_execucao'.

    Args:
        nome_arquivo (str): O nome do arquivo CSV a ser lido.
    """
    print(f"Tentando ler o arquivo: {nome_arquivo}")

    
    try:
        
        df = pd.read_csv(nome_arquivo)
        print("Arquivo lido com sucesso!")

        
        coluna_alvo = 'tempo_execucao'
        if coluna_alvo not in df.columns:
            
            raise ValueError(f"Erro: A coluna '{coluna_alvo}' não foi encontrada no arquivo CSV.")

        
        df[coluna_alvo] = pd.to_numeric(df[coluna_alvo], errors='coerce')

    
        df_limpo = df.dropna(subset=[coluna_alvo])

        if df_limpo.empty:
            raise ValueError("Erro: Após a limpeza, a coluna 'tempo_execucao' está vazia ou contém apenas dados inválidos.")

        
        media = df_limpo[coluna_alvo].mean()

        
        desvio_padrao = df_limpo[coluna_alvo].std()

        
        print("\n--- Resultados da Análise ---")
        print(f"Total de Registros Válidos: **{len(df_limpo)}**")
        print(f"Média de Execução (μ): **{media:.2f} segundos**")
        print(f"Desvio Padrão (σ): **{desvio_padrao:.2f} segundos**")
        print("-----------------------------\n")

    
    except FileNotFoundError:
        print(f"\n ERRO: O arquivo '{nome_arquivo}' não foi encontrado.")
        print("Certifique-se de que o arquivo está no mesmo diretório do script ou forneça o caminho completo.")

    
    except pd.errors.EmptyDataError:
        print(f"\n ERRO: O arquivo '{nome_arquivo}' está vazio.")
    except pd.errors.ParserError:
        print(f"\n ERRO: Falha ao analisar o arquivo '{nome_arquivo}'. Verifique se o formato CSV está correto.")

    
    except Exception as e:
        print(f"\n ERRO INESPERADO durante o processamento: {e}")


analisar_tempos_execucao(NOME_ARQUIVO)