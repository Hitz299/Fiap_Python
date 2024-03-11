print('*-* Cálculo da Média *-*')

nota1 = float(input('Nota1: '))
nota2 = float(input('Nota2: '))

n_presenca = int(input('Presenças: '))
total_aula = 50
valor_presenca = 100/total_aula

frequencia = valor_presenca * n_presenca

print(f'Frequencia do aluno: {frequencia: .2f}%' )

media = (nota1 + nota2)/2

print(f'Média: {media: .2f}')

# No Python, os operadores lógicos são os seguintes:
# && -> and; || -> or

if (media >= 6.00 and frequencia >= 75.00):
    print('Aprovado \n meus parabéns')
    
elif (media >= 6 and frequencia < 75.00):
    print('Reprovado por falta')
    
elif (media < 6 and frequencia > 75.00):
    print('Reprovado por nota \n mas faz o teste de rec aí')
    exame = float(input('Nota do Exame: '))
    media = (media + exame)/2
    if (media >= 6):
        print('Aprovado com a recuperação')
    else:
        print('É fi, tu é burro mesmo, não tem jeito')
else:
    print('credo, reprovou por tudo')
    
    
    
    