print('*-* Cálculo da Média *-*')

nota1 = float(input('nota1: '))
nota2 = float(input('nota2: '))

media = (nota1 + nota2)/2

print(f'Média: {media: .2f}')

if (media >= 6.00):
    print('Aprovado \n meus parabéns')
    
else:
    print('credo')