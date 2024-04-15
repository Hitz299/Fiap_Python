'''
Escreva um programa que receba 4 salários, calcule a média salarial e exiba
os salários que estão abaixo da média

Com adição de lista


ordem_salario = ("primeiro", "segundo", "terceiro", "quarto", "quinto")
salarios = [0,0,0,0,0] #lista com 4 itens
soma = 0
index = 0

for i in salarios:
    salarios[index] = float(input("Digite o valor do salário: R$"))
    soma += salarios[index]
    print(f"\nSeu último salário foi: R${salarios[index]:.2f}")
    print(salarios)
    index += 1
    
media = soma/len(salarios)
index = 0

for i in ordem_salario:
    if salarios[index] < media:
        print(f"\n{i} salário está abaixo de sua média salarial")
    index += 1
    '''
    
    
salarios = [] #criando lista vazia
soma = 0

for _ in range(0,4):
    salario = float(input("\nDigite o salário: R$ "))
    soma += salario
    salarios.append(salario)
    print(", ".join(str(item) for item in salarios))
    
media = soma/len(salarios)

print(f"\nSua média salarial é: R${media}")

for salario in salarios:
    if salario < media:
        print(f"\nO salário R${salario:.3f} está abaixo da média")