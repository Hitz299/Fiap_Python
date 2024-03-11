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

if (media >= 6.00 and frequencia >= 75.00):
    print('Aprovado \n meus parabéns')
    
elif (media >= 6 and frequencia < 75.00):
    print('Reprovado por falta')
    
elif (media < 6 and frequencia > 75.00):
    print('Reprovado por nota')
    
else:
    print('credo, reprovou por tudo')
    
# No Python, os operadores lógicos são os seguintes:
# && -> and; || -> or
    
    