#Crie um programa que  acesse a API  para buscar um usuário fictício aleatório. exibindo o nome, e-mail e país desse usuário, caso houver erro na conexão, mostre uma mensagem de falha.
# no cmd execute o seguinte código: pip install requests
import requests

def buscar_usuario_aleatorio():
    
    url = "https://randomuser.me/api/"

    print("Conectando à API para buscar dados...")

    try:
        
        response = requests.get(url, timeout=5)

        
        response.raise_for_status()

        
        dados = response.json()

        
        usuario = dados['results'][0]

        
        nome_completo = f"{usuario['name']['first']} {usuario['name']['last']}"
        email = usuario['email']
        pais = usuario['location']['country']

        
        print("\n" + "=" * 40)
        print(f"👤  USUÁRIO ENCONTRADO")
        print("=" * 40)
        print(f"Nome:   {nome_completo}")
        print(f"E-mail: {email}")
        print(f"País:   {pais}")
        print("-" * 40)

    except requests.exceptions.ConnectionError:
        print("\n FALHA: Erro de conexão. Verifique sua internet.")
    except requests.exceptions.Timeout:
        print("\n FALHA: A conexão demorou muito para responder (Timeout).")
    except requests.exceptions.RequestException as erro:
        
        print(f"\n FALHA: Ocorreu um erro ao acessar a API: {erro}")
    except Exception as e:
        
        print(f"\n Erro inesperado: {e}")

if __name__ == "__main__":
    buscar_usuario_aleatorio()