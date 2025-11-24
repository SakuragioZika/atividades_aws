#Criar um código que registre as notas de alunos e calcular a média da turma.

def main():
    print("--- SISTEMA DE GESTÃO DE NOTAS ESCOLARES ---")
    
    turma = []  
    
    while True:
        print("\n--- Novo Aluno ---")
        nome = input("Nome do aluno: ")
        
       
        while True:
            try:
                qtd_notas = int(input(f"Quantas notas para o aluno {nome}? "))
                if qtd_notas > 0:
                    break
                print("Por favor, digite um número maior que zero.")
            except ValueError:
                print("Entrada inválida. Digite um número inteiro.")
        
        notas = []
        for i in range(qtd_notas):
            
            while True:
                try:
                    nota = float(input(f"Digite a nota {i+1}: "))
                    if 0 <= nota <= 10:  # Assumindo notas de 0 a 10
                        notas.append(nota)
                        break
                    else:
                        print("A nota deve ser entre 0 e 10.")
                except ValueError:
                    print("Por favor, digite um número válido (ex: 7.5).")
        
        
        media_aluno = sum(notas) / len(notas)
        
        
        aluno = {
            "nome": nome,
            "notas": notas,
            "media": media_aluno
        }
        turma.append(aluno)
        
        
        continuar = input("\nDeseja adicionar outro aluno? (s/n): ").lower()
        if continuar != 's':
            break
    
    
    print("\n" + "="*40)
    print(f"{'RELATÓRIO DA TURMA':^40}")
    print("="*40)
    
    soma_medias_turma = 0
    
    
    print(f"{'ALUNO':<20} | {'MÉDIA':<10} | {'SITUAÇÃO'}")
    print("-" * 40)
    
    for aluno in turma:
        soma_medias_turma += aluno['media']
        
        
        situacao = "Aprovado" if aluno['media'] >= 6.0 else "Reprovado"
        
        print(f"{aluno['nome']:<20} | {aluno['media']:<10.2f} | {situacao}")
    
    print("-" * 40)
    
    
    if len(turma) > 0:
        media_geral_turma = soma_medias_turma / len(turma)
        print(f"\nMédia Geral da Turma: {media_geral_turma:.2f}")
    else:
        print("\nNenhum aluno registrado.")
        
    print("="*40)

if __name__ == "__main__":
    main()