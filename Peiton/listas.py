'''
Escreva um programa em Python que receba como entrada o crédito 
de um cliene e depois o preço de itens comprados por este cliente.
O programa deverá parar de solicitar novoas preços quando o crétido
disponível for insuficiente para pagar por um dos itens. Ao final,
exiba o crédito restante.
'''

credito = float(input("Informe seu crédito atual: "))

while (credito > 0):
    valor_item = float(input("preço do item: "))
    if (valor_item <= 0):
        print("Entrada inválida!\nTente novamente")
    elif (valor_item <= credito):
        credito -= valor_item
        print(f"\nSaldoAtual: R${credito:.2f}")
    else:
        print("\nCompra negado, você tá duro 🥵")
        print(f"Saldo atual: R${credito:.2f}\n"+
               f"Valor do produto: R${valor_item:.2f}")
        break
    escolha = input("Quer Continuar comprando?: ")
    if escolha.lower() == "sim":
        print("Manda mais dinheiro pra nós, chefe 😍")
    elif escolha.lower() == "nao":
        print("Obrigado pela sua preferência")
        break

print(f"Saldo restante: R${credito:.2f}")
