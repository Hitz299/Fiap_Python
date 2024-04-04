'''
Escreva um Programa em Python que leia 3 notas do usuário,
e depois calcule, imprima a média obtida e o status (aprovado
ou reprovado). Além disso, o programa deve imprimir o
conceito ref, ou seja, a média obtida.

(Média > 9) - A - Excelente
(9 > Média > 8) - B - Ótimo
(8 > Média > 7) - C - Bom
(7 > Média > 6) - D - Regular
(6 > Média > 5) - E - Ruim
(Média < 5) - F - Nos vemos no ano que vem!

'''

print("**- Cálculo da Média de um aluno, utilizando o modelo conceito **-")

nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))
nota3 = float(input("Nota 3: "))

media = (nota1 + nota2 + nota3)/3

print(f"Média final do aluno {media}")

if (media >= 9 and media <= 10):
    conceito = 'A'
    mensagem = "Excelente"
    status = "Aprovado"
elif (media >= 8 and media < 9):
    conceito = 'B'
    mensagem = "Ótimo"
    status = "Aprovado"
elif (media >= 7 and media < 8):
    conceito = 'C'
    mensagem = "Bom"
    status = "Aprovado"
elif (media >= 6 and media < 7):
    conceito = 'D'
    mensagem = "Regular"
    status = "Aprovado"
elif (media >= 5 and media < 6):
    conceito = 'E'
    mensagem = "Ruim"
    status = "Reprovado/Exame"
elif (media < 8):
    conceito = 'F'
    mensagem = "Nos vemos no ano que vem rsrs"
    status = "Reprovado Direto"
else:
    mensagem = "Tá chapando??"
    
match conceito:
    case 'A':
        print(f"{mensagem}\n Conceito {conceito}\n" +
              f"Status: {status}")
    case 'B':
        print(f"{mensagem}\n Conceito {conceito}\n" +
              f"Status: {status}")
    case 'C':
        print(f"{mensagem}\n Conceito {conceito}\n" +
              f"Status: {status}")
    case 'D':
        print(f"{mensagem}\n Conceito {conceito}\n" +
              f"Status: {status}")
    case 'E':
        print(f"{mensagem}\nConceito {conceito}\n" +
              f"Status: {status}")
    case 'F':
        print(f"{mensagem}\n Conceito {conceito}\n" +
              f"Status: {status}")    
    