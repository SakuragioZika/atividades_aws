#Crie um programa que consulte informações de um  na API , retorne logradouro, bairro, cidade e estado do CEP digitado, caso o CEP não existir ou houver erro na requisição, mostre uma mensagem de falha.

import requests

def consultar_cep():
    print("--- CONSULTA DE ENDEREÇO VIA CEP ---")
    print("Digite 'sair' para encerrar o programa.\n")

    while True:
        cep_input = input("Digite o CEP (apenas números ou com traço): ").strip()

        
        if cep_input.lower() == 'sair':
            print("Encerrando...")
            break

        
        cep_limpo = cep_input.replace("-", "").replace(".", "")

        
        if len(cep_limpo) != 8 or not cep_limpo.isdigit():
            print("Formato inválido. O CEP deve conter 8 números.\n")
            continue

        
        url = f"https://viacep.com.br/ws/{cep_limpo}/json/"

        try:
            print("Buscando informações...")
            
            
            response = requests.get(url, timeout=5)
            
            
            response.raise_for_status()

            
            dados = response.json()

            
            if "erro" in dados:
                print(f"O CEP {cep_input} não foi encontrado na base de dados.\n")
            else:
                
                print("-" * 40)
                print(f" ENDEREÇO ENCONTRADO:")
                print(f"Logradouro: {dados.get('logradouro', 'N/A')}")
                print(f"Bairro:     {dados.get('bairro', 'N/A')}")
                print(f"Cidade:     {dados.get('localidade', 'N/A')}")
                print(f"Estado:     {dados.get('uf', 'N/A')}")
                print("-" * 40 + "\n")

        except requests.exceptions.ConnectionError:
            print("Erro de Conexão: Verifique sua internet.\n")
        except requests.exceptions.Timeout:
            print("Erro: O servidor demorou muito para responder.\n")
        except Exception as e:
            print(f"Erro inesperado ao consultar a API: {e}\n")

if __name__ == "__main__":
    consultar_cep()