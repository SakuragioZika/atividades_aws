#Crie uma função que verifique se uma palavra ou frase é um palíndromo (lê-se igual de trás para frente, ignorando espaços e pontuação). Se o resultado é True, responda “Sim”, se o resultado for False, responda “Não”.

import unicodedata
import re

def verificar_palindromo(texto):
    """
    Verifica se uma frase é um palíndromo (lê-se igual de trás para frente).
    Ignora espaços, pontuação, acentos e diferenças entre maiúsculas/minúsculas.
    
    Retorna: "Sim" ou "Não"
    """
    
   
    nfkd = unicodedata.normalize('NFKD', texto)
    
    
    texto_sem_acento = nfkd.encode('ASCII', 'ignore').decode('ASCII')
    
    
    texto_limpo = re.sub(r'[^a-zA-Z0-9]', '', texto_sem_acento).lower()
    
    
    texto_invertido = texto_limpo[::-1]
    
    
    if texto_limpo == texto_invertido:
        return "Sim"
    else:
        return "Não"

def main():
    print("--- Verificador de Palíndromos ---")
    print("Exemplos: 'Ovo', 'Arara', 'A grama é amarga', 'Socorram-me, subi no ônibus em Marrocos'")
    print("Digite 'sair' para encerrar.\n")

    while True:
        entrada = input("Digite uma palavra ou frase: ")
        
        if entrada.lower() == 'sair':
            break
            
        resultado = verificar_palindromo(entrada)
        print(f"É um palíndromo? {resultado}")
        print("-" * 30)

if __name__ == "__main__":
    main()