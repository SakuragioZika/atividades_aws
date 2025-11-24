#Calculadora de IMC

#Desenvolva um programa que calcule o Índice de Massa Corporal (IMC) de uma pessoa.
#O programa deve solicitar o peso (em kg) e a altura (em metros) do usuário,
#calcular o IMC e fornecer a classificação de acordo com a tabela padrão de IMC.

#< 18.5: classificacao = "Abaixo do peso"
#< 25: classificacao = "Peso normal"
#< 30: classificacao = "Sobrepeso"
#Para os demais cenários: classificacao = "Obeso"

while True:
    # 1. Obter entradas
    try:
        peso = float(input("Digite seu peso em kg (ou digite '0' para sair): "))
        
        
        if peso == 0:
            print("Calculadora encerrada.")
            break # Interrompe o loop
            
        altura = float(input("Digite sua altura em metros: "))

        
        if altura <= 0 or peso < 0:
            print("Valores inválidos. Altura e peso devem ser positivos.")
            continue # Pula para a próxima iteração do loop

    except ValueError:
        print("Entrada inválida. Por favor, digite um número.")
        continue # Pula para a próxima iteração do loop

    # 2. Calcular IMC
    imc = peso / (altura ** 2)

    # 3. Classificação
    if imc < 18.5:
        classificacao = "Abaixo do peso"
    elif imc < 25:
        classificacao = "Peso normal"
    elif imc < 30:
        classificacao = "Sobrepeso"
    else:
        classificacao = "Obeso"

    
    print("\nSeu IMC é: %.2f" % imc)
    print("Classificação: ", classificacao)
    print("-" * 30, "\n")