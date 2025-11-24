#Criar um código que serve para verificar se uma senha digitada pelo usuário atende a critérios básicos de segurança.
 #a - deve ter pelo menos 8 caracteres.
 #b - deve conter pelo menos um número

import re

def verificar_senha(senha):
    """
    Verifica se a senha atende aos critérios de segurança:
    1. Pelo menos 8 caracteres.
    2. Pelo menos um número.
    """
    
    
    if len(senha) < 8:
        return False, "A senha deve ter pelo menos 8 caracteres."
    
    
    if not re.search(r'\d', senha):
        return False, "A senha deve conter pelo menos um número."
    
    
    return True, "Senha válida e segura!"

def main():
    print("--- Verificação de Segurança de Senha ---")
    
    while True:
        senha_usuario = input("Digite a senha para verificação: ")
        valida, mensagem = verificar_senha(senha_usuario)
        
        print(mensagem)
        
        
        if valida:
            break
        else:
            print("Tente novamente...\n")

if __name__ == "__main__":
    main()