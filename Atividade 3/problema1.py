#Classificador de Idade

#Criança (0-12 anos),
#Adolescente (13-17 anos),
#Adulto (18-59 anos) ou
#Idoso (60 anos ou mais).

idade = int(input("Digite sua idade: "))
if idade <= 12:
    print("Criança")
elif idade >= 13 and idade <= 17:
    print("Adolescente")
elif idade >= 18 and idade <= 59:
    print("Adulto")
else:
    print("Idoso")