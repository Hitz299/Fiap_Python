def erro_entrada(entrada):
    while entrada != 1 and entrada != 2:
        entrada = int(input("Entrada inválida\n"))
    return entrada


escolha = int(input("Digite um valor para realizar sua escolha:\n" +
          "1-> sim\n2-> não\n"))

escolha = erro_entrada(escolha)

if escolha == 1:
    print("Sim")

if escolha == 2:
    print("Não")

