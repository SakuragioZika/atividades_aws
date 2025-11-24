#Crie um programa que realize consultas a  em relação ao Real (BRL) usando a API mostre valor atual, máxima, mínima e data/hora da última atualização, caso a moeda não existir ou houver erro na requisição, retorne uma mensagem de erro.

import requests

def consultar_cotacao():
    print("--- CONSULTA DE CÂMBIO (AwesomeAPI) ---")
    print("Moedas comuns: USD (Dólar), EUR (Euro), BTC (Bitcoin)")
    print("Digite 'sair' para encerrar.\n")

    while True:
        
        moeda_origem = input("Digite o código da moeda (ex: USD): ").strip().upper()

        
        if moeda_origem == 'SAIR':
            print("Encerrando o sistema...")
            break
        
        
        if not moeda_origem:
            print("Por favor, digite um código válido.")
            continue

        
        url = f"https://economia.awesomeapi.com.br/last/{moeda_origem}-BRL"

        try:
            print(f"Consultando cotação do {moeda_origem}...")
            
            
            response = requests.get(url, timeout=10)
            
            
            response.raise_for_status()
            
            
            dados = response.json()
            
            
            chave_api = f"{moeda_origem}BRL"
            
            if chave_api in dados:
                info = dados[chave_api]
                
                nome = info.get('name', moeda_origem)
                valor_atual = float(info['bid'])
                maxima = float(info['high'])
                minima = float(info['low'])
                data_atualizacao = info['create_date']

                
                print("\n" + "=" * 40)
                print(f" {nome}")
                print("=" * 40)
                print(f"Valor Atual:   R$ {valor_atual:.2f}")
                print(f"Máxima do dia: R$ {maxima:.2f}")
                print(f"Mínima do dia: R$ {minima:.2f}")
                print(f"Atualizado em: {data_atualizacao}")
                print("-" * 40 + "\n")
            else:
                
                print(f"Erro: Dados da moeda {moeda_origem} não encontrados na resposta.\n")

        except requests.exceptions.HTTPError:
            
            print(f"Erro: A moeda '{moeda_origem}' não foi encontrada ou é inválida.\n")
            
        except requests.exceptions.ConnectionError:
            
            print("Erro de Conexão: Verifique sua internet.\n")
            
        except Exception as e:
            
            print(f"Erro inesperado: {e}\n")

if __name__ == "__main__":
    consultar_cotacao()