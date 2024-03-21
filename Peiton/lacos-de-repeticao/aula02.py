
'''

ent = input("Digite sua escolha: ")
num = 0

while (ent == "sim" or ent == "Sim"):
    num += 1;
    print(num);
    ent = input("Digite sua escolha: ")
    
print(num)
'''
'''

Crie um programa que receba como entrada os preços de itens comprados 
em um supermercado por um cliente, ao final, o programa deverá exibir o total
da compra. Para informar que não há mais itens a serem comprados, o cliente deve
digitar o valor -1. 
'''
compras = float(input("Digite o valor da compra: "))
valorPagamento = 0;

while compras != -1:
    valorPagamento += compras
    print(f"valor a pagar 🥵 {valorPagamento}R$")
    compras = float(input("Valor do próximo item: "))

print(f"Sua compra ficou {valorPagamento}R$")